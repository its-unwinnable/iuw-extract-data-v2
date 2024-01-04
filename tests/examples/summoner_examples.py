from rito.models import Summoner


summoner_dict_example = {
    "id": "Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg",
    "accountId": "ZxKqFYLgPAadIPHYvNNOTMN6mWmUcKxwHTuM9g2crduqPg",
    "puuid": "5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA",
    "name": "Enno0815",
    "profileIconId": 503,
    "revisionDate": 1704274921373,
    "summonerLevel": 87
}

summoner_example = Summoner(
    summoner_id='Tr_eUweC_R276FidCsrUZW-P1rbvpASIr6axy8O6PBn3fbg', 
    account_id='ZxKqFYLgPAadIPHYvNNOTMN6mWmUcKxwHTuM9g2crduqPg', 
    puuid='5PxpwmAj85lpMrqF0JQDOEUGyECT-dY1IOxeOi0cBPvYXkyDZglM-B8PV8igMDq2KCfglujJ7OBnpA', 
    name='Enno0815', 
    profile_icon_id='503', 
    revision_date=1704274921373, 
    summoner_level=87
)
