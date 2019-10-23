import pygame, sys, random
from pygame.locals import *

#                   R    G    B
RED             = (255, 0,   0)         #ff0000
GREEN           = (0,   255, 0)         #00ff00
BLUE            = (0,   0,   255)       #0000ff
YELLOW          = (255, 255, 0)         #ffff00
ORANGE          = (255, 128, 0)         #ff8000
WHITE           = (255, 255, 255)       #ffffff
DARKTURQUOISE   = ( 3,  54,  73)        #033649
BRIGHTBLUE      = ( 0,  50, 255)        #0032ff
BLACK           = ( 0,  0,  0)          #000000

BOARDWIDTH = 4          # NUM of Col = 4
BOARDHEIGHT = 4         # NUM of Row = 4
BORDERCOLOR = BRIGHTBLUE
BGCOLOR = DARKTURQUOISE

TILESIZE = 80           # TILESIZE = 80 x 80
TILECOLOR = GREEN

WINDOWWIDTH = 640       # WINDOW = 640 x 480
WINDOWHEIGHT = 480

FPS = 30                # Frame Per Second
BLANK = None            # Empty 1 block = None

BASICFONTSIZE = 20
TEXTCOLOR = WHITE

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH -1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT -1))) / 2)

UP = 'up'
DOWN ='down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT,\
        NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()           # Initialize function, Always be done beforehand.
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))   # set WINDOWW

    pygame.display.set_caption('SLIDE PUZZLE')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)     # Size = 20

    # RECT.BORDER will stored in OPTIONS / makeText()
    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR,
        WINDOWWIDTH - 120, WINDOWHEIGHT - 90)

    NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR,
        WINDOWWIDTH - 120, WINDOWHEIGHT - 60)

    SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, TILECOLOR,
        WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    mainBoard, solutionSeq = generateNewPuzzle(80)        #

    SOLVEDBOARD = getStartingBoard()        # State of Finish BD = Start BD
    allMoves = []                           #

    while True:         # main Loop
        SlideTo = None  # the direction, if any, a tile should Slide
        msg = 'Click tile or press arrow keys to slide.'    # Top-left MESSAGE
        if mainBoard == SOLVEDBOARD: msg = 'Solved!'

        drawBoard(mainBoard, msg)
        checkForQuit()

        for event in pygame.event.get():         # event Loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    #
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, allMoves)     # CLICK - RESET Button
                        allMoves = []

                    elif NEW_RECT.collidepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80)    # Click NEW Game
                        allMoves = []

                    elif SOLVE_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves)
                        allMoves = []

                else:
                    # check there's BLANK arround clicked tile

                    blankx, blanky = getBlankPosition(mainBoard)

                    if spotx == blankx+1 and spoty == blanky:   SlideTo = LEFT
                    elif spotx == blankx-1 and spoty == blanky:   SlideTo = RIGHT
                    elif spotx == blankx and spoty == blanky+1:   SlideTo = UP
                    elif spotx == blankx and spoty == blanky-1:   SlideTo = DOWN

            elif event.type == KEYUP:
                #
                if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT) : SlideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT) : SlideTo = RIGHT
                elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP) : SlideTo = UP
                elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN) : SlideTo = DOWN

        if SlideTo:
            slideAnimation(mainBoard,SlideTo, 'Click tile or Press arrow keys to slide', 8)     # Show slide on screen
            makeMove(mainBoard, SlideTo)        #
            allMoves.append(SlideTo)            # write slide

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate ():               # exit ()
    pygame.quit()
    sys.exit()

def checkForQuit():             # check QUIT event
    for event in pygame.event.get(QUIT):    # Click [x] = QUIT
        terminate()                         # sys.exit()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:           # Click ESC
            terminate()                     # sys.exit()

        pygame.event.post(event)        # If other key-in, Return Event-object

def getStartingBoard():         # Making MATRIX[][]
    # Board= [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16=None]]
    # Board = [col-01, 02, 03, 04 ... in vertical]
    counter = 1
    board = []

    for x in range (BOARDWIDTH):
        column = []

        for y in range (BOARDHEIGHT):   # BOARDHEIGHT = 4,
            column.append(counter)
            counter += BOARDWIDTH       # BOARDWIDTH = 4, -- 1,5,9,13 = column

        board.append(column)            #
        counter -= BOARDWIDTH * (BOARDHEIGHT -1) + BOARDWIDTH -1
        # counter -= 15;    (4 * 3 + 3 = 15)

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
    return board

def getBlankPosition(board):         # Where's Blank Piece(x,y)?
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y]  == BLANK:       # Blank = None
                return (x,y)                # blank (x,y)coordinates

