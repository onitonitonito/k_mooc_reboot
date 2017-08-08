import os, sys, pygame
DESTIN_DIR = os.path.dirname(__file__)+'/sprites/'

POS_X = (480-50)/2
POS_Y = (640-(53+20))

X_MOVE = 0
Y_MOVE = 0

pygame.init()

fighter = pygame.image.load(DESTIN_DIR+'galaga_fighter.png')
fighter = pygame.transform.scale(fighter,(50,53))

DISPLAYSURF = pygame.display.set_mode((480, 640))
pygame.display.set_caption('MOVE TEST SCREEN')
FPS_CLK = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_MOVE = -5
            elif event.key == pygame.K_RIGHT:
                X_MOVE = +5
            elif event.key == pygame.K_UP:
                Y_MOVE = -5
            elif event.key == pygame.K_DOWN:
                Y_MOVE = +5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_MOVE = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                Y_MOVE = 0

        POS_X += X_MOVE
        POS_Y += Y_MOVE

        DISPLAYSURF.fill((0,0,0))
        DISPLAYSURF.blit(fighter,(POS_X, POS_Y))

        pygame.display.update()
        FPS_CLK.tick(30)

pygame.quit()
sys.exit()
