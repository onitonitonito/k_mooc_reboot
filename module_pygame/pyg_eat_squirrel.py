"""
# REFER HERE: https://inventwithpython.com/pygame/chapter8.html
# Invert with Python part-2 (with pygame)
"""
print(__doc__)

import math
import time
import random
import pygame

from pygame.locals import *   # K_bind, Const, color, button & keymap etc.
from _config_general import *


DESTIN_DIR = ROOT + "/statics/img/"

FPS = 30                # Frames Per Second

WINDOWWIDTH = 640       # 640 x 480 px SCREEN WINDOW
WINDOWHEIGHT = 480

HALF_WINWIDTH = int(WINDOWWIDTH / 2)        # 640/2= 320
HALF_WINHEIGHT = int(WINDOWHEIGHT / 2)      # 480/2= 240

GRASS_COLOR = (24, 255, 0)
# WHITE & RED were assigned already.

CAMERA_SLACK = 90   # how far squirrel's away from center, when move cam.
MOVE_RATE = 9       # player speed
BOUNCE_RATE = 6     # player jumping speen (the bigger the slower)
BOUNCE_HEIGHT = 30  # player jumping height (pixel)

START_SIZE = 25     # default size = 25
WIN_SIZE = 300      # victor's size
INVUL_TIME = 2      # invulnerable seconds when crashed(reset)

GAMEOVER_TIME = 4   # seconds show 'GAMEOVER'
MAX_HEALTH = 3      # lives
NUM_GRASS = 80      # number of glass in activated area
NUM_SQUIRRELS = 30  #
MAX_SPEED = 7
MIN_SPEED = 3

DIR_CHANGE_FREQ = 2 # (%)rate = chance to turn in frames
LEFT = 'left'
RIGHT = 'right'

''' there are 3 classes = player, enemy, glass and each one has DICT structure
 REFER HERE: https://inventwithpython.com/pygame/chapter8.html
 (1) PLAYER
    - Surface:
    - facing:
    - size:
    - bounce:
    - health:

 (2) ENEMY
    - Surface:
    - movex / movey:
    - width / height:
    - bounce: / ..rate / ..height

 (3) GRASS
    - GrassImage :
'''

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASS_IMGS

    pygame.init()

    # Game window parameter
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_icon(pygame.image.load(DESTIN_DIR + 'gameicon.png'))
    pygame.display.set_caption('SQUIRREL EATER')

    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    # LOAD IMAGE FILE
    L_SQUIR_IMG = pygame.image.load(DESTIN_DIR + 'squirrel.png')
    R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)

    GRASS_IMGS = []
    for n in range(1, 5):
        GRASS_IMGS.append(pygame.image.load(DESTIN_DIR + 'grass%s.png' % n) )
    # print(GRASS_IMGS); quit()         # for TEST

    while True:
        run_game()

