import pygame 


def hello_world(x):
    if x == 'print':
        print('Hello World!')
    else:
        print(x)

hello_world('print')

pygame.init()
screen = pygame.display.set_mode((600, 300))


display1 = True
while display1:

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display1 = False


if __name__ == '__main__':
    print('hello world')
