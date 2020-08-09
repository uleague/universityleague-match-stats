import os

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class SteamConfig:
    """
    Class for Steam config
    """

    STEAM_LOGIN = os.getenv("STEAM_LOGIN")
    STEAM_PASSWORD = os.getenv("STEAM_PASSWORD")


class Config:
    """
    Class for General config
    """

    PORT = os.getenv("PORT", 8080)