def run_game():
    invulnerable_mode = False
    invulnerable_start_time = 0

    gameover_mode = False
    gameover_start_time = 0
    win_mode = False

    # 'GAMEOVER' Surf Parameters
    gameover_surf = BASICFONT.render('Game Over', True, WHITE)
    gameover_rect = gameover_surf.get_rect()
    gameover_rect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    #'Restart' Surf Parameters
    win_surf1 = BASICFONT.render('(Press "r" to restart.)', True, WHITE)
    win_rect1 = win_surf1.get_rect()
    win_rect1.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 30)

    # 'Clear All Stages' Parameters
    win_surf2 = BASICFONT.render('You\'ve achieved OMEGA SQUIRREL!! ', True, WHITE)
    win_rect2 = win_surf2.get_rect()
    win_rect2.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

    #
    camerax = 0
    cameray = 0

    grass_objs = []      #
    squirrel_objs = []   #
    player_obj = {
        'surface': pygame.transform.scale(L_SQUIR_IMG, (START_SIZE, START_SIZE)),
        'facing'    : LEFT ,
        'size'      : START_SIZE,
        'x'         : HALF_WINWIDTH,
        'y'         : HALF_WINHEIGHT,
        'bounce'    : 0,
        'health'    : MAX_HEALTH
        }

    move_left   = False
    move_right  = False
    move_up     = False
    move_down   = False

    # randomly place grass image
    for n in range(10):
        grass_objs.append(make_new_grass(camerax,cameray))
        grass_objs[n]['x'] = random.randint(0, WINDOWWIDTH)
        grass_objs[n]['y'] = random.randint(0, WINDOWWIDTH)

    while True:
        # check invul_mode on/off
        if invulnerable_mode and time.time() - invulnerable_start_time > INVUL_TIME:
            invulnerable_mode = False

        # move squirrel_objs
        for s_obj in squirrel_objs:
            s_obj['x'] += s_obj['movex']
            s_obj['y'] += s_obj['movey']
            s_obj['bounce'] += 1

            # reset bounce when exceed bounce_rate
            if s_obj['bounce'] > s_obj['bounce_rate']:
                s_obj['bounce'] = 0

            # turn randomly
            if random.randint(0, 99) < DIR_CHANGE_FREQ:
                s_obj['movex'] = get_random_velocity()
                s_obj['movey'] = get_random_velocity()
                # turn face left-right
                if s_obj['movex'] > 0:
                    s_obj['surface'] = pygame.transform.scale(R_SQUIR_IMG,
                    (s_obj['width'],s_obj['height']))
                else:
                    s_obj['surface'] = pygame.transform.scale(L_SQUIR_IMG,
                    (s_obj['width'],s_obj['height']))

        # check which instance will be eliminated
        for n in range(len(grass_objs)-1, -1, -1):
            if is_outside_acitve_area(camerax, cameray, grass_objs[n]):
                del grass_objs[n]

        for n in range(len(squirrel_objs)-1, -1, -1):
            if is_outside_acitve_area(camerax, cameray, squirrel_objs[n]):
                del squirrel_objs[n]

        # if insurficiant in num_grass,squirrel, CREATE
        while len(grass_objs) < NUM_GRASS:
            grass_objs.append(make_new_grass(camerax,cameray))

        while len(squirrel_objs) < NUM_SQUIRRELS:
            squirrel_objs.append(make_new_squirrel(camerax,cameray))

        # if out of CAMERA_SLACK, adjust again
        player_centerx = player_obj['x'] + int(player_obj['size'] / 2)
        player_centery = player_obj['y'] + int(player_obj['size'] / 2)

        if (camerax + HALF_WINWIDTH) - player_centerx > CAMERA_SLACK:
            camerax = player_centerx + CAMERA_SLACK - HALF_WINWIDTH

        elif player_centerx - (camerax + HALF_WINWIDTH) > CAMERA_SLACK:
            camerax = player_centerx - CAMERA_SLACK - HALF_WINWIDTH

        if (cameray + HALF_WINHEIGHT) - player_centery > CAMERA_SLACK:
            cameray = player_centery + CAMERA_SLACK - HALF_WINHEIGHT

        elif player_centery - (cameray + HALF_WINHEIGHT) > CAMERA_SLACK:
            cameray = player_centery - CAMERA_SLACK - HALF_WINHEIGHT

        # 181- draw green screed
        DISPLAYSURF.fill(GRASS_COLOR)

        # 184- draw all grass objects
        for g_obj in grass_objs:
            g_rect = pygame.Rect((
                g_obj['x'] - camerax,
                g_obj['y'] - cameray,
                g_obj['width'],
                g_obj['height']
                ))
            DISPLAYSURF.blit(GRASS_IMGS[g_obj['grass_image']], g_rect)

        # 193- draw other squirrels
        for s_obj in squirrel_objs:
            s_obj['rect'] = pygame.Rect((
                s_obj['x'] - camerax,
                s_obj['y'] - cameray - get_bounce_amount(
                    s_obj['bounce'], s_obj['bounce_rate'],s_obj['bounce_height']),
                s_obj['width'],
                s_obj['height']))

            DISPLAYSURF.blit(s_obj['surface'], s_obj['rect'])

        # 202 - draw players squirrel
        flash_is_on = round(time.time(), 1) * 10 % 2 == 1

        if not gameover_mode and not(invulnerable_mode and flash_is_on):
            player_obj['rect'] = pygame.Rect((
                player_obj['x'] - camerax,
                player_obj['y'] - cameray - get_bounce_amount(
                    player_obj['bounce'], BOUNCE_RATE, BOUNCE_HEIGHT),
                player_obj['size'],
                player_obj['size']))

        DISPLAYSURF.blit(player_obj['surface'], player_obj['rect'])

        # 212- draw HEALTH METER
        draw_health_meter(player_obj['health'])

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    move_up = True
                    move_down = False

                elif event.key in (K_DOWN, K_s):
                    move_up = False
                    move_down = True

                elif event.key in (K_LEFT, K_a):
                    move_left = True
                    move_right = False

                    if player_obj['facing'] != LEFT:
                        player_obj['surface'] = pygame.transform.scale(
                            L_SQUIR_IMG, (
                                player_obj['size'], player_obj['size'])
                        )
                        player_obj['facing'] = LEFT

                elif event.key in (K_RIGHT, K_d):
                    move_left = False
                    move_right = True

                    if player_obj['facing'] != RIGHT:
                        player_obj['surface'] = pygame.transform.scale(
                            R_SQUIR_IMG, (
                                player_obj['size'], player_obj['size'])
                        )
                        player_obj['facing'] = RIGHT
                elif win_mode and event.key == K_r:
                    return

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    move_left = False

                elif event.key in (K_RIGHT, K_d):
                    move_right = False

                elif event.key in (K_UP, K_w):
                    move_up = False

                elif event.key in (K_DOWN, K_s):
                    move_down = False

                elif event.key == K_ESCAPE:
                    terminate()

        if not gameover_mode:
            # 256- move player_obj
            if move_left:
                player_obj['x'] -= MOVE_RATE

            elif move_right:
                player_obj['x'] += MOVE_RATE

            elif move_up:
                player_obj['y'] -= MOVE_RATE

            elif move_down:
                player_obj['y'] += MOVE_RATE

            if (move_left or move_right or move_up or move_down) or\
             player_obj['bounce'] != 0:
                player_obj['bounce'] += 1

            if player_obj['bounce'] > BOUNCE_RATE:
                player_obj['bounce'] = 0    # 270 - reset bounce

            # 272- check player_obj crushed into ENEMY
            for n in range(len(squirrel_objs)-1, -1, -1):
                s_obj = squirrel_objs[n]

                if 'rect' in s_obj and\
                 player_obj['rect'].colliderect(s_obj['rect']):
                 # 276- collided into ENEMY
                    if s_obj['width'] * s_obj['height'] <= player_obj['size']**2:
                        # 279- player eat ENEMY cuz, bigger

                        player_obj['size'] += int((s_obj['width']*s_obj['height'])**0.2) + 1
                        del squirrel_objs[n]

                        if player_obj['facing'] == LEFT:
                            player_obj['surface'] = pygame.transform.scale(
                                L_SQUIR_IMG, (player_obj['size'], player_obj['size'])
                            )
                        if player_obj['facing'] == RIGHT:
                            player_obj['surface'] = pygame.transform.scale(
                                R_SQUIR_IMG, (player_obj['size'], player_obj['size'])
                            )
                        if player_obj['size'] > WIN_SIZE:
                            win_mode = True

                    elif not invulnerable_mode:
                        # 292- player damaged by ENEMY cuz, smaller
                        invulnerable_mode = True
                        invulnerable_start_time = time.time()
                        player_obj['health'] -= 1

                        if player_obj['health'] == 0:
                            gameover_mode = True
                            gameover_start_time = time.time()

        else:
            # 300- Show 'GAMEOVER' Title
            DISPLAYSURF.blit(gameover_surf, gameover_rect)
            if time.time() - gameover_start_time > GAMEOVER_TIME:   # >4
                return                  # 300- end of game

        # 305- check player's victory
        if win_mode:
            DISPLAYSURF.blit(win_surf2,win_rect2)   # get OMEGA SQUIRREL!
            DISPLAYSURF.blit(win_surf1,win_rect1)   # press 'r'

        pygame.display.update()
        FPSCLOCK.tick(FPS)                          # FPS=30

