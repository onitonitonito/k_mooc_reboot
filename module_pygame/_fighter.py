from assets.init import *
from assets.sprite import *


FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(
    'TEST SCREEN [%sx%s]' % (SCREEN_SIZE[0], SCREEN_SIZE[1]))

# FIGHTER = pygame.image.load(FILE_IMG_04)
FIGHTER = set_sprite(FILE_IMG_01, 50, 55)

# MAIN ROUTINE
while True:
    DISPLAYSURF.blit(FIGHTER, (480 * 0.25, 640 * 0.35))
    pygame.display.update()
    FPSCLOCK.tick(60)
