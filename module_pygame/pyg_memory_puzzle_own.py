# Memory Puzzle
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license

import random, pygame, sys
from pygame.locals import *

FPS = 30                    # Frame Per Rate = Speed & Quality
WINDOWWIDTH = 640           #
WINDOWHEIGHT = 480          #
REVEALSPEED = 8             # defaukt Speed = 8
HINTSPEED = 1               # 8 times slower than Reveal speed
HINTBOXES = 10              # *NEW* default Hint boxes showed in startGameAnimation
BOXSIZE = 40                #
GAPSIZE = 10                #
BOARDWIDTH = 10             #
BOARDHEIGHT = 7             #

assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0,\
'Board needs to have an even number of boxes for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#               R    G    B
GRAY        = (100, 100, 100)   #646464
NAVYBLUE    = ( 60, 60,  100)   #3c6464
WHITE       = (255, 255, 255)   #ffffff
RED         = (255, 0,   0)     #ff0000
GREEN       = (0,   255, 0)     #00ff00
BLUE        = (0,   0,   255)   #0000ff
YELLOW      = (255, 255, 0)     #ffff00
ORANGE      = (255, 128, 0)     #ff8000
PURPLE      = (255, 0,   255)   #ff00ff
CYAN        = (0,   255, 255)   #00ffff

BGCOLOR         = NAVYBLUE
LIGHTBGCOLOR    = GRAY
BOXCOLOR        = WHITE
HIGHLIGHTCOLOR  = GREEN                 # BLUE = default

DONUT       = 'donut'
SQUARE      = 'square'
DIAMOND     = 'diamond'
LINES       = 'lines'
OVAL        = 'oval'

ALLCOLORS   = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)  # 7
ALLSHAPES   = (DONUT, SQUARE, DIAMOND, LINES, OVAL)             # 5

assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,\
"Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
    pygame.display.set_caption('Memory TEST Game :: %s x %s' %(WINDOWWIDTH,WINDOWHEIGHT))

    mousex = 0      # When Mouse.Event happens, initial X.Coords
    mousey = 0      # When Mouse.Event happens, initial Y.Coords

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealBoxesData(False)

    firstSelection = None   # store (x,y), when the first Box is clicked.
    DISPLAYSURF.fill(BGCOLOR)

    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False
        DISPLAYSURF.fill(BGCOLOR)   # draw WINDOW
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None :
            # mouse pointer is on the boxes
            if not revealedBoxes[boxx][boxy]: drawHighlightBox(boxx,boxy)

            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)]) # Open BOX
                revealedBoxes[boxx][boxy] = True                # Set as revelaed boxe

                if firstSelection == None: firstSelection = (boxx, boxy) # 1st open - store (X,Y)
                else:   # box which is clicked 2nd, examin right pairs of Icon or not.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # If Two icons doesn't matches, close two boxes all
                        pygame.time.wait(1000)  # waits 1 Second
                        coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes):     # if matches
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)      # wait 2 sec


                        mainBoard = getRandomizedBoard()        # Reset Board
                        revealedBoxes = generateRevealBoxesData(False)

                        drawBoard(mainBoard, revealedBoxes)     # Show Boxes for a while
                        pygame.display.update()
                        pygame.time.wait(1000)

                        startGameAnimation(mainBoard)   # Show Game begin Animation

                    firstSelection = None               # Reset firstSelection Variable

        # draw screen and wait for a while
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateRevealBoxesData(val):   # val = True Or False ( 0 or 1 )
    revealedBoxes = []
    for i in range (BOARDWIDTH):
        revealedBoxes.append( [val]*BOARDHEIGHT)
    return revealedBoxes

def getRandomizedBoard():
    icons = []                   # declair ARRAY
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append( (shape, color) )

    random.shuffle(icons)       # shuffle icon lists randomly
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 2)    # How many icons needed?

    icons = icons[:numIconsUsed] * 2            # Making each pairs
    random.shuffle(icons)

    board = []
    for x in range (BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append( icons[0])
            del icons[0]                # Del. first icons[0] - Assigned icon
        board.append(column)
    return board

def splitIntoGroupsOf(groupSize,theList):
    result = []
    for i in range (0, len(theList), groupSize):
        result.append( theList[i : i+groupSize] )
    return result

def leftTopCoordsOfBox(boxx,boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left,top)

def getBoxAtPixel(x,y):
    for boxx in range(BOARDWIDTH):
        for boxy in range (BOARDHEIGHT):
            left,top = leftTopCoordsOfBox(boxx,boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x,y):
                return (boxx,boxy)
    return (None, None)

def drawIcons(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25)       # syntactic sugar
    half = int (BOXSIZE * 0.5)          # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx,boxy)   # real PIX. coords

    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half-5)
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), quarter-5)

    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half ))

    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left+half, top), (left+BOXSIZE-1, top+half), (left + half, top + BOXSIZE - 1),(left, top + half)))

    elif shape == LINES:
        for i in range(0,BOXSIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top +i),(left +i,top))
            pygame.draw.line(DISPLAYSURF, color, (left +i, top +BOXSIZE -1),(left +BOXSIZE -1,top +i))

    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF,color, (left, top + quarter, BOXSIZE, half))

def getShapeAndColor(board, boxx, boxy):
    # shape value @(x,y) = board [x][y][0]
    # color value @(x,y) = board [x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]

def drawBoxCovers(board, boxes, coverage):
    # draw Boxes which are OPEN or CLOSED.
    # Boxes have 2 items and X,Y Coords
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0],box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))

        shape, color = getShapeAndColor(board,box[0],box[1])
        drawIcons(shape, color, box[0], box[1])

        if coverage > 0:
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))

    pygame.display.update()
    FPSCLOCK.tick(FPS)

def revealBoxesAnimation(board, boxesToReveal):
    # Open Box Animation
    for coverage in range(BOXSIZE, (-REVEALSPEED)-1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board,boxesToCover):
    # Close Box Animation
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)

def drawBoard(board, revealed):
    # Draw Every Boxes
    for boxx in range (BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)

            if not revealed [boxx][boxy]:
                # draw closed box
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))

            else :
                # draw OPEN, indeed Draw Icon
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcons(shape, color, boxx, boxy)

def drawHighlightBox(boxx,boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left-5, top-5, BOXSIZE+10, BOXSIZE+10), 5)

def startGameAnimation(board):
    coveredBoxes = generateRevealBoxesData(False) # Animation of OPEN & SHOW 8~10 Boxes randomly
    boxes = []
    for x in range (BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    boxGroup = splitIntoGroupsOf(HINTBOXES, boxes)  # boxes = (x,y), HINTBOXES = 8 (default)
    drawBoard(board, coveredBoxes)

    for boxGroup in boxGroup:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)

def gameWonAnimation(board):
    # if player find all pairs of Icons, Blinking screen
    coveredBoxes = generateRevealBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range (13):
        color1, color2 = color2, color1       # Change colors
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)

def hasWon(revealedBoxes):
    # if every BOXES are opeend, return True. or Return False
    for i in revealedBoxes:
        if False in i:
            return False    # if closed box(es), return False
    return True

if __name__ == '__main__':
    main()
