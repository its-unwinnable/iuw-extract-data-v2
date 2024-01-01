from iuw_extract_data.extract_match_ids import ExtractMatchIds
from iuw_extract_data import helpers

import logging

from rito.models import ChampionMastery
from rito.errors import ExtractorError


logger = logging.getLogger(__name__)


class ExtractData:
    def __init__(self, extractor_match_ids: ExtractMatchIds) -> None:
        self.extractor_match_ids = extractor_match_ids
        
        self.rito_client = extractor_match_ids.rito_client
        self.extractor_client = extractor_match_ids.extractor_client

    def extract_samples(self, n: int) -> None:
        samples = []
        while len(samples) < n:
            try:
                match_id = self.extractor_match_ids.next_match_id()
                
                match_dict = self.rito_client.match.by_match_id(match_id=match_id)

                sample = self._build_sample(match_dict=match_dict)
                samples.append(sample)
                logger.info(f"progression: {len(samples)}/{n} ({len(samples)/n:.2%}")

            except Exception as e:
                logger.error(f"{e.__class__.__name__}: {e}")
        
        return samples

    def _build_sample(self, match_dict: dict) -> dict:
        sample = {}
        
        match = self.extractor_client.match.extract(match_dict=match_dict)
        match_totals = self.extractor_client.match.extract_totals(match_dict=match_dict)
        
        sample["match"] = match.dict(exclude={"participants_puuid", "participants_id"})
        sample["match_totals"] = [match_total.dict() for match_total in match_totals]
        sample["summoners"] = []

        start_time_last_match = helpers.get_timestamp_utc()-(86400*8)
        for summoner_id in match.participants_id:
            sample_summoner = self._build_sample_summoner(
                match_dict=match_dict, 
                summoner_id=summoner_id, 
                start_time_last_match=start_time_last_match
            )
            sample["summoners"].append(sample_summoner)

        return sample
    
    def _build_sample_summoner(self, match_dict: dict, summoner_id: str, start_time_last_match: int) -> dict:
        sample_summoner = {}
        
        # Summoner + Entries: requests
        summoner_dict = self.rito_client.summoner.by_id(summoner_id=summoner_id)
        entries_list = self.rito_client.league.entries.by_summoner(summoner_id=summoner_id)

        # Match Summoner + Summoner + Entries: extractions
        match = self.extractor_client.match.extract(match_dict=match_dict)
        match_summoner = self.extractor_client.match.extract_summoner(match_dict=match_dict, summoner_id=summoner_id)
        summoner = self.extractor_client.summoner.extract(summoner_dict)
        entries = self.extractor_client.league.entries.extract(entries_list=entries_list)

        # Champion Masteries: request + extractions
        champion_masteries_list = self.rito_client.champion_mastery.by_puuid(puuid=summoner.puuid)
        champion_mastery_totals = self.extractor_client.champion_mastery.extract_totals_from_list(
            champion_masteries_list=champion_masteries_list
        )
        try:
            champion_mastery = self.extractor_client.champion_mastery.extract_from_list(
                champion_masteries_list=champion_masteries_list, 
                champion_id=match_summoner.champion_id
            )
        except ExtractorError:
            champion_mastery = ChampionMastery(
                champion_id=match_summoner.champion_id,
                champion_points=0,
                champion_level=1
            )
        
        # Fill sample_summoner dict
        sample_summoner["match_summoner"] = match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"})
        sample_summoner["summoner"] = summoner.dict(exclude={"account_id"})
        sample_summoner["entries"] = [entry.dict(exclude={"league_id", "summoner_id", "summoner_name"}) for entry in entries]
        sample_summoner["champion_mastery"] = champion_mastery.dict(exclude={"summoner_id", "puuid"})
        sample_summoner["champion_mastery_totals"] = champion_mastery_totals.dict()
        sample_summoner["last_match"] = self._build_sample_last_match(
            match_id=match.match_id,
            puuid=summoner.puuid, 
            start_time_last_match=start_time_last_match
        )

        return sample_summoner

    def _build_sample_last_match(self, match_id: str, puuid: str, start_time_last_match: int) -> dict:
        match_ids = self.rito_client.match.list_by_puuid(
            puuid=puuid, 
            queue="420",
            start_time=start_time_last_match,
            count=100
        )

        try:
            idx = match_ids.index(match_id)
            last_match_id = match_ids[idx+1]
        except (ValueError, IndexError):
            last_match_id = None
        
        last_match_return = {}
        if last_match_id:
            last_match_dict = self.rito_client.match.by_match_id(match_id=last_match_id)
            last_match_timeline_dict = self.rito_client.match.timeline_by_match_id(match_id=last_match_id)

            last_match = self.extractor_client.match.extract(match_dict=last_match_dict)
            last_match_summoner = self.extractor_client.match.extract_summoner(match_dict=last_match_dict, puuid=puuid)
            last_match_opponent = self.extractor_client.match.extract_opponent(match_dict=last_match_dict, puuid=puuid)
            last_match_totals = self.extractor_client.match.extract_totals(match_dict=last_match_dict)
            last_match_timeline = self.extractor_client.match.extract_timeline(match_timeline_dict=last_match_timeline_dict)
            if last_match.game_duration > 900:
                timeline_15 = {}
                frame_idx_15 = last_match_timeline.frames[15]
                timeline_15_summoner = frame_idx_15.participant_frames[last_match_timeline.participants_ids_map[last_match_summoner.puuid]].dict(
                    exclude={"champion_stats", "participant_id", "position"}
                )
                timeline_15_opponent = frame_idx_15.participant_frames[last_match_timeline.participants_ids_map[last_match_opponent.puuid]].dict(
                    exclude={"champion_stats", "participant_id", "position"}
                )
                timeline_15["timestamp"] = frame_idx_15.timestamp
                timeline_15["summoner"] = timeline_15_summoner
                timeline_15["opponent"] = timeline_15_opponent
            else:
                timeline_15 = {}

            last_match_return["match"] = last_match.dict(exclude={"participants_puuid", "participants_id"})
            last_match_return["match_summoner"] = last_match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"})
            last_match_return["match_opponent"] = last_match_opponent.dict(exclude={"summoner_id", "puuid", "summoner_name"})
            last_match_return["match_totals"] = [last_match_total.dict() for last_match_total in last_match_totals]
            last_match_return["timeline_15"] = timeline_15
        
        return last_match_return
