"""
# config_autogui.py - 함수 및 변수들
"""
import os
import sys
import time
import random
import pygame
import pyautogui as pag

from pygame.locals import *
from datetime import datetime as dd

print(__doc__)

# BANG CLICK POS_XY
BANG_XY = (1403, 977)


POS_XY = {
    'calendar'  : [(1877 , 1060), 'calendar timer pop-up'],
    'start'     : [(21   , 1060), 'start button'],
    'pycmd'     : [(453 ,  273), 'python cmd'],
    'pytap'     : [(1901 , 14), 'pygame tap here - close[x]'],

    'bang1'     : [(1403 , 977), 'marked bang pos_xy'],
    'bang2'     : [(35 , 846), 'home idle icon'],
    'bang3'     : [(35 , 961), 'tree CIAD icon'],

    'win'       : [(22 , 1060), 'win-start button'],
    'off'       : [(26 , 1019), 'next, power-off button'],
    'sys-out'   : [(30 , 923), 'next, sys-out button'],

    'procedure' : [(1615, 506), 'proceed button'],
    'finish'    : [(1608, 580), 'finish check-button'],
}

# PYGAME WINDOW START! --> POS_XY[nw]
WINDOW_SIZE = (500,100)
WINDOW_START = (1400, 40)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{WINDOW_START[0]}, {WINDOW_START[1]}"


# PYGAME DISPLAYSURF SET
pygame.init()
DISPLAYSURF = pygame.display.set_mode((10,10))

# COLOR CODE
BG_COLOR = (31, 231, 231)   # rgb(31,231,231)
PINK = (252, 100, 196)      # rgb(252, 100, 196)
RED = (237, 17, 121)        # rgb(237, 17, 121)
BLUE = (61, 92, 224)        # rgb(61, 92, 224)
GREEN = (22, 172, 13)       # rgb(22, 172, 13)

# IDLE GOTO_XYS
GOTO_XYS = {
    'A' : (100,850),
    'B' : (250,850),
    'C' : (250,950),
    'D' : (100,950),
}


def main():
    pass

def get_prep_time(str_time_fire="00:00:00", minute_before=1):
    """ 2분 전 시간으로 준비시간(str)을 반환한다"""
    fires = str_time_fire.split(":")
    minut_prep = int(fires[1]) - minute_before
    if minut_prep < 0:
        minut_prep += 59
    return f"{fires[0]}:{minut_prep:02}:{fires[2]}"

def set_basic_screen(screen_size, caption="CAPTION HERE"):
    """set default window screen"""
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(screen_size)
    DISPLAYSURF.fill((244, 223, 35))
    pygame.display.set_caption(caption)

def display_message(text, size, posxy, font_color, delay_time=0):
    """HELPER(): for display_*() """
    textfont = pygame.font.Font("freesansbold.ttf", size)
    text = textfont.render(text, True, font_color)
    DISPLAYSURF.blit(text, posxy)



def event_prep(pos_xy, picks=['calendar',]):
    """ default = 1, 캘린더를 띄운다
    # pag.click(x=1877, y=1060, clicks=1)    # (1st) 캘린더
    # pag.click(x=20, y=1060, clicks=1)      # (1st) 윈도우 시작
    # pag.click(x=2490, y=15, clicks=1)      # (2nd) CMD 85x80 @(0,0) [x]
    # pag.click(x=1895, y=20, clicks=1)      # (1st) pygame 300x100 [x]
    """
    for pick in picks:
        pag.click(*pos_xy[pick][0], clicks=1)

    pag.moveTo(pos_xy['pycmd'][0],)   # (2nd)에서 대기
    print(f"-------------- {ttime_s}.{ttime_f} [PREP]▶", flush=True)

