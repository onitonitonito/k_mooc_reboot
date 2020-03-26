"""
# app.py - (Temporary) PyAutoGui제어
"""
# https://www.pygame.org/wiki/SettingWindowPosition
# pag.moveTo(x=1877, y=1060)    # check!... (1st) 캘린더
# pag.moveTo(x=20, y=1060)      # check!... (1st) 윈도우 시작
# pag.moveTo(x=2490, y=15)      # check!... (2nd) CMD 85x80 @(0,0) [x]
# pag.moveTo(x=1895, y=20)      # check!... (1st) pygame 300x100 @(1620,40) [x]


import os
import sys
import time

from config_autogui import *

print(__doc__)


def main():
    """ 좌표체크(with 'SPACE') """
    global ttime_fire, ttime_prep

    # bang2(1) - procedure(1) - finish(1)+1
    for key in ['bang2', 'procedure', 'finish',]:
        print("{:10} = ({}, {})".format(key, *POS_XY[key][0]))

    set_basic_screen(WINDOW_SIZE,"TAP HERE!")
    display_message("TAP=SPACE!", 45, (10,30), PINK)
    pygame.display.update()

    print(f"* SCREEN_SIZE  : {pag.size()}") # Size(width=1920, height=1080)
    while 1:
        check_pointer_xy_coords()           # 스페이스바로 좌표체크


if __name__ == '__main__':
    main()
