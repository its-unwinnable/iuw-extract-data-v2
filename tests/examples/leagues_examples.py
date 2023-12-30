from rito.models import League, Entry


league_dict_example = {
    "tier": "EMERALD",
    "leagueId": "15b4ec05-bd78-4d4b-8da2-ff68bd37c493",
    "queue": "RANKED_SOLO_5x5",
    "name": "Miss Fortune's Villains",
    "entries": [
        {
            "summonerId": "pPE4MoR7CkND99L38MPw9V1-CWT-PeXZzCxHDtcCxK9mz0U",
            "summonerName": "Ulltimatum",
            "leaguePoints": 35,
            "rank": "I",
            "wins": 157,
            "losses": 134,
            "veteran": False,
            "inactive": False,
            "freshBlood": False,
            "hotStreak": False
        },
        {
            "summonerId": "_bq69Vh8mC1EEwjhdRCmgnrI6fUCzL6M58yqw6J-rs-upQS8",
            "summonerName": "Naturâss",
            "leaguePoints": 0,
            "rank": "IV",
            "wins": 55,
            "losses": 42,
            "veteran": False,
            "inactive": False,
            "freshBlood": False,
            "hotStreak": False
        }
    ]
}

league_example = League(
    tier='EMERALD', 
    league_id='15b4ec05-bd78-4d4b-8da2-ff68bd37c493', 
    queue='RANKED_SOLO_5x5', 
    name="Miss Fortune's Villains", 
    entries=[
        Entry(
            league_id='15b4ec05-bd78-4d4b-8da2-ff68bd37c493', 
            queue_type='RANKED_SOLO_5x5', 
            tier='EMERALD', 
            rank='I',
            summoner_id='pPE4MoR7CkND99L38MPw9V1-CWT-PeXZzCxHDtcCxK9mz0U',
            summoner_name='Ulltimatum',
            league_points=35, 
            wins=157, 
            losses=134, 
            veteran=False, 
            inactive=False, 
            fresh_blood=False, 
            hot_streak=False, 
            miniseries_progress=None, 
            total_lp=2335
        ), 
        Entry(
            league_id='15b4ec05-bd78-4d4b-8da2-ff68bd37c493', 
            queue_type='RANKED_SOLO_5x5', 
            tier='EMERALD', 
            rank='IV', 
            summoner_id='_bq69Vh8mC1EEwjhdRCmgnrI6fUCzL6M58yqw6J-rs-upQS8', 
            summoner_name='Naturâss', 
            league_points=0, 
            wins=55, 
            losses=42, 
            veteran=False, 
            inactive=False, 
            fresh_blood=False, 
            hot_streak=False, 
            miniseries_progress=None, 
            total_lp=2000
        )
    ]
)
