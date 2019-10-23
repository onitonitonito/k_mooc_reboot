import pygame, sys, random
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20           # Grid size1

# Checkout INOUT
assert WINDOWWIDTH % CELLSIZE == 0, "WINDOWWIDTH must be a muliple of CELLSIZE"
assert WINDOWHEIGHT % CELLSIZE == 0, "WINDOWHEIGHT must be a muliple of CELLSIZE"

CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#                   R    G    B
WHITE           = (255, 255, 255)       #ffffff
BLACK           = ( 0,  0,  0)          #000000
RED             = (255, 0,   0)         #ff0000
GREEN           = (0,   255, 0)         #00ff00
DARKGREEN       = (0,   155, 0)         #009b00
DARKGRAY        = (40,   40, 40)        #282828

BLUE            = (0,   0,   255)       #0000ff
YELLOW          = (255, 255, 0)         #ffff00
ORANGE          = (255, 128, 0)         #ff8000
DARKTURQUOISE   = ( 3,  54,  73)        #033649
BRIGHTBLUE      = ( 0,  50, 255)        #0032ff

BGCOLOR = BLACK

UP = 'up'
DOWN ='down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0     # Synthetic SUGAR, HEAD = 0 index



def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()           # Pygame Initialize
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))   # set WINDOWW
    pygame.display.set_caption('WORM.. WORMY!')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)     # Size = 18
    # Load Soundfile (.ogg)
    BEEP1 = pygame.mixer.Sound('./statics/sound/beep1.ogg')
    BEEP2 = pygame.mixer.Sound('./statics/sound/beep2.ogg')
    BEEP3 = pygame.mixer.Sound('./statics/sound/beep3.ogg')
    BEEP4 = pygame.mixer.Sound('./statics/sound/beep4.ogg')

    showStartScreen()

    while True:
        runGame()
        BEEP2.play()                #if out of rungame()Loop -- BEEP3
        showGameOverScreen()

def runGame():
    #
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)

    wormCoords = [
        {'x' : startx,      'y': starty},
        {'x' : startx - 1,  'y': starty},
        {'x' : startx - 2,  'y': starty},
    ]

    direction = RIGHT

    # Randomly place APPLE
    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():        # event Loop
            if event.type == QUIT:  terminate()

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key ==K_a) and direction != RIGHT:
                    direction = LEFT

                elif (event.key == K_RIGHT or event.key ==K_d) and direction != LEFT:
                    direction = RIGHT

                elif (event.key == K_UP or event.key ==K_w) and direction != DOWN:
                    direction = UP

                elif (event.key == K_DOWN or event.key ==K_s) and direction != UP:
                    direction = DOWN

                elif event.key == K_ESCAPE:
                    terminate()

        # Check worm collided to Wall
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or\
            wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return              # GAME OVER

        # Check worm eat APPLE
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:

            # Don't erase wormy's tail
            BEEP4.play()
            apple = getRandomLocation()    # place new APPLE

        else:   del wormCoords[-1]          # Do Erase wormy's tail

        # Add Cell to moving direction
        if direction == UP:     newHead = {'x':wormCoords[HEAD]['x'],   'y':wormCoords[HEAD]['y']-1}
        elif direction == DOWN: newHead = {'x':wormCoords[HEAD]['x'],   'y':wormCoords[HEAD]['y']+1}
        elif direction == LEFT: newHead = {'x':wormCoords[HEAD]['x']-1,   'y':wormCoords[HEAD]['y']}
        elif direction == RIGHT: newHead = {'x':wormCoords[HEAD]['x']+1,  'y':wormCoords[HEAD]['y']}

        wormCoords.insert(0, newHead)

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords)-3)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)

    if len(keyUpEvents) == 0:   return None
    if keyUpEvents[0].key == K_ESCAPE:  terminate()
    return keyUpEvents[0].key

def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0

    while True:
        DISPLAYSURF.fill(BGCOLOR)

        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT /2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT /2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()      # clear EVENT.QUE
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        degrees1 += 3       # rotate 3, every Frame
        degrees1 += 7       # rotate 7, every Frame

def terminate():
    pygame.quit()
    sys.exit()

def getRandomLocation():
    return {'x' : random.randint(0, CELLWIDTH - 1),
            'y' : random.randint(0, CELLHEIGHT -1) }

def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 70)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()

    gameRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT/3 - 25)
    overRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT/3 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)           # 500 ms

    checkForKeyPress()              # clear every Key.Input in Event.QUE

    while True:
        if checkForKeyPress():
            pygame.event.get()      # clear Event.QUE
            return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' %(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)

    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect( x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)

        wormInnerSegmentRect = pygame.Rect( x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE

    appleRect = pygame.Rect( x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):   # draw vertical
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):   # draw horizontal
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

if __name__ == '__main__':
    main()
