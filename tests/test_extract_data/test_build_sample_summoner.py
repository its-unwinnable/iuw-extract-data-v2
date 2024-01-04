from iuw_extract_data import ExtractData
from tests.mocked.mocked_extract_match_ids import TestExtractMatchIds
from tests.examples import summoner_examples, entries_examples, champion_masteries_examples, match_examples


def test_extractdata_build_sample_summoner(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestSummonerAPI.by_id", 
        return_value=summoner_examples.summoner_dict_example
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestEntries.by_summoner",
        return_value=entries_examples.entries_list_by_summoner
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestChampionMasteryAPI.by_puuid",
        return_value=champion_masteries_examples.champion_masteries_list
    )
    mocker.patch("iuw_extract_data.extract_data.ExtractData._build_sample_last_match", return_value={})

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_summoner =  extractor_data._build_sample_summoner(
        match_dict=match_examples.match_dict_example, 
        summoner_id="Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg",
        start_time_last_match=10
    )

    # Verifs
    assert sample_summoner == {
        "match_summoner": match_examples.match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "summoner": summoner_examples.summoner_example.dict(exclude={"account_id"}),
        "entries": [entry.dict(exclude={"league_id", "summoner_id", "summoner_name"}) for entry in entries_examples.entries_by_summoner],
        "champion_mastery": champion_masteries_examples.champion_mastery.dict(exclude={"summoner_id", "puuid"}),
        "champion_mastery_totals": champion_masteries_examples.champion_mastery_totals.dict(),
        "last_match": {}
    }


def test_extractdata_build_sample_summoner_NO_CHAMPION_MASTERY(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestSummonerAPI.by_id", 
        return_value=summoner_examples.summoner_dict_example
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestEntries.by_summoner",
        return_value=entries_examples.entries_list_by_summoner
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestChampionMasteryAPI.by_puuid",
        return_value=[champion_masteries_examples.champion_masteries_list[0]]
    )
    mocker.patch("iuw_extract_data.extract_data.ExtractData._build_sample_last_match", return_value={})

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_summoner =  extractor_data._build_sample_summoner(
        match_dict=match_examples.match_dict_example, 
        summoner_id="Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg",
        start_time_last_match=10
    )

    # Verifs
    assert sample_summoner == {
        "match_summoner": match_examples.match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "summoner": summoner_examples.summoner_example.dict(exclude={"account_id"}),
        "entries": [entry.dict(exclude={"league_id", "summoner_id", "summoner_name"}) for entry in entries_examples.entries_by_summoner],
        "champion_mastery": {
            'champion_id': '36', 
            'champion_level': 1, 
            'champion_points': 0, 
            'last_play_time': None, 
            'champion_points_since_last_level': None, 
            'champion_points_until_next_level': None, 
            'chest_granted': None, 
            'tokens_earned': None
         },
        "champion_mastery_totals": {'total_champion_level': 7, 'total_champion_points': 118490},
        "last_match": {}
    }
