from iuw_extract_data import extract_match_ids
from tests.mocked.mocked_rito_client import TestRitoClient
from tests.examples import leagues_examples

from rito import ExtractorClient


def test_extractmatchids_next_league_CLASSIC_TIER(mocker):
    # Mocks
    mocker.patch(
        "iuw_extract_data.extract_match_ids.ExtractMatchIds._next_league_id", 
        return_value="15b4ec05-bd78-4d4b-8da2-ff68bd37c493"
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestLeagues.by_league_id", 
        return_value=leagues_examples.league_dict_example
    )
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="EMERALD"
    )
    league = extractor_match_ids._next_league()

    # Verifs
    assert league == leagues_examples.league_example


def test_extractmatchids_next_league_CHALLENGER(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestLeagues.challenger_leagues_by_queue", 
        return_value=leagues_examples.league_dict_example
    )
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="CHALLENGER"
    )
    league = extractor_match_ids._next_league()

    # Verifs
    assert league == leagues_examples.league_example


def test_extractmatchids_next_league_GRANDMASTER(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestLeagues.grandmaster_leagues_by_queue", 
        return_value=leagues_examples.league_dict_example
    )
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="GRANDMASTER"
    )
    league = extractor_match_ids._next_league()

    # Verifs
    assert league == leagues_examples.league_example


def test_extractmatchids_next_league_MASTER(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestLeagues.master_leagues_by_queue", 
        return_value=leagues_examples.league_dict_example
    )
    
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="MASTER"
    )
    league = extractor_match_ids._next_league()

    # Verifs
    assert league == leagues_examples.league_example
