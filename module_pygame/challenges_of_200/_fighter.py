import os
import pygame

DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1]
WORK_DIR = os.path.join(ROOT, '_static', 'pygame_sprites', '')
FILE_IMG = 'galaga_fighter.png'



SCREEN_SIZE = (480, 640)            # screen size = 480 x 640 default
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption('TEST SCREEN [%s x %s]'%
    (SCREEN_SIZE[0],SCREEN_SIZE[1]))

FIGHTER = pygame.image.load(WORK_DIR + FILE_IMG)

while True:
    DISPLAYSURF.blit(FIGHTER,(480/4, 640/3))
    pygame.display.update()
    FPSCLOCK.tick(60)
