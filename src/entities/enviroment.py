import pygame

from src.config import settings


class Environment:
    def __init__(self):
        self.map_data = settings.MAP
        self.wall_img = pygame.transform.scale(settings.IMAGE.WALL_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
        self.floor_img = pygame.transform.scale(settings.IMAGE.FLOOR_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

    def draw(self, screen):
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                x = col_idx * settings.TILE_WIDTH
                y = row_idx * settings.TILE_HEIGHT

                screen.blit(self.floor_img, (x, y))

                if tile == 1:
                    screen.blit(self.wall_img, (x, y))