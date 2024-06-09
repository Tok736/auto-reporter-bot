import json

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class BotSettings(BaseModel):
    token: str

class Settings(BaseSettings):
    bot: BotSettings

def load_config(file_path: str) -> Settings:
    with open(file_path, "r") as f:
        settings_data = json.load(f)
    return Settings.model_validate(settings_data)

settings = load_config("config.json")



