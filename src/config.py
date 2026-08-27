import json
from typing import Any

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pygame import Surface, image


class ImageSettings(BaseSettings):
    model_config = SettingsConfigDict(
            extra='ignore',
        env_file='.env'
    )

    STATIC_DIR: str = 'chobi_ne_bilo_pohmeliya'

    WALL_IMG: Surface  = Surface(size=(1,1))
    PLAYER_IMG: Surface = Surface(size=(1,1))
    FLOOR_IMG: Surface  = Surface(size=(1,1))
    ENEMY_IMG: Surface  = Surface(size=(1,1))

    def __deepcopy__(self, memo: dict[int, Any] | None = None) -> Any:
        if memo is None:
            memo = {}
        return self

    @model_validator(mode="after")
    def all_img(self) -> Any:
        self.WALL_IMG = image.load(self.STATIC_DIR+'Стена.bmp')
        self.PLAYER_IMG = image.load(self.STATIC_DIR+'edward.png')
        self.FLOOR_IMG = image.load(self.STATIC_DIR+'доска.bmp')
        self.ENEMY_IMG = image.load(self.STATIC_DIR+'horror.png')

        return self



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )

    SCREEN_WIDTH: int = 123
    SCREEN_HEIGHT: int = 123
    COLS: int = 0
    ROWS: int = 0
    TILE_HEIGHT: int = 8
    TILE_WIDTH: int = 8
    MAP: list[list[int]] = []

    IMAGE: ImageSettings = ImageSettings()


    @model_validator(mode="after")
    def create_map(self) -> Any:
        with open("map.json", encoding="utf-8") as file:
            data = json.load(file)
        self.MAP = data
        self.ROWS = len(self.MAP)
        self.COLS = len(self.MAP[0])

        self.TILE_HEIGHT = self.SCREEN_HEIGHT // self.ROWS
        self.TILE_WIDTH = self.TILE_HEIGHT

        self.SCREEN_WIDTH = self.TILE_HEIGHT * self.COLS

        # self.TILE_WIDTH = self.SCREEN_WIDTH // self.COLS

        return self


settings = Settings()
