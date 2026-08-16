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
import pygame
import os

# 1. Получаем путь к папке src (там, где лежит этот файл classes.py)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 2. Поднимаемся на уровень выше в главную папку проекта
ROOT_DIR = os.path.dirname(CURRENT_DIR)
# 3. Указываем точный путь к папке static
STATIC_DIR = os.path.join(ROOT_DIR, 'static')

class Environment:
    def __init__(self, map_data, screen_width, screen_height):
        self.map_data = map_data
        self.rows = len(map_data)
        self.cols = len(map_data[0]) if self.rows > 0 else 0
        
        self.tile_w = screen_width // self.cols
        self.tile_h = screen_height // self.rows
        
        # Используем STATIC_DIR вместо просто 'static'
        wall_img = pygame.image.load(os.path.join(STATIC_DIR, 'Стена.bmp'))
        self.wall_img = pygame.transform.scale(wall_img, (self.tile_w, self.tile_h))
        
        floor_img = pygame.image.load(os.path.join(STATIC_DIR, 'доска.bmp'))
        self.floor_img = pygame.transform.scale(floor_img, (self.tile_w, self.tile_h))

    def draw(self, screen):
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                x = col_idx * self.tile_w
                y = row_idx * self.tile_h
                
                screen.blit(self.floor_img, (x, y))
                
                if tile == 1:
                    screen.blit(self.wall_img, (x, y))
class Player:
    def __init__(self, start_pos, tile_w, tile_h):
        self.pos = list(start_pos)
        self.tile_w = tile_w
        self.tile_h = tile_h
        
        image = pygame.image.load(os.path.join(STATIC_DIR, 'edward.bmp'))
        self.image = pygame.transform.scale(image, (self.tile_w, self.tile_h))

    def get_movement(self, event):
        """Отлавливает нажатия и возвращает желаемое направление (сдвиг по Y, X)"""
        dy, dx = 0, 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
        return dy, dx

    def draw(self, screen):
        # Переводим координаты массива в координаты экрана
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
        
        image = pygame.image.load(os.path.join(STATIC_DIR, 'horror.bmp')) #[cite: 3]
        self.image = pygame.transform.scale(image, (self.tile_w, self.tile_h)) #[cite: 3]
        
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