from app import extract_match_ids
from tests.mocked.mocked_rito_client import TestRitoClient
from tests.examples import entries_examples

from rito import ExtractorClient


def test_extractmatchids_new_entries(mocker):
    # Mocks
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestEntries.by_rank", 
        return_value=entries_examples.entries_list_example
    )

    # Calls
    extractor_match_ids = extract_match_ids.ExtractMatchIds(
        rito_client=TestRitoClient(), 
        extractor_client=ExtractorClient(), 
        tier="tier"
    )
    entries = extractor_match_ids._new_entries(division="I", page=3)

    # Verifs
    assert entries == entries_examples.entries_example
    extractor_match_ids.rito_client.league.entries.by_rank.assert_called_once_with(
        queue="RANKED_SOLO_5x5", 
        tier="tier", 
        division="I", 
        page=3
    )