def draw_health_meter(current_health):
    for n in range(current_health):     # draw life bars
        pygame.draw.rect(
            DISPLAYSURF,
            RED, (
            # x1,y1,x2,y2
                15, 5 + (10 * MAX_HEALTH) - n * 10,
                20, 10
                ))

    for n in range(MAX_HEALTH):         # draw WHITE border
        pygame.draw.rect(
            DISPLAYSURF,
            WHITE, (
            # x1,y1,x2,y2
                15, 5 + (10 * MAX_HEALTH) - n * 10,
                20, 10
                ),
            1)

def terminate():
    pygame.quit()
    sys.exit()

def get_bounce_amount(current_bounce, bounce_rate, bounce_height):
    # return pixel height
    # bounce_rate = the bigger the slower
    # bounce_height = the bigger the higher
    # 332- {current_bounce} is always smaller than {bounce_rate}
    height = int(math.sin((math.pi / float(bounce_rate)) * current_bounce) * bounce_height)
    return height

def get_random_velocity():
    speed = random.randint(MIN_SPEED, MAX_SPEED)    # 3 ~ 7 / -3 ~ -7
    if random.randint(0,10) % 2 == 1:
        return speed
    else:
        return -speed

def get_random_off_camera_POS(camerax, cameray, obj_width, obj_height):
    # create camera_view RECT
    camera_rect = pygame.Rect(
        camerax, cameray,
        WINDOWWIDTH, WINDOWHEIGHT)

    while True:
        x = random.randint(camerax - WINDOWWIDTH, camerax + (2 * WINDOWWIDTH))
        y = random.randint(cameray - WINDOWHEIGHT, cameray + (2 * WINDOWHEIGHT))
        # 349- randomly create RECT obj.
        # colliderect() and check right border is within screen

        obj_rect = pygame.Rect(x, y, obj_width, obj_height)
        if not obj_rect.colliderect(camera_rect):
            return x, y

