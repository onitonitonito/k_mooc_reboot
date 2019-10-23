# Pygame Practice
import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 200)

pygame.init()           # if import pygame, init() should always execute in advance
DISPLAYSURF = pygame.display.set_mode((640,480))    # set_mode
pygame.display.set_caption('Hello World~!')         # set_caption
catImg1 = pygame.image.load('../statics/img/icon_yellowCAT.png')
catImg2 = pygame.image.load('../statics/img/icon_greyCAT.png')

while True: # main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg1, (100, 100))
    DISPLAYSURF.blit(catImg2, (300, 100))

    for event in pygame.event.get():
        if event.type == QUIT:                      # event = Quit, press [x]
            pygame.quit()
            sys.exit()
        pygame.display.update()                     # update() Loop
