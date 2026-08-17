# 1. Игрок
# инициализация
# Функции которые отлавливают нажатия на кнопки
# Его отрисовка
# Механика толкания врагов

# 2. Враг
# инициализация
# Мини ИИ
# Его отрисовка

# 3. Окружение
# инициализация
# отрисовка
import os

import pygame

from src.config import settings

# # 1. Получаем путь к папке src (там, где лежит этот файл classes.py)
# CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# # 2. Поднимаемся на уровень выше в главную папку проекта
# ROOT_DIR = os.path.dirname(CURRENT_DIR)
# # 3. Указываем точный путь к папке static
# STATIC_DIR = os.path.join(ROOT_DIR, 'static')

class Environment:
    def __init__(self):
        self.map_data = settings.MAP
        # self.rows = len(map_data)
        # self.cols = len(map_data[0]) if self.rows > 0 else 0

        # self.tile_w = screen_width // self.cols
        # self.tile_h = screen_height // self.rows

        # Используем STATIC_DIR вместо просто 'static'
        # wall_img = pygame.image.load(os.path.join(STATIC_DIR, 'Стена.bmp'))
        self.wall_img = pygame.transform.scale(settings.IMAGE.WALL_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

        # floor_img = pygame.image.load(os.path.join(STATIC_DIR, 'доска.bmp'))
        self.floor_img = pygame.transform.scale(settings.IMAGE.FLOOR_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

    def draw(self, screen):
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                x = col_idx * settings.TILE_WIDTH
                y = row_idx * settings.TILE_HEIGHT

                screen.blit(self.floor_img, (x, y))

                if tile == 1:
                    screen.blit(self.wall_img, (x, y))


class Player:
    def __init__(self, start_pos, tile_w, tile_h):
        self.pos = list(start_pos)
        self.tile_w = tile_w
        self.tile_h = tile_h

        self.image = pygame.transform.scale(settings.IMAGE.PLAYER_IMG, (self.tile_w, self.tile_h))

    def get_movement(self):
        dy, dx = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        return dy, dx

    def draw(self, screen):
        print(self.pos[1], self.pos[0], self.tile_w, self.tile_h)
        print(settings.TILE_HEIGHT, settings.TILE_WIDTH)
        x = self.pos[1] * self.tile_w
        y = self.pos[0] * self.tile_h
        screen.blit(self.image, (x, y))

    def push_enemy(self):
        pass

class Enemy:
    def __init__(self, start_pos, tile_w, tile_h):
        self.pos = list(start_pos) #[cite: 3]
        self.tile_w = tile_w #[cite: 3]
        self.tile_h = tile_h #[cite: 3]

        # image = pygame.image.load(os.path.join(STATIC_DIR, 'horror.bmp')) #[cite: 3]
        self.image = pygame.transform.scale(settings.IMAGE.ENEMY_IMG, (self.tile_w, self.tile_h)) #[cite: 3]

        # --- НОВЫЕ ПЕРЕМЕННЫЕ ДЛЯ БОЯ ---
        self.hp = 3                  # Враг умрет после 3 нажатий
        self.is_dead = False         # Жив ли враг
        self.hit_effect_timer = 0    # Таймер эффекта получения урона

    def update(self):
        # Уменьшаем таймер эффекта каждый кадр
        if self.hit_effect_timer > 0:
            self.hit_effect_timer -= 1
        pass #[cite: 3]

    def draw(self, screen):
        # Если враг мертв, выходим из функции и не рисуем его
        if self.is_dead:
            return

        x = self.pos[1] * self.tile_w #[cite: 3]
        y = self.pos[0] * self.tile_h #[cite: 3]

        # --- ВИЗУАЛЬНЫЙ ЭФФЕКТ: Тряска и покраснение ---
        if self.hit_effect_timer > 0:
            x += 5  # Эффект тряски (небольшой сдвиг по оси X)
            # Рисуем красный квадрат поверх врага как вспышку урона/крови
            pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tile_w, self.tile_h))
        else:
            screen.blit(self.image, (x, y)) #[cite: 3]
