from rito.models import Entry


entries_list_example = [
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

entries_example = [
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