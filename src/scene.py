import pygame
import sys

class BaseScene:
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        pass

class MenuScene(BaseScene):
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            return GameScene()
        return None

    def draw(self, screen):
        screen.fill((0, 0, 0)) 
        
        # Вместо шрифта рисуем большой зелёный прямоугольник,
        # символизирующий, что мы в меню.
        pygame.draw.rect(screen, (0, 200, 0), (120, 200, 400, 80))
        
        # Можно нарисовать внутри него красный квадрат, как символ игрока
        pygame.draw.rect(screen, (255, 0, 0), (300, 220, 40, 40))

class GameScene(BaseScene):
    def __init__(self):
        # Окружение через двумерный массив (карту): 1 - стена, 0 - пол
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
        ]
        self.player_pos = [1, 1] # [строка, колонка] (Y, X)

    def handle_event(self, event):
        # --- 1. ОБРАБОТКА УДАРА (Кнопка X) ---
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            # Проверяем, что игрок и враг на одной клетке, и враг еще жив
            if self.player.pos == self.enemy.pos and not self.enemy.is_dead:
                self.enemy.hp -= 1                   # Отнимаем 1 HP
                self.enemy.hit_effect_timer = 10     # Включаем вспышку на 10 кадров
                
                if self.enemy.hp <= 0:
                    self.enemy.is_dead = True
                    # Здесь позже можно будет добавить звук смерти врага

        # --- 2. ПЕРЕМЕЩЕНИЕ ИГРОКА ---
        dy, dx = self.player.get_movement(event) #[cite: 1]
        
        if dy != 0 or dx != 0: #[cite: 1]
            new_y = self.player.pos[0] + dy #[cite: 1]
            new_x = self.player.pos[1] + dx #[cite: 1]
            
            # Простая проверка: если там не стена, то идем[cite: 1]
            if self.map_data[new_y][new_x] != 1: #[cite: 1]
                self.player.pos[0] = new_y #[cite: 1]
                self.player.pos[1] = new_x #[cite: 1]

    def update(self):
        # Здесь будет функция расчёта (проверка границ массива, столкновений)
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        # Отрисовка массива
        for row_idx, row in enumerate(self.map_data):
            for col_idx, tile in enumerate(row):
                if tile == 1:
                    # Рисуем серые квадраты (стены)
                    pygame.draw.rect(screen, (100, 100, 100), (col_idx * 40, row_idx * 40, 38, 38))
                    
        # Отрисовка игрока (обязательно ВНЕ цикла перебора карты)
        # Координата X = колонка (player_pos[1]), координата Y = строка (player_pos[0])
        pygame.draw.rect(screen, (255, 0, 0), (self.player_pos[1] * 40, self.player_pos[0] * 40, 38, 38))


# === Менеджер сцен и главный цикл ===
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Scene Manager Test")
    clock = pygame.time.Clock()

    # Устанавливаем начальную сцену
    active_scene = MenuScene()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Передаем событие активной сцене
            next_scene = active_scene.handle_event(event)
            # Если сцена вернула новый объект сцены, переключаемся на него
            if next_scene is not None:
                active_scene = next_scene

        # Вызываем логику и отрисовку активной сцены
        active_scene.update()
        active_scene.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()