# page = 46
import sys, pygame
from pygame.locals import *

pygame.init()

FPS = 60            # Frame Per Second
fpsCLOCK = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((640,480), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 200)
catImg = pygame.image.load('../statics/img/icon_yellowCAT.png')
catx = 10
caty = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx >= 560:
            direction = 'down'

    elif direction == 'down':
        caty += 5
        if caty >= 410:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx <= 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty <= 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsCLOCK.tick(FPS)
