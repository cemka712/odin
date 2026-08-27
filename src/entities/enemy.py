import pygame

from src.config import settings


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

    def draw(self, screen, start_pos):
        # Если враг мертв, выходим из функции и не рисуем его
        if self.is_dead:
            return

        x = start_pos[0] + self.pos[1] * self.tile_w
        y = start_pos[1] + self.pos[0] * self.tile_h
        if self.hit_effect_timer > 0:
            x += 5  # Эффект тряски (небольшой сдвиг по оси X)
            # Рисуем красный квадрат поверх врага как вспышку урона/крови
            pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tile_w, self.tile_h))
        else:
            screen.blit(self.image, (x, y))
