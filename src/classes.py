import pygame

from src.config import settings


class Environment:
    def __init__(self):
        self.map_data = settings.MAP
        self.wall_img = pygame.transform.scale(settings.IMAGE.WALL_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))
        self.floor_img = pygame.transform.scale(settings.IMAGE.FLOOR_IMG, (settings.TILE_WIDTH, settings.TILE_HEIGHT))

    def draw(self, screen: pygame.Surface):
        width = settings.SCREEN_WIDTH
        height = settings.SCREEN_HEIGHT
        cols = settings.COLS
        rows = settings.ROWS

        # Рисуем центральную точку для проверки
        pygame.draw.circle(screen, (0, 255, 0), (width // 2, height // 2), 3)

        # Вычисляем стартовую (верхнюю левую) координату сетки так,
        # чтобы центр карты совпал с центром экрана
        start_x = (width // 2) - (cols * settings.TILE_WIDTH // 2)
        start_y = (height // 2) - (rows * settings.TILE_HEIGHT // 2)

        # Один цикл для обхода ВСЕЙ карты без срезов
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                # Координата текущей плитки рассчитывается от стартовой точки
                x = start_x + col_idx * settings.TILE_WIDTH
                y = start_y + row_idx * settings.TILE_HEIGHT

                # Отрисовка
                screen.blit(self.floor_img, (x, y))
                if tile == 1:
                    screen.blit(self.wall_img, (x, y))


        # for row_idx, row in enumerate(self.map_data):
        #     for col_idx, tile in enumerate(row):
                # x = col_idx * settings.TILE_WIDTH + s_x
                # y = row_idx * settings.TILE_HEIGHT + s_y

                # screen.blit(self.floor_img, (x, y))
                # if col_idx == l_x and row_idx == l_y:
                #     pygame.draw.circle(screen, (0, 255, 0), (x,y), 3)
                # else:
                #     pygame.draw.circle(screen, (255, 0, 0), (x,y), 3)

                # if tile == 1:
                #     screen.blit(self.wall_img, (x, y))


class Player:
    def __init__(self, start_pos, tile_w, tile_h):
        self.pos = list(start_pos)
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.image = pygame.transform.scale(settings.IMAGE.PLAYER_IMG, (self.tile_w, self.tile_h)) #[cite: 10]

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

    def update_movement(self):
        dy, dx = self.get_movement()
        if dy != 0 or dx != 0:
            new_y = self.pos[0] + dy
            new_x = self.pos[1] + dx
            if settings.MAP[new_y][new_x] != 1:
                self.pos[0] = new_y
                self.pos[1] = new_x

    def attack(self, enemy):
        if self.pos == enemy.pos and not enemy.is_dead:
            enemy.hp -= 1
            enemy.hit_effect_timer = 10

            if enemy.hp <= 0:
                enemy.is_dead = True

    def draw(self, screen):
        x = self.pos[1] * self.tile_w
        y = self.pos[0] * self.tile_h
        screen.blit(self.image, (x, y))

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

        x = self.pos[1] * self.tile_w
        y = self.pos[0] * self.tile_h

        # --- ВИЗУАЛЬНЫЙ ЭФФЕКТ: Тряска и покраснение ---
        if self.hit_effect_timer > 0:
            x += 5  # Эффект тряски (небольшой сдвиг по оси X)
            # Рисуем красный квадрат поверх врага как вспышку урона/крови
            pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tile_w, self.tile_h))
        else:
            screen.blit(self.image, (x, y))
