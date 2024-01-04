from rito.models import ChampionMastery, ChampionMasteryTotals


champion_masteries_list = [
    {
        "puuid": "5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA",
        "championId": 21,
        "championLevel": 7,
        "championPoints": 118490,
        "lastPlayTime": 1702846663000,
        "championPointsSinceLastLevel": 96890,
        "championPointsUntilNextLevel": 0,
        "chestGranted": False,
        "tokensEarned": 0,
        "summonerId": "wGLIUKGRoGd2faTzC2U2EX883DPJcGb9rxZMXmE5TdrtK4_X"
    },
    {
        "puuid": "5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA",
        "championId": 36,
        "championLevel": 3,
        "championPoints": 6893,
        "lastPlayTime": 1704274921000,
        "championPointsSinceLastLevel": 893,
        "championPointsUntilNextLevel": 5707,
        "chestGranted": True,
        "tokensEarned": 0,
        "summonerId": "wGLIUKGRoGd2faTzC2U2EX883DPJcGb9rxZMXmE5TdrtK4_X"
    }
]


champion_mastery = ChampionMastery(
    puuid='5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA', 
    champion_id='36', 
    champion_level=3, 
    champion_points=6893, 
    last_play_time=1704274921000, 
    champion_points_since_last_level=893, 
    champion_points_until_next_level=5707, 
    chest_granted=True, 
    tokens_earned=0, 
    summoner_id='wGLIUKGRoGd2faTzC2U2EX883DPJcGb9rxZMXmE5TdrtK4_X'
)


champion_mastery_totals = ChampionMasteryTotals(total_champion_level=10, total_champion_points=125383)
