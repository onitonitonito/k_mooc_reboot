import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

FLASHSPEED = 500        # ms.
FLASHDELAY = 200        # ms.
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4             # sec without reaction

#               R       G       B
WHITE       = ( 255,   255, 255)        #ffffff
BLACK       = ( 0,     0,     0)        #000000
BRIGHTRED   = ( 255,   0,     0)        #ff0000
RED         = ( 155,   0,     0)        #9b0000
BRIGHTGREEN = ( 0,   255,     0)        #00ff00
GREEN       = ( 0,   155,     0)        #009b00
BRIGHTBLUE  = ( 0,      0,  255)        #0000ff
BLUE        = ( 0,      0,  155)        #00009b
BRIGHTYELLOW= ( 255,   255,   0)        #ffff00
YELLOW      = ( 155,   155,   0)        #9b9b00
DARKGRAY    = ( 40,    40,   40)        #282828
bgColor     = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

# RECT object for 4 each buttons
# col-00 = YELLOW, RED (SAME X, diff Y)
# col-01 = BLUE, GREEN (SAME X, diff Y)
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT    = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
BLUERECT   = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
GREENRECT  = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simulate Game')

    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    infoSurf = BASICFONT.render('Match the pattern by clicking on the buttons or using the Q,W,A,S keys.', 1, DARKGRAY)
    infoRect = infoSurf.get_rect()
    infoRect.topleft = (10, WINDOWHEIGHT - 25)

    # Load Soundfile (./statics/sound/.ogg)
    BEEP1 = pygame.mixer.Sound('./statics/sound/beep1.ogg')
    BEEP2 = pygame.mixer.Sound('./statics/sound/beep2.ogg')
    BEEP3 = pygame.mixer.Sound('./statics/sound/beep3.ogg')
    BEEP4 = pygame.mixer.Sound('./statics/sound/beep4.ogg')

    # New Game Initialize
    pattern = []    # Set pattern
    currentStep = 0
    lastClickTime = 0           #
    score = 0

    # waitingForInput = False, --- pattern playing
    # if True                   -- Wait for key input

    waitingForInput = False

    while True:         # Game loop
        clickedButton = None    #
        DISPLAYSURF.fill(bgColor)

        drawButtons()

        scoreSurf = BASICFONT.render('Score : ' + str(score), 1, WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 100, 10)

        DISPLAYSURF.blit(infoSurf, infoRect)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

        checkForQuit()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                clickedButton = getButtonClicked(mousex, mousey)

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    clickedButton = YELLOW

                elif event.key == K_w:
                    clickedButton = BLUE

                elif event.key == K_a:
                    clickedButton = RED

                elif event.key == K_s:
                    clickedButton = GREEN

        if not waitingForInput:
            # SHow pattern
            pygame.display.update()
            pygame.time.wait(1000)          # wait 1,000ms

            pattern.append(random.choice((YELLOW, BLUE, RED, GREEN)))

            for button in pattern:
                flashButtonAnimation(button)
                pygame.time.wait(FLASHDELAY)

            waitingForInput = True

        else:
            # Input mode
            if clickedButton and clickedButton == pattern[currentStep]:
                # if correct
                flashButtonAnimation(clickedButton)
                currentStep += 1
                lastClickTime = time.time()

                if currentStep == len(pattern):
                    # if push last button
                    changeBackgroundAnimation()
                    score += 1
                    waitingForInput = False
                    currentStep = 0         # game turn is over, and reset

            elif (clickedButton and clickedButton != pattern[currentStep])\
            or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
                # Wrong push or timeout lapse
                gameOverAnimation()

                # RESET pattern
                pattern = []
                currentStep = 0             #
                waitingForInput = False     # Show playing
                score = 0
                pygame.time.wait(1000)

                changeBackgroundAnimation()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT):
        terminate()

    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)    # if other key, return que

def flashButtonAnimation(color, animationSpeed = 50):
    if color == YELLOW:
        sound = BEEP1
        flashColor = BRIGHTYELLOW
        rectangle = YELLOWRECT

    elif color == BLUE:
        sound = BEEP2
        flashColor = BRIGHTBLUE
        rectangle = BLUERECT

    elif color == RED:
        sound = BEEP3
        flashColor = BRIGHTRED
        rectangle = REDRECT

    elif color == GREEN:
        sound = BEEP4
        flashColor = BRIGHTGREEN
        rectangle = GREENRECT

    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
    flashSurf = flashSurf.convert_alpha()

    r, g, b = flashColor
    sound.play()

    for start, end, step in ((0, 255, 1),(255, 0, -1)):     # animation loop
        for alpha in range(start, end, step*animationSpeed):
            checkForQuit()
            DISPLAYSURF.blit(origSurf, (0, 0))      # blit(Obj, (x,y))
            flashSurf.fill((r, g, b, alpha))

            DISPLAYSURF.blit(flashSurf, rectangle.topleft)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    DISPLAYSURF.blit(origSurf, (0, 0))

def drawButtons():
    pygame.draw.rect(DISPLAYSURF, YELLOW,   YELLOWRECT)
    pygame.draw.rect(DISPLAYSURF, BLUE,     BLUERECT)
    pygame.draw.rect(DISPLAYSURF, RED,      REDRECT)
    pygame.draw.rect(DISPLAYSURF, GREEN,    GREENRECT)

def changeBackgroundAnimation(animationSpeed = 40):
    global bgColor
    newBgColor = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255))

    newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
    newBgSurf = newBgSurf.convert_alpha()

    r, g, b = newBgColor

    for alpha in range(0, 255, animationSpeed):         # Animation loop
        checkForQuit()
        DISPLAYSURF.fill(bgColor)

        newBgSurf.fill((r, g, b, alpha))
        DISPLAYSURF.blit(newBgSurf, (0, 0))

        drawButtons()           # Re-draw buttons on color

        pygame.display.update()
        FPSCLOCK.tick(FPS)
    bgColor = newBgColor

def gameOverAnimation(color= WHITE, animationSpeed= 50):
    # play Beep 1,2,3,4 at once... blinking bgColor
    origSurf = DISPLAYSURF.copy()
    flashSurf = pygame.Surface(DISPLAYSURF.get_size())
    flashSurf = flashSurf.convert_alpha()

    BEEP1.play()
    BEEP2.play()
    BEEP3.play()
    BEEP4.play()

    r, g, b = color

    for i in range(3):
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            #
            #
            for alpha in range(start, end, step * animationSpeed):
                # Alpha = transparency / 255 = opaque, 0 = transparency
                checkForQuit()

                flashSurf.fill((r, g, b, alpha))
                DISPLAYSURF.blit(origSurf,(0, 0))
                DISPLAYSURF.blit(flashSurf,(0, 0))

                drawButtons()
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def getButtonClicked(x, y):
    if YELLOWRECT.collidepoint((x, y)):
        return YELLOW

    elif BLUERECT.collidepoint((x, y)):
        return BLUE

    elif REDRECT.collidepoint((x, y)):
        return RED

    elif GREENRECT.collidepoint((x, y)):
        return GREEN

    return None


if __name__ == '__main__':
    main()
