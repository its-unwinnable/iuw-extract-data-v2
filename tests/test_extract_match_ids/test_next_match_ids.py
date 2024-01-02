from iuw_extract_data import extract_match_ids
from tests.mocked.mocked_rito_client import TestRitoClient
from tests.examples import summoner_examples, leagues_examples

from unittest.mock import call

from rito import ExtractorClient


def test_extractmatchids_next_match_id_SUMMONER_IDS_NOT_EMPTY(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestSummonerAPI.by_id", 
        return_value=summoner_examples.summoner_dict_example
    )
    mocker.patch("tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", return_value=["match_id1", "match_id2"])
    mocker.patch("iuw_extract_data.helpers.get_timestamp_utc", return_value=186400)
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._summoner_ids = ["summoner_id1"]
    match_id = extractor_match_ids.next_match_id()

    # Verifs
    assert match_id == "match_id1"
    assert extractor_match_ids._match_ids == ["match_id1"]
    extractor_match_ids.rito_client.summoner.by_id.assert_called_once_with(summoner_id="summoner_id1")
    extractor_match_ids.rito_client.match.list_by_puuid.assert_called_once_with(
        puuid='eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g',
        queue='420',
        start_time=100000
    )


def test_extractmatchids_next_match_id_SUMMONER_IDS_NOT_EMPTY_MATCH_IDS_EMPTY(mocker):
    # Mocks
    test_list_match_ids = [["match_id1", "match_id2"], []]
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestSummonerAPI.by_id", 
        return_value=summoner_examples.summoner_dict_example
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", 
        side_effect=lambda puuid, queue, start_time: test_list_match_ids.pop()
    )
    mocker.patch("iuw_extract_data.helpers.get_timestamp_utc", return_value=186400)
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._summoner_ids = ["summoner_id2", "summoner_id1"]
    match_id = extractor_match_ids.next_match_id()

    # Verifs
    assert match_id == "match_id1"
    assert extractor_match_ids._match_ids == ["match_id1"]
    extractor_match_ids.rito_client.summoner.by_id.assert_has_calls(
        [
            call(summoner_id="summoner_id1"), 
            call(summoner_id="summoner_id2")
        ]
    )
    extractor_match_ids.rito_client.match.list_by_puuid.assert_has_calls(
        [
            call(
                puuid='eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g', 
                queue='420', 
                start_time=100000
            ),
            call(
                puuid='eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g', 
                queue='420', 
                start_time=100000
            )
        ]
    )


def test_extractmatchids_next_match_id_SUMMONER_IDS_EMPTY(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestSummonerAPI.by_id", 
        return_value=summoner_examples.summoner_dict_example
    )
    mocker.patch("tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", return_value=["match_id1", "match_id2"])
    mocker.patch(
        "iuw_extract_data.extract_match_ids.ExtractMatchIds._next_league", 
        return_value=leagues_examples.league_example
    )
    mocker.patch("iuw_extract_data.helpers.get_timestamp_utc", return_value=186400)
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    match_id = extractor_match_ids.next_match_id()

    # Verifs
    assert match_id == "match_id1"
    assert extractor_match_ids._summoner_ids == ["pPE4MoR7CkND99L38MPw9V1-CWT-PeXZzCxHDtcCxK9mz0U"]
    assert extractor_match_ids._match_ids == ["match_id1"]
    extractor_match_ids.rito_client.summoner.by_id.assert_called_once_with(
        summoner_id="_bq69Vh8mC1EEwjhdRCmgnrI6fUCzL6M58yqw6J-rs-upQS8"
    )
    extractor_match_ids.rito_client.match.list_by_puuid.assert_called_once_with(
        puuid='eZZVkO20LI7XCkfeqBn8X0eae2lNJFxgzlnq3QvjzRTQ-FI2oeBq-mfYGElhsUKgndHdGccJ9zuA0g',
        queue='420',
        start_time=100000
    )
