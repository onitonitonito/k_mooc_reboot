import pygame, sys
from pygame.locals import *

pygame.init()       # always

DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello~ World of Pygame!")

#               R    G    B
RED         = (255, 0,   0)
GREEN       = (0,   255, 0)
BLUE        = (0,   0,   255)
YELLOW      = (255, 255, 0)
ORANGE      = (255, 128, 0)
WHITE       = (255, 255, 255)

fontOBJ = pygame.font.Font('freesansbold.ttf', 35)
textSurfaceOBJ = fontOBJ.render('Hello, Pygame~!',True, GREEN, ORANGE)
textRectOBJ = textSurfaceOBJ.get_rect()
textRectOBJ.center = (200,120)

while True:         # main loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceOBJ, textRectOBJ)

    for event in pygame.event.get():
        if event.type == QUIT:                      # event = Quit, press [x]
            pygame.quit()
            sys.exit()
        pygame.display.update()                     # update() Loop
