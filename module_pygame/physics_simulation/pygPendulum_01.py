""" funny pendulum dynamics / school science
refer : scientific information blog - https://goo.gl/Aicg6K
refer : about Galileo Galilei NamuWiki = https://goo.gl/H3H8ho
"""
import os
import sys
import pygame
import numpy as np
from pygame.locals import *

# COLOR TABLE
RED =   (250, 0,    0)      #fa0000
GREEN = (0,   250,  0)      #00fa00
BLUE =  (0,   0,    250)    #0000fa
GRAY =  (155, 155,  155)    #9b9b9b
WHITE = (255, 255,  255)    #000000

DESTIN_DIR = os.path.join(os.path.dirname(__file__),'statics', 'img\\')
FPSCLOCK = pygame.time.Clock()

h = 0.05                # time increasement (sec)
t = v = 0               # time & velocity (sec, m/sec)
x = 90 * np.pi / 180    # 30 degree * PI() / 180

pen_fm = 0.01           # fm =
pen_m = 0.1             # m = mass (kg)
pen_l = 100 * 0.01      # l = length of string (m)
pen_J = 0.02            # j =
pen_g = 9.8             # g = acceleration of Gravity (m/sec**2)

gndCenterX = 150        # tied positon (center = 300 / 2)
gndCenterY = 20         # Margin of Ceiling = 20 px.
penLength = pen_l * 100 * 2 # length of string = multiple 100 times for ANIM.

def calcODEFunc(tVal, xVal, vVal):
    """ Dynamic Mechanics of ODE (Ordinary Differential Equation) function """
    return -pen_fm/(pen_m*pen_l*pen_l+pen_J)*vVal-pen_m*pen_g*pen_l/(pen_m*pen_l**2+pen_J)*xVal

def solveODEusingRK4(t, x, v):
    """ ODE(Ordinary Differential Equation for Runge Kutta 4th Order """
    kx1 = v
    kv1 = calcODEFunc( t, x, v )

    kx2 = v + h*kv1/2
    kv2 = calcODEFunc( t + h/2, x + h*kx1/2, v + h*kv1/2 )

    kx3 = v + h*kv2/2
    kv3 = calcODEFunc( t + h/2, x + h*kx2/2, v + h*kv2/2 )

    kx4 = v + h*kv3
    kv4 = calcODEFunc( t + h, x + h*kx3, v + h*kv3 )

    dx = h*(kx1 + 2*kx2 + 2*kx3 + kx4)/6
    dv = h*(kv1 + 2*kv2 + 2*kv3 + kv4)/6

    return x+dx, v+dv

def set_image(filename):
    return pygame.image.load(DESTIN_DIR + filename)

def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))

def set_object(obj, x, y):
    DISPLAYSURF.blit(obj, (x, y))

def terminate():
    print('\tPROGRAM IS TERMINATED!!....')
    pygame.quit()
    sys.exit()

pygame.init()

FONT_BIG = pygame.font.SysFont('Vernada.ttf', 30)
FONT_MID = pygame.font.SysFont('Vernada.ttf', 22)

DISPLAYSURF = pygame.display.set_mode((300, 550)) # display MODE = 300 x 300
pygame.display.set_caption('MY PENDULUM~!!')

FONTSURF_01 = FONT_BIG.render('PENDULUM Simulation', True, BLUE)
FONTSURF_02 = FONT_MID.render('  (by using ODE RK4 - function)', True, RED)

imgEquation = set_size(set_image('img_ode_rk4_eq.jpg'), 250, 65)
imgSketch = set_size(set_image('img_pendulum.jpg'), 330, 200)

loopFlag = True

while loopFlag:
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        elif event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            elif event.key == K_SPACE:
                h = 0.05                # time increasement (sec)
                t = v = 0               # time & velocity (sec, m/sec)
                x = 90 * np.pi / 180    # 30 degree * PI() / 180

                pen_fm = 0.01           # fm =
                pen_m = 0.1             # m = mass (kg)
                pen_l = 100 * 0.01      # l = length of string (m)
                pen_J = 0.02            # j =
                pen_g = 9.8             # g = acceleration of Gravity (m/sec**2)

                gndCenterX = 150        # tied positon (center = 300 / 2)
                gndCenterY = 20         # Margin of Ceiling = 20 px.
                penLength = pen_l * 100 * 2 # length of string = multiple 100 times for ANIM.

    DISPLAYSURF.fill(WHITE)             # fill up with WHITE
    FONTSURF_03 = FONT_MID.render('SPACE to restart            TIME: %3.2f Sec.'%t, True, GRAY)

    t += h
    [x, v] = solveODEusingRK4(t,x,v)
    print("t = %3.2f sec / x = %1.3f / v = %3.3f" %(t,x,v))


    updatedX = gndCenterX + penLength*np.sin(x)
    updatedY = gndCenterY + penLength*np.cos(x)

    pygame.draw.line(DISPLAYSURF, BLUE, (gndCenterX, gndCenterY), (updatedX, updatedY), 2)
    pygame.draw.circle(DISPLAYSURF, RED, (int(updatedX), int(updatedY)), 12, 0)
    pygame.draw.line(DISPLAYSURF, GRAY, (10,12), (290,12), 15)

    DISPLAYSURF.blit(FONTSURF_03, (10,30))      # time : 00 sec.
    DISPLAYSURF.blit(FONTSURF_01, (10,230))     # Title = PENDULUM Simulation
    DISPLAYSURF.blit(FONTSURF_02, (10,250))     # Description

    set_object(imgEquation, 0, 270)
    set_object(imgSketch, 20, 335)

    # pygame.time.delay(40)
    # pygame.display.flip()

    pygame.display.update()
    FPSCLOCK.tick(30)                          # FPS=30

# refer to : http://pinkwink.kr/683 [PinkWink]
# Youtube : https://youtu.be/pYx66DwWbk8 : PENDULUM Simulation
