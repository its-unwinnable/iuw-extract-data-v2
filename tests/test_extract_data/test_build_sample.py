from iuw_extract_data import ExtractData
from tests.mocked.mocked_extract_match_ids import TestExtractMatchIds
from tests.examples import match_examples


def test_extractdata_build_sample(mocker):
    # Mocks
    mocker.patch("iuw_extract_data.helpers.get_timestamp_utc", return_value = 1_000_000)
    mocker.patch("iuw_extract_data.extract_data.ExtractData._build_sample_summoner", return_value = {"lol": "xd"})

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    sample = extractor_data._build_sample(match_dict=match_examples.match_dict_example)

    # Verifs
    assert sample == {
        "match": match_examples.match_example.dict(exclude={"participants_puuid", "participants_id"}),
        "match_totals": [mt.dict() for mt in match_examples.match_totals],
        "summoners": [
            {"lol": "xd"}, 
            {"lol": "xd"}, 
            {"lol": "xd"}, 
            {"lol": "xd"}, 
            {"lol": "xd"}, 
            {"lol": "xd"}, 
            {"lol": "xd"},
            {"lol": "xd"},
            {"lol": "xd"},
            {"lol": "xd"}
        ]
    }
