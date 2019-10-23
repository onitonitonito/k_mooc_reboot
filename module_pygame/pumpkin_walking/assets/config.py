"""
# ./assets/config.py - variable setting : configuration
"""
print(__doc__)

import os, sys
import pygame

# 폴더 구조관련 변수
dir_top = "_ing02_pumpkin_walking"
dir_array = os.path.dirname(__file__).partition(dir_top)
dir_root = "".join(dir_array[:2]) + "\\"

dir_assets = dir_root + "assets\\"
dir_statics = dir_root + "statics\\"
dir_images = dir_statics + "img\\"

# getting the pygame clock for handling fps
CLOCK = pygame.time.Clock()

# pygame 관련변수
FPS = 10                # Frames per second
START_POS = (0, 200)
WINDOW_SIZE = (WIDTH, HEIGHT) = (600, 400)
BACKGROUND_COLOR = pygame.Color('darkgray')

#               R       G       B
BLACK       = (   0,     0,   0)    #000000
WHITE       = ( 255,   255, 255)    #ffffff

DARKGRAY    = ( 90,    90,   90)    #5a5a5a
GRAY        = ( 185,   185, 185)    #b9b9b9

BRIGHTRED   = ( 255,   0,     0)    #ff0000
LIGHTRED    = ( 175,  20,    20)    #af1414
RED         = ( 155,   0,     0)    #9b0000

BRIGHTGREEN = ( 0,   255,     0)    #00ff00
LIGHTGREEN  = ( 20,  175,    20)    #14af14
GREEN       = ( 0,   155,     0)    #009b00

BRIGHTBLUE  = ( 0,      0,  255)    #0000ff
LIGHTBLUE   = (20,     20,  175)    #1414af
BLUE        = ( 0,      0,  155)    #00009b

BRIGHTYELLOW= ( 255,   255,   0)    #ffff00
LIGHTYELLOW = ( 175,   175,  20)    #afaf14
YELLOW      = ( 155,   155,   0)    #9b9b00
