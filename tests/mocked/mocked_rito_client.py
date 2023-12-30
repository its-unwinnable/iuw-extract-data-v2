class TestEntries:
    def by_rank(self, queue: str, tier: str, division: str, page: int = 1):
        """entries by rank"""


class TestLeagues:
    def by_league_id(self, league_id: str):
        """league by league id"""

    def challenger_leagues_by_queue(self, queue):
        """challenger league"""

    def grandmaster_leagues_by_queue(self, queue):
        """grandmaster league"""

    def master_leagues_by_queue(self, queue):
        """master league"""


class TestSummonerAPI:
    def by_id(self, summoner_id: str):
        """summoner by summoner ID"""


class TestMatchAPI:
    def list_by_puuid(self, puuid, start_time = None, end_time = None, queue = None, type = None, start = None, count = 20):
        """list of match ID by summoner PUUID"""


class TestLeagueAPI:
    entries = TestEntries()
    leagues = TestLeagues()


class TestRitoClient:
    league = TestLeagueAPI()
    summoner = TestSummonerAPI()
    match = TestMatchAPI()
