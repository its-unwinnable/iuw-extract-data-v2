# Extract Data v2

Extract samples to train models 

## Installation
````bash
pip install git+ssh://git@github.com/its-unwinnable/extract-data-v2.git
````

## Exemple
```python
from iuw_extract_data.config import get_settings
from iuw_extract_data.extract_data import ExtractData
from iuw_extract_data.extract_match_ids import ExtractMatchIds

from rito import ExtractorClient, RitoClient


settings = config.get_settings()

rito_client = RitoClient(riot_api_key=settings.RIOT_API_KEY, region="EUW")
extractor_client = ExtractorClient()

extractor_match_ids = ExtractMatchIds(rito_client=rito_client, extractor_client=extractor_client, tier="BRONZE")
extractor_data = ExtractData(extractor_match_ids=extractor_match_ids)

print(extractor_data.extract_samples(n=2))

```