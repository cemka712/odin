import pygame

from src.config import settings


class Environment:
    def __init__(self) -> None:
        self.map_data = settings.MAP
        self.wall_img = pygame.transform.scale(settings.IMAGE.WALL_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
        self.floor_img = pygame.transform.scale(settings.IMAGE.FLOOR_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

    def draw(self, screen: pygame.Surface, start_pos: tuple[int , int]) -> None:
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                x = start_pos[0] + col_idx * settings.TILE_WIDTH
                y = start_pos[1] + row_idx * settings.TILE_HEIGHT
                screen.blit(self.floor_img, (x, y))
                if tile == 1:
                    screen.blit(self.wall_img, (x, y))
