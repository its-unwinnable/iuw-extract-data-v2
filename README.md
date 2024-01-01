# Extract Data v2

Extract samples thanks to the Riot API to train models.

## Installation
````bash
pip install git+ssh://git@github.com/its-unwinnable/extract-data-v2.git
````

## Example
```python
from iuw_extract_data.config import get_settings
from iuw_extract_data import ExtractData, ExtractMatchIds

from rito import ExtractorClient, RitoClient


settings = config.get_settings()

rito_client = RitoClient(riot_api_key="riot_api_key", region="EUW")
extractor_client = ExtractorClient()

extractor_match_ids = ExtractMatchIds(rito_client=rito_client, extractor_client=extractor_client, tier="BRONZE")
extractor_data = ExtractData(extractor_match_ids=extractor_match_ids)

print(extractor_data.extract_samples(n=2))
```