def make_new_squirrel(camerax, cameray):
    general_size = random.randint(5, 25)    # default max = 25
    multipier = random.randint(1, 20)        # default max = 3

    sq = {}
    sq['width'] = (general_size + random.randint(0,10) * multipier)
    sq['height'] = (general_size + random.randint(0,10) * multipier)
    sq['x'], sq['y'] = get_random_off_camera_POS(
        camerax, cameray, sq['width'], sq['height'])

    sq['movex'] = get_random_velocity()     # get +_3 ~ +_7
    sq['movey'] = get_random_velocity()

    if sq['movex'] < 0:
        sq['surface'] =  pygame.transform.scale(L_SQUIR_IMG, (sq['width'], sq['height']))
    else:
        sq['surface'] =  pygame.transform.scale(R_SQUIR_IMG, (sq['width'], sq['height']))

    sq['bounce'] = 0
    sq['bounce_rate'] = random.randint(10, 18)
    sq['bounce_height'] = random.randint(10, 50)
    return sq

def make_new_grass(camerax, cameray):
    # return gr_dict on (camerax, cameray)
    gr = {}
    gr['grass_image'] = random.randint(0, len(GRASS_IMGS) - 1)
    gr['width'] = GRASS_IMGS[0].get_width()
    gr['height'] = GRASS_IMGS[0].get_height()
    gr['x'], gr['y'] = get_random_off_camera_POS(
                            camerax, cameray, gr['width'], gr['height'])
    gr['rect'] = pygame.Rect((gr['x'], gr['y'], gr['width'], gr['height']))
    return gr

def is_outside_acitve_area(camerax, cameray, obj):
    # 386- camerax, cameray coordination cross the border
    # and exceed half of windiw width, return False
    border_left = camerax - WINDOWWIDTH
    border_top = cameray - WINDOWHEIGHT
    border_rect = pygame.Rect(
        border_left, border_top,
        WINDOWWIDTH * 3, WINDOWHEIGHT * 3)

    obj_rect = pygame.Rect(
        obj['x'], obj['y'], obj['width'], obj['height'])

    return not border_rect.colliderect(obj_rect)


if __name__ == '__main__':
    main()
