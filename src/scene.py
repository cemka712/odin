import sys

import pygame

from src.entities.enemy import Enemy
from src.entities.enviroment import Environment
from src.entities.player import Player
from src.config import settings


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
        self.env.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)