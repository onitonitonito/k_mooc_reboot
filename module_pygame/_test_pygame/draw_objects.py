"""
# pygame Drawing_examples
#
"""
print(__doc__)

#
import sys
import pygame
from pygame.locals import *

# SET COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

DISPLAYSURF = pygame.display.set_mode(
                            (500, 400),     # resolutions
                            0,              # flags=0
                            32,             # depth=0
                        )
pygame.display.set_caption('Drawing_examples')

# SET
DISPLAYSURF.fill(WHITE)

pygame.draw.polygon(
                DISPLAYSURF,   # Surface
                GREEN,         # color
                (              # pointlist
                    (146, 0),
                    (291, 106),
                    (236, 277),
                    (56, 277),
                    (0, 106),
                ),
                5,                  # width=0 ... fill-in
            )

pygame.draw.line(
                DISPLAYSURF,        # Surface
                BLUE,               # color
                (60, 60),           # pointlist
                (120, 60),
                10,                 # width
            )

pygame.draw.line(
                DISPLAYSURF,
                BLUE,
                (120, 60),
                (60, 120),
                1,                   # width = default:1
            )

pygame.draw.line(
                DISPLAYSURF,        # Surface
                BLUE,               # color
                (60, 120),          # pointlist
                (120, 120),
                10,                 # width
            )

pygame.draw.circle(
                DISPLAYSURF,
                RED,
                (300, 100),         # pos
                80,                 # radious
                10,                 # width=0 ... fill-in
            )

pygame.draw.ellipse(
                DISPLAYSURF,
                BLUE,
                (50, 200, 150, 100),     # rect (x,y,dx,dy) - inside
                15,                      # width
            )

pygame.draw.rect(
                DISPLAYSURF,
                GREEN,
                (300, 150, 100, 100),   # rect (x,y,dx,dy)
                0,
            )


# draw dot pixel objects
pixel_array = pygame.PixelArray(DISPLAYSURF)

for x in range(150, 251, 2):
    pixel_array[x][200] = BLUE
    pixel_array[200][x] = RED


# main LOOP
while True:
    for event in pygame.event.get():

        event_dict = {
            'quit' : [
                (event.type == QUIT),
                (event.type == KEYUP and event.key == K_ESCAPE),
            ],
        }

        print(event_dict)

        if True in event_dict['quit']:
            pygame.quit()

    pygame.display.update()
