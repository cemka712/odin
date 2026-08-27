import pygame

from src.config import settings
from src.entities.enemy import Enemy
from src.entities.enviroment import Environment
from src.entities.player import Player


class BaseScene:
    def handle_event(self, event): pass
    def update(self): pass
    def draw(self, screen): pass


class MenuScene(BaseScene):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Передаем размеры экрана в игровую сцену
            return GameScene()
        return None

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 200, 0), (120, 200, 400, 80))



class GameScene(BaseScene):
    def __init__(self):
        self.env = Environment()
        self.player = Player([1, 1], settings.TILE_WIDTH, settings.TILE_HEIGHT)
        self.enemy = Enemy([3, 5], settings.TILE_WIDTH, settings.TILE_HEIGHT)

    def handle_event(self, event):
        self.player.handle_event(event, self.enemy)

    def update(self):
        self.player.update_movement()
        self.enemy.update()

    def draw(self, screen):
        width = settings.SCREEN_WIDTH
        height = settings.SCREEN_HEIGHT
        cols = settings.COLS
        rows = settings.ROWS

        start_x = (width // 2) - (cols * settings.TILE_WIDTH // 2)
        start_y = (height // 2) - (rows * settings.TILE_HEIGHT // 2)
        start_pos = (start_x, start_y)

        self.env.draw(screen, start_pos)
        self.player.draw(screen, start_pos)
        self.enemy.draw(screen, start_pos)
