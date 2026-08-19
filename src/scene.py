import sys

import pygame

from src.classes import Enemy, Environment, Player
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
        pass
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
        #     self.player.attack(self.enemy)

    def update(self):
        pass
        # self.player.update_movement()
        # self.enemy.update() #[cite: 9]

    def draw(self, screen):
        self.env.draw(screen) #[cite: 9]
        # self.player.draw(screen) #[cite: 9]
        # self.enemy.draw(screen) #[cite: 9]


# # === Менеджер сцен и главный цикл ===
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480))
#     pygame.display.set_caption("Scene Manager Test")
#     clock = pygame.time.Clock()

#     # Устанавливаем начальную сцену
#     active_scene = MenuScene()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             next_scene = active_scene.handle_event(event)
#             if next_scene is not None:
#                 active_scene = next_scene

#         active_scene.update()
#         active_scene.draw(screen)

#         pygame.display.flip()
#         clock.tick(60)

# if __name__ == "__main__":
#     main()
