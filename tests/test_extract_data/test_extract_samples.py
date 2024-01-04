from iuw_extract_data import ExtractData
from tests.mocked.mocked_extract_match_ids import TestExtractMatchIds
from tests.examples import match_examples


def test_extractdata_extract_sample(mocker):
    # Mocks
    mocker.patch("iuw_extract_data.extract_data.ExtractData._build_sample", return_value={"oui": "lol"})
    mocker.patch(
        "tests.mocked.mocked_extract_match_ids.TestExtractMatchIds.next_match_id", 
        return_value="EUW1_6743454141"
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.by_match_id", 
        return_value=match_examples.match_dict_example
    )

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    samples = extractor_data.extract_samples(n=2)

    # Verifs
    assert samples == [{"oui": "lol"}, {"oui": "lol"}]


def test_extractdata_extract_sample_ERROR(mocker):
    # Mocks
    test_match_ids = ["EUW1_6743454141", "match_id_error", "EUW1_6743454141"]
    def side_effect_match_by_match_id(match_id: str):
        if match_id == "match_id_error":
            raise ValueError("wrong id")
        return match_examples.match_dict_example

    mocker.patch(
        "tests.mocked.mocked_extract_match_ids.TestExtractMatchIds.next_match_id", 
        side_effect=lambda: test_match_ids.pop()
    )
    mocker.patch(
        "tests.mocked.mocked_rito_client.TestMatchAPI.by_match_id", 
        side_effect=side_effect_match_by_match_id
    )
    mocker.patch("iuw_extract_data.extract_data.ExtractData._build_sample", return_value={"oui": "lol"})

    # Calls
    extractor_data = ExtractData(TestExtractMatchIds())
    samples = extractor_data.extract_samples(n=2)

    # Verifs
    assert samples == [{"oui": "lol"}, {"oui": "lol"}]
