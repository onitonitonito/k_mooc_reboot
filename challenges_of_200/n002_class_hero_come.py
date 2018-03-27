import os
import sys
import pygame
# from pygame.locals import *
DESTIN_DIR = os.path.dirname(__file__)+'/sprites/'

BLACK = (0,0,0)     # fill black
FPS = 30
fpsClock = pygame.time.Clock()

pygame.init()

DISPLAYSURF = pygame.display.set_mode((480, 640), 0, 32)
pygame.display.set_caption('Animation')

class Hero(object):
    def __init__(self, filename, width, height, posx, posy):
        self.filename = filename
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.x_move = 10
        self.y_move = 10

    def set_image(self):
        return pygame.image.load(DESTIN_DIR + self.filename)

    def set_size(self, obj):
        return pygame.transform.scale(obj, (self.width, self.height))      # Added

    def get_move(self,key):
        if key == 'up':
            self.posy -= self.y_move
            return self.posy
        elif key == 'down':
            self.posy += self.y_move
            return self.posy

        elif key == 'left':
            self.posx -= self.x_move
            return self.posx
        elif key == 'right':
            self.posx += self.x_move
            return self.posx
        return False

fighter = Hero('galaga_fighter.png', 40, 45, 200, 500)       #create a Hero

while True:
    ship = fighter.set_image()
    ship = fighter.set_size(ship)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = fighter.get_move('left')
                print("x=", x)
            elif event.key == pygame.K_RIGHT:
                x = fighter.get_move('right')
                print("x=", x)
            elif event.key == pygame.K_UP:
                y = fighter.get_move('up')
                print("y=", y)
            elif event.key == pygame.K_DOWN:
                y = fighter.get_move('down')
                print("y=", y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or\
            event.key == pygame.K_UP   or event.key == pygame.K_DOWN :
                pass

    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(ship, (fighter.posx, fighter.posy))    # draw object

    pygame.display.update()
    fpsClock.tick(FPS)
