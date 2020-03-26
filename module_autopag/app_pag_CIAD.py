"""
# pag.py - HOWDY! Call It a Day!
 - and I, I always call it a da~e~e~~e~y~..
"""
# https://www.pygame.org/wiki/SettingWindowPosition


import os
import sys

from config_autogui import *

print(__doc__)

def main():
    """ ENTER=타이머 설정! """
    # global ttime_fire, ttime_prep

    time_input = f"\n\n 타겟시간입력: (예)'{str(dd.now())[-16:-7]}'   : "
    ttime_fire = input(time_input)     # 이벤트 클릭 시간!
    ttime_prep = get_prep_time(str_time_fire=ttime_fire, minute_before=1)

    print(f"* CURRENT TIME : {dd.now()}")
    print(f"* PREPERATION_TIME        = {ttime_prep}")
    print(f"* ACTIVATE_TIME_TRIGGER   = {ttime_fire} ***", "\n\n")

    # bang2(1) - procedure(1) - finish(1)+1
    for key in ['bang2', 'procedure', 'finish',]:
        print("{:10} = ({}, {})".format(key, *POS_XY[key][0]))


    while 1:
        get_set_trigger_time(ttime_fire, ttime_prep)




if __name__ == '__main__':
    main()