def makeMove(board,move):       # it doesn't check wheather it can move or NOT?
    # board array, move(Key_value, up,down,left,right)
    blankx, blanky = getBlankPosition(board)    # get (x,y)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky+1] = \
        board[blankx][blanky+1], board[blankx][blanky]

    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky-1] = \
        board[blankx][blanky-1], board[blankx][blanky]

    elif move == LEFT:
        board[blankx][blanky], board[blankx+1][blanky] = \
        board[blankx+1][blanky], board[blankx][blanky]

    elif move == RIGHT:
        board[blankx][blanky], board[blankx-1][blanky] = \
        board[blankx-1][blanky], board[blankx][blanky]

def isValidMove(board, move):
    # board array, move(Key_value, up,down,left,right)
    blankx, blanky = getBlankPosition(board)    # get (x,y)

    return  (move == UP and     blanky != len(board[0])-1) or \
            (move == DOWN and   blanky != 0) or \
            (move == LEFT and   blankx != len(board)-1) or \
            (move == RIGHT and  blankx != 0)

def getRandomMove(board, lastMove=None):
    # vailde move = 4 Direction
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # if disable, delete Direction
    if lastMove == UP or not isValidMove(board,DOWN):
        validMoves.remove(DOWN)

    if lastMove == DOWN or not isValidMove(board,UP):
        validMoves.remove(UP)

    if lastMove == LEFT or not isValidMove(board,RIGHT):
        validMoves.remove(RIGHT)

    if lastMove == RIGHT or not isValidMove(board,LEFT):
        validMoves.remove(LEFT)

    #
    return random.choice(validMoves)

def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)

    return (left, top)

def getSpotClicked(board, x, y):
    # turn x,y PIXEL Coords --> LC_Coords
    for tileX in range (len(board)):                        # len = 16
        for tileY in range (len(board[0])):                 # len = 4
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left,top,TILESIZE, TILESIZE)

            if tileRect.collidepoint(x, y):
                return (tileX, tileY)

    return (None, None)

def drawTile(tileX, tileY, number, adjx=0, adjy=0):
    #
    #
    left,top = getLeftTopOfTile(tileX, tileY)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left+adjx, top+adjy, TILESIZE, TILESIZE))
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left+int(TILESIZE/2)+adjx, top+int(TILESIZE/2)+adjy
    DISPLAYSURF.blit(textSurf, textRect)

def makeText(text, color, bgcolor, top, left):
    #
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def drawBoard(board, message):
    DISPLAYSURF.fill(BGCOLOR)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            if board[tileX][tileY]:
                drawTile(tileX, tileY, board[tileX][tileY])
    left, top = getLeftTopOfTile(0, 0)      #
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE

    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left-5, top-5, width+11, height+11), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)

def slideAnimation(board, direction, message, animationSpeed):
    # CAUSION : This doesn't check available move
    blankx, blanky = getBlankPosition(board)

    if direction ==     UP:  movex = blankx;   movey = blanky+1
    elif direction == DOWN:  movex = blankx;   movey = blanky-1
    elif direction == LEFT:  movex = blankx+1; movey = blanky
    elif direction == RIGHT: movex = blankx-1; movey = blanky

    # prepare basic SURF
    drawBoard(board, message)

    baseSurf = DISPLAYSURF.copy()
    # draw blank tile on baseSurf Surface moving tile

    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BGCOLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))

    for i in range(0, TILESIZE, animationSpeed):
        #
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0,0))       #

        if direction == UP: drawTile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN: drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT: drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT: drawTile(movex, movey, board[movex][movey], i, 0)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

def generateNewPuzzle(numSlides):
    #
    #
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')

    pygame.display.update()
    pygame.time.wait(500)       # wait 500 msec
    lastMove = None

    for i in range(numSlides):
        move = getRandomMove(board, lastMove)

        slideAnimation(board, move, 'Generating New Puzzle.....',\
            animationSpeed=int(TILESIZE/3))

        makeMove(board, move)
        sequence.append(move)
        lastMove = move

    return (board, sequence)

def resetAnimation(board, allMoves):    #
    #
    revAllMoves =  allMoves[:]          # make copy
    revAllMoves.reverse()

    for move in revAllMoves:
        if   move == UP:      oppositeMove = DOWN
        elif move == DOWN:    oppositeMove = UP
        elif move == LEFT:    oppositeMove = RIGHT
        elif move == RIGHT:   oppositeMove = LEFT

        slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE/2))
        makeMove(board, oppositeMove)

if __name__ == '__main__':
    main()
