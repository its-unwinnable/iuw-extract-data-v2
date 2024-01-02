from iuw_extract_data import ExtractData
from tests.mocked.mocker_extract_match_ids import TestExtractMatchIds
from tests.examples import match_examples, match_timeline_examples


def test_extractdata_build_sample_last_match_NO_LAST_MATCH_ID(mocker):
    # Mocks
    mocker.patch("tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", return_value=[])

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_last_match = extractor_data._build_sample_last_match(
        match_id="match_id1", 
        puuid="puuid1", 
        start_time_last_match=10
    )

    # Verifs
    assert sample_last_match == {}


def test_extractdata_build_sample_last_match_NO_LAST_MATCH_ID_IDX(mocker):
    # Mocks
    mocker.patch("tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", return_value=["match_id1"])

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_last_match = extractor_data._build_sample_last_match(
        match_id="match_id1", 
        puuid="puuid1", 
        start_time_last_match=10
    )

    # Verifs
    assert sample_last_match == {}


def test_extractdata_build_sample_last_match_GAME_DURATION_OVER_900(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", 
        return_value=["match_id1", "EUW_6743454141"]
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.by_match_id", 
        return_value=match_examples.match_dict_example
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.timeline_by_match_id", 
        return_value=match_timeline_examples.match_timeline_dict_example
    )

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_last_match = extractor_data._build_sample_last_match(
        match_id="match_id1", 
        puuid="5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA", 
        start_time_last_match=10
    )

    # Verifs
    assert sample_last_match == {
        "match": match_examples.match_example.dict(exclude={"participants_puuid", "participants_id"}),
        "match_summoner": match_examples.match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "match_opponent": match_examples.match_opponent.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "match_totals": [mt.dict() for mt in match_examples.match_totals],
        "timeline_15": {
            "summoner": match_timeline_examples.match_timeline_15_example.participant_frames["1"].dict(
                exclude={"champion_stats", "participant_id", "position"}
            ),
            "opponent": match_timeline_examples.match_timeline_15_example.participant_frames["6"].dict(
                exclude={"champion_stats", "participant_id", "position"}
            ),
            "timestamp": 900281
        }
    }


def test_extractdata_build_sample_last_match_GAME_DURATION_BELOW_900(mocker):
    # Mocks
    match_dict_low_duration = match_examples.match_dict_example
    match_dict_low_duration["info"]["gameDuration"] = 300
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.list_by_puuid", 
        return_value=["match_id1", "EUW_6743454141"]
    )
    mocker.patch("tests.mocked.mocked_rito_client.TestMatchAPI.by_match_id", return_value=match_dict_low_duration)
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.timeline_by_match_id", 
        return_value=match_timeline_examples.match_timeline_dict_example
    )

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample_last_match = extractor_data._build_sample_last_match(
        match_id="match_id1", 
        puuid="5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA", 
        start_time_last_match=10
    )

    # Verifs
    match_low_duration = match_examples.match_example.dict(exclude={"participants_puuid", "participants_id"})
    match_low_duration["game_duration"] = 300
    assert sample_last_match == {
        "match": match_low_duration,
        "match_summoner": match_examples.match_summoner.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "match_opponent": match_examples.match_opponent.dict(exclude={"summoner_id", "puuid", "summoner_name"}),
        "match_totals": [mt.dict() for mt in match_examples.match_totals],
        "timeline_15": {}
    }
