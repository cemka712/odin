import os
import sys

os.environ["DISPLAY"] = ":0"
os.environ["SDL_VIDEODRIVER"] = "x11"

import pygame

from src.config import settings
from src.scene import MenuScene


def main():
    pygame.init()
    print('Начал выполнение')
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    active_scene = MenuScene()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode(
                    (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
                    pygame.RESIZABLE
                )

            next_scene = active_scene.handle_event(event)

            if next_scene is not None:
                active_scene = next_scene

        print('Начал выполнение')
        active_scene.update()
        active_scene.draw(screen)
        pygame.display.flip()
        clock.tick(15)


if __name__ == "__main__":
    main()
