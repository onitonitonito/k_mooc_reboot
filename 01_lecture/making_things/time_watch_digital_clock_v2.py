#! python
import io
import sys
""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import time
import datetime

NUM_ARR = [
    [
    '.ooooo.',
    'oo..oo.',
    'oo..oo.',
    'oo..oo.',
    'ooooo..',],
    [
    '..oo...',
    'oooo...',
    '..oo...',
    '..oo...',
    'oooooo.',],
    [
    '.ooooo.',
    'o...oo.',
    '..ooo..',
    'ooo....',
    'oooooo.',],
    [
    '.ooooo.',
    '....oo.',
    '.oooo..',
    '...ooo.',
    'ooooo..',],
    [
    '...oo..',
    '.oo.o..',
    'oo..o..',
    'oooooo.',
    '....o..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    [
    '.ooooo.',
    'oo.....',
    'oooooo.',
    'oo..oo.',
    '.oooo..',],
    [
    'oooooo.',
    'o...oo.',
    '...oo..',
    '..oo...',
    '.oo....',],
    [
    '.ooooo.',
    'oo..oo.',
    '.oooo..',
    'oo..oo.',
    '.oooo..',],
    [
    '.ooooo.',
    'oo...o.',
    'oooooo.',
    '....oo.',
    'ooooo..',],
    ]
SYMBOL_ARR = [
    [
    '...',
    '...',
    '...',
    '...',
    '...',],
    [
    'oo.',
    'oo.',
    '...',
    'oo.',
    'oo.',],
    [
    'ooo...',
    '.o..o.',
    '..o..o',
    '.ooo..',
    'ooo...',],
    ]
AMPM_ARR = [
    [
    '.oo.....',
    'o..o....',
    'oooo....',
    'o..o.oo.',
    'o..o.oo.',],
    [
    'ooo.....',
    'o..o....',
    'ooo.....',
    'o....oo.',
    'o....oo.',],
    ]
CONTROL_DICT = {
    '0' : NUM_ARR[0],
    '1' : NUM_ARR[1],
    '2' : NUM_ARR[2],
    '3' : NUM_ARR[3],
    '4' : NUM_ARR[4],
    '5' : NUM_ARR[5],
    '6' : NUM_ARR[6],
    '7' : NUM_ARR[7],
    '8' : NUM_ARR[8],
    '9' : NUM_ARR[9],
    '_' : SYMBOL_ARR[0],
    ':' : SYMBOL_ARR[1],
    '~~' : SYMBOL_ARR[2],
    'a' : AMPM_ARR[0],
    'p' : AMPM_ARR[1],
    }

def show_1_digit_arr(_arr_n, change_flag=1):
    for n in range(5):
        if change_flag == 0:
            print(_arr_n[n].replace('.',' '))
        else:
            print(_arr_n[n].replace('o','■').replace('.','∴'))
    print()

def get_multi_mixed_arr(*arr_names):
    multi_arr = ['', '', '', '', '']
    for name in arr_names:
        multi_arr[0] += name[0]
        multi_arr[1] += name[1]
        multi_arr[2] += name[2]
        multi_arr[3] += name[3]
        multi_arr[4] += name[4]
    return multi_arr

def show_digital_watch(apm_hr_min_sec_str):
    """ apm_hr_min_sec_str = 'am 10 27 54'
      - break 'str' into apm('int' 0 or 1), hr_str, min_str, sec_str
      - show unchanged & replaced version both
      - refresh screen every 1 second!
    """
    time_arr = apm_hr_min_sec_str.strip().split()

    apm = time_arr[0].lower()[0]   # 'str' = 'AM'/'PM' --> 'a' or 'p'
    hr_str = time_arr[1]           # 'str' = '10'
    min_str = time_arr[2]          # 'str' = '27'
    sec_str = time_arr[3]          # 'str' = '54'

    """ to make Recursive function or yield is much simpler LATER! """
    print('\n\n\n')
    _a_arr = get_multi_mixed_arr(
        CONTROL_DICT[apm],
        CONTROL_DICT['_'],
        CONTROL_DICT[hr_str[0]],
        CONTROL_DICT[hr_str[1]],
        CONTROL_DICT[':'],
        CONTROL_DICT['_'],
        CONTROL_DICT[min_str[0]],
        CONTROL_DICT[min_str[1]],
        CONTROL_DICT[':'],
        CONTROL_DICT['_'],
        CONTROL_DICT[sec_str[0]],
        CONTROL_DICT[sec_str[1]],
        )
    show_1_digit_arr(_a_arr, 0)

    print('\n\n')
    _b_arr = get_multi_mixed_arr(
        CONTROL_DICT[apm],
        CONTROL_DICT[hr_str[0]],
        CONTROL_DICT[hr_str[1]],
        CONTROL_DICT[':'],
        CONTROL_DICT[min_str[0]],
        CONTROL_DICT[min_str[1]],
        )
    show_1_digit_arr(_b_arr, 1)

    _c_arr = get_multi_mixed_arr(
        CONTROL_DICT['_'],
        CONTROL_DICT['~~'],
        CONTROL_DICT['_'],
        CONTROL_DICT['_'],
        CONTROL_DICT[sec_str[0]],
        CONTROL_DICT[sec_str[1]],
        )
    show_1_digit_arr(_c_arr, 1)

def main():
    _time = datetime.datetime.now()

    ampm = _time.strftime('%p')     # AM, PM
    hour = _time.strftime('%I')     # 07
    minute = _time.strftime('%M')   # 01
    second = _time.strftime('%S')   # 01
    weekday = _time.strftime('%A')  # MONDAY

    print(_time, end='   ....  ')

    apm_hr_min_sec_str = \
        ampm + ' ' + \
        hour + ' ' + \
        minute + ' '+\
        second
    print(apm_hr_min_sec_str + '  : ' + weekday)

    # show_digital_watch('am 10 27 54')
    show_digital_watch(apm_hr_min_sec_str)


if __name__ == '__main__':
    while True:
        main()

        sys.stdout.flush()
        time.sleep(1)
        os.system('cls')
