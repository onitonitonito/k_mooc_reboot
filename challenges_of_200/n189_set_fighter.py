import os, sys, pygame
''' further development
        - encounter enemy and cross fire.
'''
DESTIN_DIR = os.path.dirname(__file__)+'/sprites/Galaga/'

BLACK = (0, 0, 0)
PAD_WIDTH = 480
PAD_HEIGHT = 640

# original size = (200x213) is transformed (36x38)
FIGHTER_WIDTH = 36
FIGHTER_HEIGHT = 38

DICT_OBJ = {
    'fighter'   : [36, 38, (PAD_WIDTH - 36)/2 , PAD_HEIGHT-(38+10), 'Ship_White.png'],
    'g_catcher' : [36, 38, 200, 100,'Green_Catcher.png'],
    'gremlin'   : [36, 38, 200, 150,'gremlin_0001.png'],
    'bee'       : [36, 38, 200, 200,'Fly_0001.png'],
    'scorpion'  : [36, 38, 200, 250,'scorpion_0001.png'],
    'pheonix'   : [36, 38, 200, 300,'pheonix_0001.png'],
    'bullit'    : [13, 22, 200, 550,'rocket_0001.png'],
}

DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
pygame.display.set_caption('My GALAXTICA~!!')
clock = pygame.time.Clock()

# draw object
def set_image(filename):
    return pygame.image.load(DESTIN_DIR + filename)

def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))

def draw_object(obj, x, y):
    DISPLAYSURF.blit(obj, (x, y))

def run_game():
    # initial POS of fighter
    x = PAD_WIDTH * 0.45                     # 45% start X-point
    y = PAD_HEIGHT - (FIGHTER_HEIGHT + 10)   # 95% start Y-point

    x_change = 0                             # not moving
    y_change = 0

    ongame = False

    while not ongame:
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

        # deploy fighter jet
        x += x_change
        y += y_change

        if x < 0:
            x = 0
        elif x > PAD_WIDTH - FIGHTER_WIDTH:
            x = PAD_WIDTH - FIGHTER_WIDTH

        if y < 0:
            y = 0
        elif y > PAD_HEIGHT - FIGHTER_HEIGHT:
            y = PAD_HEIGHT - FIGHTER_HEIGHT

        DISPLAYSURF.fill(BLACK)

        draw_object(fighter, x, y)
        draw_object(gremlin, DICT_OBJ['gremlin'][2], DICT_OBJ['gremlin'][3])
        draw_object(bee, DICT_OBJ['bee'][2], DICT_OBJ['bee'][3])
        draw_object(bullit, DICT_OBJ['bullit'][2], DICT_OBJ['bullit'][3])
        draw_object(scorpion, DICT_OBJ['scorpion'][2], DICT_OBJ['scorpion'][3])
        draw_object(pheonix, DICT_OBJ['pheonix'][2], DICT_OBJ['pheonix'][3])
        draw_object(g_catcher, DICT_OBJ['g_catcher'][2], DICT_OBJ['g_catcher'][3])


        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

def init_game():
    pygame.init()

    # fighter OBJ.image load
    if not pygame.image.get_extended():
        raise SystemExit('Sorry, Extended image is not available')

    # picture = pygame.transform.scale(picture, (1280, 720))


# for key, value in DICT_OBJ.items():
#     key = pygame.image.load(DESTIN_DIR+value[4])
#     key = pygame.transform.scale(key, (value[0], value[1]))      # Added


fighter = set_image(DICT_OBJ['fighter'][4])
fighter = set_size(fighter, DICT_OBJ['fighter'][0], DICT_OBJ['fighter'][1])

g_catcher = set_image(DICT_OBJ['g_catcher'][4])
g_catcher = set_size(g_catcher, DICT_OBJ['g_catcher'][0], DICT_OBJ['g_catcher'][1])

bee = set_image(DICT_OBJ['bee'][4])
bee = set_size(bee, DICT_OBJ['bee'][0], DICT_OBJ['bee'][1])

gremlin = set_image(DICT_OBJ['gremlin'][4])
gremlin = set_size(gremlin, DICT_OBJ['gremlin'][0], DICT_OBJ['gremlin'][1])

scorpion = set_image(DICT_OBJ['scorpion'][4])
scorpion = set_size(scorpion, DICT_OBJ['scorpion'][0], DICT_OBJ['scorpion'][1])

pheonix = set_image(DICT_OBJ['pheonix'][4])
pheonix = set_size(pheonix, DICT_OBJ['pheonix'][0], DICT_OBJ['pheonix'][1])

bullit = set_image(DICT_OBJ['bullit'][4])
bullit = set_size(bullit, DICT_OBJ['bullit'][0], DICT_OBJ['bullit'][1])

# boss = pygame.image.load(DESTIN_DIR+'Green_Catcher.png')
# boss = pygame.transform.scale(boss, (36,38))      # Added


init_game()
run_game()
