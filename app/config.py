import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    RIOT_API_KEY: str


@lru_cache()
def get_settings():
    ENV_FILE_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return Settings(_env_file=os.path.join(ENV_FILE_FOLDER, ".env"))
