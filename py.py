import pygame 

pygame.init()
screen = pygame.display.set_mode((800, 600))

game_cucle = True

player_image = pygame.image.load('static/edward.png').convert_alpha()

target_rect = pygame.Rect(100, 100, 200, 200)

player_image = pygame.transform.scale(player_image, target_rect.size)

while game_cucle:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cucle = False

    screen.fill((255, 255, 255))

    screen.blit(player_image, target_rect)

    pygame.display.flip()

pygame.quit()
