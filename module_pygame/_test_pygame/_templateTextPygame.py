import sys, pygame
from pygame.locals import *

import os
DESTIN_DIR = os.path.dirname(os.path.dirname(__file__)) + "/statics/img/"


pygame.init()

IMAGE_ICON = pygame.image.load(DESTIN_DIR + 'gameicon.png')

FPS = 30
FPS_CLOCK = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((640,480))
DISPLAYSURF.fill((100,100,0))

pygame.display.set_caption('TEST SCREEN (640 x 480)')
pygame.display.set_icon(IMAGE_ICON)

BASIC_FONT = pygame.font.Font('freesansbold.ttf', 50)

WIN_SURF1 = BASIC_FONT.render('Your text is here', True, (255,255,255))
WIN_RECT1 = WIN_SURF1.get_rect()        # <rect(0, 0, 397, 51)>
WIN_RECT1.center = (198, 25)   # <rect(122, 215, 397, 51)>

print(type(WIN_RECT1))
print((WIN_RECT1))

DISPLAYSURF.blit(WIN_SURF1, WIN_RECT1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
