from iuw_extract_data import helpers

from rito import RitoClient, ExtractorClient
from rito.models import League, Entry


class ExtractMatchIds:
    def __init__(self, rito_client: RitoClient, extractor_client: ExtractorClient, tier: str) -> None:
        self.rito_client = rito_client
        self.extractor_client = extractor_client
        self.tier = tier

        self._next_division = {"I": "II", "II": "III", "III": "IV", "IV": "I"}
        self._league_ids = {"unused": [], "used": []}
        self._summoner_ids = []
        self._match_ids = []
        self._current_division = "I"
        self._current_page = 1

    def next_match_id(self) -> str:
        while True:
            # if summoner_ids list is empty    
            while len(self._summoner_ids) == 0:
                league = self._next_league()
                for entry in league.entries:
                    if not entry.inactive:
                        self._summoner_ids.append(entry.summoner_id)

            # if summoner_ids list is not empty 
            summoner_id = self._summoner_ids.pop()
            summoner_dict = self.rito_client.summoner.by_id(summoner_id=summoner_id)
            summoner = self.extractor_client.summoner.extract(summoner_dict=summoner_dict)
            summoner_match_ids = self.rito_client.match.list_by_puuid(
                puuid=summoner.puuid, 
                queue="420", 
                start_time=helpers.get_timestamp_utc()-86400
            )
            if len(summoner_match_ids) > 0:
                if summoner_match_ids[0] not in self._match_ids:
                    self._match_ids.append(summoner_match_ids[0])
                    return summoner_match_ids[0]        

    def _next_league(self) -> League:
        if self.tier == "CHALLENGER":
            league_dict = self.rito_client.league.leagues.challenger_leagues_by_queue(queue="RANKED_SOLO_5x5")
        elif self.tier == "GRANDMASTER":
            league_dict = self.rito_client.league.leagues.grandmaster_leagues_by_queue(queue="RANKED_SOLO_5x5")
        elif self.tier == "MASTER":
            league_dict = self.rito_client.league.leagues.master_leagues_by_queue(queue="RANKED_SOLO_5x5")
        else:            
            league_id = self._next_league_id()
            league_dict = self.rito_client.league.leagues.by_league_id(league_id=league_id)        

        league = self.extractor_client.league.leagues.extract(league_dict=league_dict)
        return league

    def _next_league_id(self) -> str:
        # if league_ids["unused"] is empty
        while len(self._league_ids["unused"]) == 0:
            entries = self._new_entries(division=self._current_division, page=self._current_page)
            # if no entries, go to next page
            if len(entries) == 0:
                if self._current_division == "IV": # reset league_ids["used"] list
                    self._league_ids["used"] = []
                self._current_division = self._next_division[self._current_division]
                self._current_page = 1
                continue
            
            # if there is entries
            for entry in entries:
                if entry.league_id not in self._league_ids["used"]:
                    self._league_ids["unused"].append(entry.league_id)
            
            self._current_page += 1

        # if league_ids["unused"] is not empty 
        league_id = self._league_ids["unused"].pop()
        self._league_ids["used"].append(league_id)
        return league_id
        
    def _new_entries(self, division: str, page: int) -> list[Entry]:
        entries_list = self.rito_client.league.entries.by_rank(
            queue="RANKED_SOLO_5x5", 
            tier=self.tier, 
            division=division, 
            page=page
        )
        entries = self.extractor_client.league.entries.extract(entries_list=entries_list)   
        return entries     
