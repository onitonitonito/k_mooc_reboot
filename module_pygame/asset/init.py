import os

# WORKING DIR. SET
DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1] + '\\'

# FILE IMG /W DIR.
FILE_IMG_LOGO = ROOT + '_static/pygame_sprites/mobygames_logo.png'
FILE_IMG_01 = ROOT + '_static/pygame_sprites/galaga_fighter.png'
FILE_IMG_02 = ROOT + '_static/pygame_sprites/galaga_pheo.png'
FILE_IMG_03 = ROOT + '_static/pygame_sprites/galaga_enter.png'

# SET INITIAL VARI.
SCREEN_SIZE = (480, 640)            # screen size = 480 x 640 default
BLACK = (0,0,0)     # fill black
FPS = 30

# FIGHTER'S POSITION
POS_X = (480-50)/2
POS_Y = (640-(53+20))

# KEY INCREASEMENT
X_MOVE = 0
Y_MOVE = 0