def event_bang(pos_xy):
    """
    # pag.click(x=3739, y=1115, clicks=3)   # (2nd) 의견추가버튼
    # pag.click(clicks=3, duration=0)       # (2nd) 확인버튼 - 1차
    # pag.doubleClick()                     # (2nd) 확인버튼 - 2차(랙대비)

    """

    """
    IF YOU WANT TO ADD RANDOM ADDITIONAL SURPLUS! ADD BELLOW
    """
    surplus_within_10 = random.randint(20,100) * 1/10
    time.sleep(surplus_within_10)

    # 메인 트리거 이벤트 - HERE!
    pag.click(*pos_xy['bang2'][0], clicks=1, duration=0.0)
    pag.click()

    # 나머지는 쓸데없는 데코레이션 이벤트
    print()
    print(f"-------------- {ttime_s}.{ttime_f} [BANG] ***", flush=True)
    print("\n")
    [print("RANG--rang--RANG---rang!!", flush=True) for i in range(3)]

    print()
    print(dd.now())
    """
    ADDITIONAL PROCEDURE ... FINISH BUTTON
    """
    print(f"--- ADDITIONAL PROCEDURES! ---")
    pag.click(*pos_xy['procedure'][0], clicks=1, duration=1)
    pag.click(*pos_xy['finish'][0], clicks=1, duration=1)
    pag.click()

    """
    IF YOU NEED DOOMS-DAY-PROGRAM, ACTIVATE BELOW!
    """
    print(f"--- DOMSDAY PROGRAM! ---")
    # pag.click(*pos_xy['win'][0], clicks=1, duration=1)
    # pag.click(*pos_xy['off'][0], clicks=1, duration=1)
    # pag.click(*pos_xy['sys-out'][0], clicks=1, duration=1)

    # https://stackoverflow.com/questions/34039845/
    # how-to-shutdown-a-computer-using-python
    # os.system('shutdown -s -t 3')
    sys.exit()

def is_trigger_time(ttime_fire, ttime_prep):
    """매초 00, 타임스탬프를 찍고, sec='00' 일때 클릭 이벤트를 실행"""
    if ttime_s == '00':
        if target_time == ttime_fire:
            event_bang(POS_XY)

        elif target_time == ttime_prep:
            event_prep(POS_XY)

        else:
            print(f"------------ {ttime_s}.{ttime_f}", flush=True)
    else:
        print(f"{target_time}.{ttime_f}", flush=True)

def get_set_trigger_time(ttime_fire, ttime_prep):
    """ 랙 때문에 어려움이 있다."""
    global target_time, ttime_h, ttime_m, ttime_s, ttime_f

    limit_time = 1000
    trigger = False

    while 1:
        time_now = dd.now()
        target_time = time_now.strftime("%H:%M:%S")

        ttime_h = target_time[-8:-6]
        ttime_m = target_time[-5:-3]
        ttime_s = target_time[-2:]
        ttime_f = time_now.strftime("%f")

        if (trigger == False) and int(ttime_f) < limit_time:
            is_trigger_time(ttime_fire, ttime_prep)
            trigger = True

        if ttime_f != dd.now().strftime("%f"):
            trigger=False

def check_pointer_xy_coords():
    """이벤트 키값에 대응하는 event_dict로 키 이벤트 입력 판단"""
    for event in pygame.event.get():

        event_dict = {
            'space': [(event.type == KEYDOWN and event.key == K_SPACE), ],
            'quit' : [
                    (event.type == QUIT),
                    (event.type == KEYDOWN and event.key == K_ESCAPE),
                ],
            }

        # show key-event on console
        """# IF - Keybinding State = keydown-stroke"""
        for key in event_dict.keys():

            if True in [*event_dict[key]]:    # 키-이벤트가 발생판단
                # print(f'----[{key.upper()}]----')  # for TEST

                if key == 'quit':
                    pygame.quit()
                    sys.exit()
                    break

                if key == 'space':
                    text_pos = str(pag.position())
                    print(text_pos)

                    DISPLAYSURF.fill((245, 236, 49))
                    display_message(text_pos, 40, (10,40), RED)
                    pygame.display.update()




if __name__ == '__main__':
    main()
