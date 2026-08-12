import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()

player_pos = [100,100]

run_game_loop = True
while run_game_loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run_game_loop = False

    screen.fill("black")

    pygame.draw.circle(screen, "red", player_pos, 10)
   
    pygame.display.flip()



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT] and player_pos[0] < 800:
        player_pos[0] += 5
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN] and player_pos[1] < 1000:
        player_pos[1] += 5

    clock.tick(60)

pygame.quit()
