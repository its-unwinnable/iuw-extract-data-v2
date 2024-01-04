from rito.models import Entry


entries_list_by_rank_example = [
    {
        "leagueId": "9898fbda-c883-4748-b704-6b9ba393e9e0",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "PLATINUM",
        "rank": "I",
        "summonerId": "MA2494I0gKIP_Cxq0sHqFg8QzlY-kcZmytp1aqHe0qkJFjm_",
        "summonerName": "Ellermann",
        "leaguePoints": 14,
        "wins": 96,
        "losses": 102,
        "veteran": False,
        "inactive": False,
        "freshBlood": False,
        "hotStreak": False
    },
    {
        "leagueId": "2064bc4b-8c6b-4f6c-803c-965954c07d54",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "PLATINUM",
        "rank": "I",
        "summonerId": "6gXXbiSIiZZUB7LtM1nLgHrFJsQcyhP8xyBYKRT51GJz6sSo",
        "summonerName": "karonalife",
        "leaguePoints": 81,
        "wins": 183,
        "losses": 188,
        "veteran": False,
        "inactive": False,
        "freshBlood": False,
        "hotStreak": True
    }
]


entries_by_rank_example = [
    Entry(
        league_id='9898fbda-c883-4748-b704-6b9ba393e9e0', 
        queue_type='RANKED_SOLO_5x5', 
        tier='PLATINUM', 
        rank='I', 
        summoner_id='MA2494I0gKIP_Cxq0sHqFg8QzlY-kcZmytp1aqHe0qkJFjm_', 
        summoner_name='Ellermann', 
        league_points=14, 
        wins=96, 
        losses=102, 
        veteran=False, 
        inactive=False, 
        fresh_blood=False, 
        hot_streak=False, 
        miniseries_progress=None,
        total_lp=1914
    ), 
    Entry(
        league_id='2064bc4b-8c6b-4f6c-803c-965954c07d54', 
        queue_type='RANKED_SOLO_5x5', 
        tier='PLATINUM', 
        rank='I', 
        summoner_id='6gXXbiSIiZZUB7LtM1nLgHrFJsQcyhP8xyBYKRT51GJz6sSo', 
        summoner_name='karonalife', 
        league_points=81, 
        wins=183, 
        losses=188, 
        veteran=False, 
        inactive=False, 
        fresh_blood=False, 
        hot_streak=True, 
        miniseries_progress=None, 
        total_lp=1981)
]


entries_list_by_summoner = [
    {
        "queueType": "CHERRY",
        "summonerId": "Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg",
        "summonerName": "Enno0815",
        "leaguePoints": 0,
        "wins": 4,
        "losses": 3,
        "veteran": False,
        "inactive": False,
        "freshBlood": False,
        "hotStreak": False
    },
    {
        "leagueId": "56410b29-158a-49be-8bf3-e64aa535124b",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "SILVER",
        "rank": "II",
        "summonerId": "Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg",
        "summonerName": "Enno0815",
        "leaguePoints": 0,
        "wins": 25,
        "losses": 39,
        "veteran": False,
        "inactive": False,
        "freshBlood": False,
        "hotStreak": False
    }
]


entries_by_summoner = [
    Entry(
        league_id=None, 
        queue_type='CHERRY', 
        tier=None, 
        rank=None, 
        summoner_id='Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg', 
        summoner_name='Enno0815', 
        league_points=0, 
        wins=4, 
        losses=3, 
        veteran=False, 
        inactive=False, 
        fresh_blood=False, 
        hot_streak=False, 
        miniseries_progress=None, 
        total_lp=None
    ), 
    Entry(
        league_id='56410b29-158a-49be-8bf3-e64aa535124b', 
        queue_type='RANKED_SOLO_5x5',
        tier='SILVER', 
        rank='II', 
        summoner_id='Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg', 
        summoner_name='Enno0815', 
        league_points=0, 
        wins=25, 
        losses=39, 
        veteran=False, 
        inactive=False, 
        fresh_blood=False, 
        hot_streak=False, 
        miniseries_progress=None, 
        total_lp=1000
    )
]
