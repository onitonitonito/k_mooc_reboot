"""
# app.py - (Temporary) PAG Idle control
"""
# https://www.pygame.org/wiki/SettingWindowPosition

import sys
import time
import pygame


from config_autogui import *

print(__doc__)

DURATION = 0.6    # 0.6
TIME_SLEEP = 3    # 3

def main():
    """입력받기: 1=좌표체크(with 'SPACE') / ENTER=타이머 설정! """
    global ttime_fire, ttime_prep

    print(f"* SCREEN_SIZE   : {pag.size()}")
    print(f"* WINDIW POS_NW : X={WINDOW_START[0]}, Y={WINDOW_START[1]}")
    print(f"* IDLE POS_XY   : {list(GOTO_XYS.values())}")
    print(f"* PRESENT TIME  : {dd.now().strftime('%H:%M:%S')} \n\n\n")

    set_basic_screen(screen_size=WINDOW_SIZE, caption="HI~!")
    display_message(text='TAP HERE!', size=50, posxy=(30,30), font_color=RED)
    pygame.display.update()

    while True:
        for i in range(4):
            print()
            for idx in GOTO_XYS:
                pag.moveTo(*GOTO_XYS[idx], DURATION)
                print(f"{idx}!", flush=True, end='')
                time.sleep(TIME_SLEEP)

        pag.click(clicks=1, duration=0)
        print("\t...", dd.now().strftime("%H:%M:%S"), " [CLICK!]")


if __name__ == '__main__':
    main()
