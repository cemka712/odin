import pygame

from src.config import settings


class Player:
    def __init__(self, start_pos, tile_w, tile_h):
        self.pos = list(start_pos)
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.image = pygame.transform.scale(settings.IMAGE.PLAYER_IMG, (self.tile_w, self.tile_h)) #[cite: 10]

    def get_movement(self):
        dy, dx = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: dx = -1
        if keys[pygame.K_RIGHT]: dx = 1
        if keys[pygame.K_UP]: dy = -1 
        if keys[pygame.K_DOWN]: dy = 1
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