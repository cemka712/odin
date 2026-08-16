import pygame
import sys
# Импортируем классы из вашего нового файла
from classes import Environment, Player, Enemy

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class BaseScene:
    # ... (Остается как раньше)
    def handle_event(self, event): pass
    def update(self): pass
    def draw(self, screen): pass

class MenuScene(BaseScene):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Передаем размеры экрана в игровую сцену
            return GameScene(SCREEN_WIDTH, SCREEN_HEIGHT)
        return None

    def draw(self, screen):
        screen.fill((0, 0, 0)) 
        pygame.draw.rect(screen, (0, 200, 0), (120, 200, 400, 80)) # Заглушка вместо текста

class GameScene(BaseScene):
    def __init__(self, screen_width, screen_height):
        # Карта (массив)
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # 1. Инициализация окружения
        self.env = Environment(self.map_data, screen_width, screen_height)
        
        # 2. Инициализация игрока (передаем размеры тайла для картинки)
        self.player = Player([1, 1], self.env.tile_w, self.env.tile_h)
        
        # 3. Инициализация врага
        self.enemy = Enemy([3, 5], self.env.tile_w, self.env.tile_h)

    def handle_event(self, event):
        # --- 1. ОБРАБОТКА УДАРА (Кнопка X) ---
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            # Проверяем, что игрок и враг на одной клетке, и враг еще жив
            if self.player.pos == self.enemy.pos and not self.enemy.is_dead:
                self.enemy.hp -= 1                   # Отнимаем 1 HP
                self.enemy.hit_effect_timer = 10     # Включаем вспышку на 10 кадров
                
                if self.enemy.hp <= 0:
                    self.enemy.is_dead = True

        # --- 2. ПЕРЕМЕЩЕНИЕ ИГРОКА ---
        dy, dx = self.player.get_movement(event)
        
        if dy != 0 or dx != 0:
            new_y = self.player.pos[0] + dy
            new_x = self.player.pos[1] + dx
            
            # Простая проверка: если там не стена, то идем
            if self.map_data[new_y][new_x] != 1:
                self.player.pos[0] = new_y
                self.player.pos[1] = new_x

    def update(self):
        self.enemy.update()

    def draw(self, screen):
        # Вызываем методы draw наших классов
        self.env.draw(screen)
        self.enemy.draw(screen)
        self.player.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        clock.tick(60)

if __name__ == "__main__":
    main()