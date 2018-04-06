#! python
import os
import sys
import random
import pygame
''' further development
        - encounter enemy and cross fire.
'''
DICT_OBJ = {            # SIZE x,y   POS x,y   file_name
            'g_catcher' : [36, 38, 200, 100,'Green_Catcher.png'],
            'gremlin'   : [36, 38, 200, 150,'gremlin_0001.png'],
            'bee'       : [36, 38, 200, 50,'Fly_0001.png'],
            'scorpion'  : [36, 38, 200, 250,'scorpion_0001.png'],
            'pheonix'   : [36, 38, 200, 300,'pheonix_0001.png'],
            'bullit'    : [13, 22, 200, 550,'rocket_0001.png'],}
DESTIN_DIR = os.path.join(os.path.dirname(__file__), 'sprites', 'Galaga/')
print(DESTIN_DIR)

# COLOR TABLE
BLACK = (0, 0, 0)
RED = (255, 0, 0)

PAD_WIDTH = 480
PAD_HEIGHT = 640

FIGHTER_WIDTH = 36
FIGHTER_HEIGHT = 38

ENEMY_WIDTH = 36
ENEMY_HEIGHT = 38

DICT_OBJ['fighter'] = [FIGHTER_WIDTH, FIGHTER_HEIGHT,
                       (PAD_WIDTH - FIGHTER_WIDTH)/2,
                       PAD_HEIGHT - (FIGHTER_HEIGHT + 10), 'Ship_White.png']

# DRAW OBJECTS
def set_image(filename):
    return pygame.image.load(filename)

def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))

def set_rotate(obj, angle):
    return pygame.transform.rotate(obj, angle)

def set_obj(dict_key, f_name_wdir, rotate=0):
    """ MAKING IMAG_OBJ Using dict_key as OBJ_name """
    obj_name = dict_key
    obj_name = set_image(f_name_wdir)
    obj_name = set_size(obj_name, DICT_OBJ[dict_key][0], DICT_OBJ[dict_key][1])
    obj_name = set_rotate(obj_name, rotate)
    return obj_name

ENEMY_X = random.randrange(0, PAD_WIDTH - ENEMY_WIDTH)
ENEMY_Y = 0
ENEMY_SPEED = 10

pygame.init()
DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
pygame.display.set_caption('My GALAGA!!')

FPS = 30
FPS_CLK = pygame.time.Clock()   # FPS_CLK.tick(FPS)

fighter = set_image(DESTIN_DIR + DICT_OBJ['fighter'][4] )
fighter = set_size(fighter, FIGHTER_WIDTH, FIGHTER_HEIGHT)

# bee = set_image(DESTIN_DIR + DICT_OBJ['bee'][4])
# bee = set_size(bee, DICT_OBJ['bee'][0], DICT_OBJ['bee'][1])
# bee = set_rotate(bee, 180)

# bullit = set_image(DESTIN_DIR + DICT_OBJ['bullit'][4])
# bullit = set_size(bullit, DICT_OBJ['bullit'][0], DICT_OBJ['bullit'][1])

bee = set_obj('bee', DESTIN_DIR+'Fly_0001.png', rotate=180)
bullit = set_obj('bullit', DESTIN_DIR+'rocket_0001.png', rotate=0)

def draw_object(obj, x, y):
    DISPLAYSURF.blit(obj, (x, y))

def run_game():
    global ENEMY_Y, ENEMY_X
    # initial POS of fighter
    x = PAD_WIDTH * 0.45                     # 45% start X-point
    y = PAD_HEIGHT - (FIGHTER_HEIGHT + 10)   # 95% start Y-point

    x_change = 0                             # not moving
    y_change = 0

    BULL_X = DICT_OBJ['bullit'][2]
    BULL_Y = DICT_OBJ['bullit'][3]

    ongame = False

    while not ongame:
        # IF - Keybinding State
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = +5

                elif event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        # IF - Cross the Limit (X,Y)
        if x < 0:
            x = 0
        elif x > PAD_WIDTH - FIGHTER_WIDTH:
            x = PAD_WIDTH - FIGHTER_WIDTH
        if y < 0:
            y = 0
        elif y > PAD_HEIGHT - FIGHTER_HEIGHT:
            y = PAD_HEIGHT - FIGHTER_HEIGHT

        if ENEMY_Y > (PAD_HEIGHT-10):
            ENEMY_X = random.randrange(0, PAD_WIDTH - ENEMY_WIDTH)
            ENEMY_Y = 0

        # [POS] Give Fight a move
        x += x_change
        y += y_change

        # [POS] Give ENEMY a BUMBLE(togo) move
        togo = random.randint(0,3)
        if togo == 0:
            for n in range(random.randint(0,20)):
                ENEMY_X += 1
        elif togo == 1:
            for n in range(random.randint(0,20)):
                ENEMY_X += 0
        elif togo == 2:
            for n in range(random.randint(0,20)):
                ENEMY_X -= 1
        ENEMY_Y += ENEMY_SPEED

        # [POS] Give BULLIT a move
        BULL_Y -= 10
        if BULL_Y <= 10:
            BULL_X = x + (FIGHTER_WIDTH/2 - DICT_OBJ['bullit'][0]/2)
            BULL_Y = y



        DISPLAYSURF.fill(BLACK)
        draw_object(fighter, x, y)
        draw_object(bee, ENEMY_X, ENEMY_Y)
        draw_object(bullit, BULL_X, BULL_Y)

        pygame.display.update()
        FPS_CLK.tick(FPS)

    pygame.quit()
    sys.exit()

run_game()
