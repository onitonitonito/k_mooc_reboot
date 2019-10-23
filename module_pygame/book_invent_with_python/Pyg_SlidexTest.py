# import pygame, sys, random
# from pygame.locals import *

BOARDWIDTH = 4
BOARDHEIGHT = 4

def MakingBOARDmatrix():
    # Making Board MATRIX by column(4x4)
    # Board= [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
    # Board = [col-01, 02, 03, 04 ... in vertical]

    counter = 1
    board = []

    print('\t x y column[]')
    print ('-'*20)

    for x in range (BOARDWIDTH):
        column = []

        for y in range (BOARDHEIGHT):   # BOARDHEIGHT = 4,
            column.append(counter)
            counter += BOARDWIDTH       # BOARDWIDTH = 4, -- 1,5,9,13 = column

            print('column= ', x, y,' '*3,column)

        board.append(column)            #
        counter -= BOARDWIDTH * (BOARDHEIGHT -1) + BOARDWIDTH -1
        print ('-'*20)
        # counter -= 15;    (4 * 3 + 3 = 15)

    print('Board=', board)
    print()

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = None   # BLANK = None
    print('PUT board[3][3] =', board[3][3])                 # board[3][3] = 16 <-- BLANK
    print(board)
MakingBOARDmatrix()
