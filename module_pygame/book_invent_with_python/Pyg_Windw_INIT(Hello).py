# Pygame Practice
import pygame, sys
from pygame.locals import *

#               R    G    B
RED         = (255, 0,   0)
GREEN       = (0,   255, 0)
BLUE        = (0,   0,   255)
YELLOW      = (255, 255, 0)
ORANGE      = (255, 128, 0)
WHITE       = (255, 255, 255)

pygame.init()           # if import pygame, init() should always execute in advance
DISPLAYSURF = pygame.display.set_mode((640,480))    # set_mode
DISPLAYSURF.fill(WHITE)                             # fill bground white

pygame.display.set_caption('Hello World~!')         # set_caption

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:                      # event = Quit, press [x]
            pygame.quit()
            sys.exit()
        pygame.display.update()                     # update() Loop
