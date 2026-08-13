

import pygame 


def hello_world(x):
    if x == 'print':
        print('Hello World!')
    else:
        print(x)

hello_world('print')
pygame.init()
screen = pygame.display.set_mode()

print('hello world')