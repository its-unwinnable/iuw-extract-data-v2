from tests.mocked.mocked_rito_client import TestRitoClient

from rito import ExtractorClient


class TestExtractMatchIds:
    rito_client = TestRitoClient()
    extractor_client = ExtractorClient()
    tier = "BRONZE"

    def next_match_id(self):
        """"""
