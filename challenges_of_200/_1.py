import os
import pygame

DESTIN_DIR = os.path.join(os.path.dirname(__file__),'sprites/')
SCREEN_SIZE = (480, 640)            # screen size = 480 x 640 default
FILE_IMG = 'galaga_fighter.png'

FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('TEST SCREEN')

FIGHTER = pygame.image.load(DESTIN_DIR + FILE_IMG)

while True:
    DISPLAYSURF.blit(FIGHTER,(100,100))
    pygame.display.update()
    FPSCLOCK.tick(60)
