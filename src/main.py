import sys

import pygame

# Импортируем классы из вашего нового файла
from src.scene import MenuScene

# SCREEN_WIDTH = 640
# SCREEN_HEIGHT = 480

from src.config import settings

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    active_scene = MenuScene()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        next_scene = active_scene.handle_event(event)

        if next_scene is not None:
            active_scene = next_scene

        active_scene.update()
        active_scene.draw(screen)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
