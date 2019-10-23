"""
# flippy 변수를 설정하는 곳
#
"""
print(__doc__)

import os

ROOT_NAME = 'pygame_flippy'
CURRENT = os.path.dirname(__file__)

DIR_ROOT = CURRENT.partition(ROOT_NAME)
DIR_CURRENT = DIR_ROOT[0]+ DIR_ROOT[1]
DIR_IMG = os.path.join(DIR_CURRENT, 'static', 'img')

IMG_BOARD = os.path.join(DIR_IMG, 'flippyboard.png')
IMG_BOARD_BG = os.path.join(DIR_IMG,'flippybackground.png')


# frames per second to update the screen
FPS = 10

# width of the program's window, in pixels / # height in pixels
WINDOWWIDTH, WINDOWHEIGHT = 640, 480

SPACESIZE = 50  # width & height of each space on the board, in pixels
BOARDWIDTH = 8  # how many columns of spaces on the game board
BOARDHEIGHT = 8  # how many rows of spaces on the game board

WHITE_TILE = 'WHITE_TILE'  # an arbitrary but unique value
BLACK_TILE = 'BLACK_TILE'  # an arbitrary but unique value

EMPTY_SPACE = 'EMPTY_SPACE'  # an arbitrary but unique value
HINT_TILE = 'HINT_TILE'  # an arbitrary but unique value

ANIMATIONSPEED = 25
# integer from 1 to 100, higher is faster animation
# Amount of space on the left & right side (XMARGIN) or above and below
# (YMARGIN) the game board, in pixels.

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE)) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE)) / 2)

#         R    G    B
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
GREEN = (0, 155,   0)
BRIGHTBLUE = (0,  50, 255)
BROWN = (174,  94,   0)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE
HINTCOLOR = BROWN


if __name__ == '__main__':
    print(ROOT_NAME)
    print(CURRENT)
    print(DIR_ROOT)
    print(DIR_CURRENT)
    print(DIR_IMG)
    print(IMG_BOARD)
    print(IMG_BOARD_BG)
