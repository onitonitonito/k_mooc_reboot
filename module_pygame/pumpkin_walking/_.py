"""
# for TEST :
#
"""
import pygame

from pygame.locals import *
from assets.config import *
from assets.sprite import MySprite

print(__doc__)




if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((400,600))

    array_key_strokes = [
        (KEYUP and K_ESCAPE),
        (KEYUP and K_SPACE),
        (KEYUP and K_w),
        (KEYUP and K_a),
        (KEYUP and K_s),
        (KEYUP and K_d),
    ]

    while True:
        for event in pygame.event.get(KEYUP):
            print(event)
            if event in array_key_strokes:
                pygame.quit()
                sys.exit()


        pygame.display.update()
