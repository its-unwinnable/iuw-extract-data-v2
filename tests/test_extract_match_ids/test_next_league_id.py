from iuw_extract_data import extract_match_ids
from tests.mocked.mocked_rito_client import TestRitoClient
from tests.examples import entries_examples

from rito import ExtractorClient


def test_extractmatchids_next_league_id_UNUSED_NOT_EMPTY():
    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._league_ids["unused"] = ["league1"]

    # Verifs
    assert extractor_match_ids._next_league_id() == "league1"
    assert extractor_match_ids._league_ids["unused"] == []
    assert extractor_match_ids._league_ids["used"] == ["league1"]


def test_extractmatchids_next_league_id_UNUSED_EMPTY(mocker):
    # Mocks
    mocker.patch("iuw_extract_data.extract_match_ids.ExtractMatchIds._new_entries", return_value=entries_examples.entries_example)

    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._league_ids["used"] = ["league1"]
    league_id = extractor_match_ids._next_league_id()

    # Verifs
    assert league_id == "2064bc4b-8c6b-4f6c-803c-965954c07d54"
    assert extractor_match_ids._league_ids["unused"] == ["9898fbda-c883-4748-b704-6b9ba393e9e0"]
    assert extractor_match_ids._league_ids["used"] == ["league1", "2064bc4b-8c6b-4f6c-803c-965954c07d54"]
    assert extractor_match_ids._current_division == "I"
    assert extractor_match_ids._current_page == 2


def test_extractmatchids_next_league_id_UNUSED_EMPTY_ENTRIES_EMPTY(mocker):
    # Mocks
    test_entries = [entries_examples.entries_example, []]

    mocker.patch(
        "iuw_extract_data.extract_match_ids.ExtractMatchIds._new_entries", 
        side_effect=lambda division, page: test_entries.pop()
    )

    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._league_ids["used"] = ["league1"]
    league_id = extractor_match_ids._next_league_id()

    # Verifs
    assert league_id == "2064bc4b-8c6b-4f6c-803c-965954c07d54"
    assert extractor_match_ids._league_ids["unused"] == ["9898fbda-c883-4748-b704-6b9ba393e9e0"]
    assert extractor_match_ids._league_ids["used"] == ["league1", "2064bc4b-8c6b-4f6c-803c-965954c07d54"]
    assert extractor_match_ids._current_division == "II"
    assert extractor_match_ids._current_page == 2


def test_extractmatchids_next_league_id_UNUSED_EMPTY_ENTRIES_EMPTY_LAST_DIVISION(mocker):
    # Mocks
    test_entries = [entries_examples.entries_example, []]

    mocker.patch(
        "iuw_extract_data.extract_match_ids.ExtractMatchIds._new_entries", 
        side_effect=lambda division, page: test_entries.pop()
    )

    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    extractor_match_ids._league_ids["used"] = ["league1"]
    extractor_match_ids._current_division = "IV"
    league_id = extractor_match_ids._next_league_id()

    # Verifs
    assert league_id == "2064bc4b-8c6b-4f6c-803c-965954c07d54"
    assert extractor_match_ids._league_ids["unused"] == ["9898fbda-c883-4748-b704-6b9ba393e9e0"]
    assert extractor_match_ids._league_ids["used"] == ["2064bc4b-8c6b-4f6c-803c-965954c07d54"]
    assert extractor_match_ids._current_division == "I"
    assert extractor_match_ids._current_page == 2
