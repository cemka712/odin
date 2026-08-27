import json
from pprint import pprint

from pydantic import computed_field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pygame import image, Surface


class ImageSettings(BaseSettings):
    model_config = SettingsConfigDict(
            extra='ignore',
        env_file='.env'
    )

    STATIC_DIR: str

    WALL_IMG: Surface | None = None
    PLAYER_IMG: Surface | None = None
    FLOOR_IMG: Surface | None = None
    ENEMY_IMG: Surface | None = None

    def __deepcopy__(self, memo):
        return self

    @model_validator(mode="after")
    def all_img(self):
        self.WALL_IMG = image.load(self.STATIC_DIR+'Стена.bmp')
        self.PLAYER_IMG = image.load(self.STATIC_DIR+'edward.bmp')
        self.FLOOR_IMG = image.load(self.STATIC_DIR+'доска.bmp')
        self.ENEMY_IMG = image.load(self.STATIC_DIR+'horror.bmp')

        return self



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )

    SCREEN_WIDTH: int
    SCREEN_HEIGHT: int
    COLS: int | None = None
    ROWS: int | None = None
    TILE_HEIGHT: int | None = None
    TILE_WIDTH: int | None = None
    MAP: list | None = None

    IMAGE: ImageSettings = ImageSettings()


    @model_validator(mode="after")
    def create_map(self):
        with open("map.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        self.MAP = data
        self.ROWS = len(self.MAP)
        self.COLS = len(self.MAP[0])

        self.TILE_HEIGHT = self.SCREEN_HEIGHT // self.ROWS
        self.TILE_WIDTH = self.SCREEN_WIDTH // self.COLS

        return self


settings = Settings()

APP_VERSION = '0.0.1'
