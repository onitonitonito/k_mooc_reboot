#! python
import os
import datetime

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

SEPARATOR = '\n' + '__'*30 + '\n\n'
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
    ]
AMPM_ARR = [
    [
    'ooo....',
    'o..o...',
    'ooo....',
    'o....o.',
    'o....o.',],
    [
    '.oo....',
    'o..o...',
    'oooo...',
    'o..o.o.',
    'o..o.o.',],
    ]



def show_digit_arr(_arr_n, change_flag=1):
    for n in range(5):
        if change_flag == 0:
            print(_arr_n[n].replace('.',' '))
        else:
            print(_arr_n[n].replace('o','■').replace('.','∴'))
    print()

# show_digit_arr(SYMBOL_ARR[0])
# show_digit_arr(SYMBOL_ARR[1])
# show_digit_arr(SYMBOL_ARR[2])
# show_digit_arr(SYMBOL_ARR[3])
# show_digit_arr(NUM_ARR[1])
# show_digit_arr(NUM_ARR[2])
# show_digit_arr(NUM_ARR[3])

def get_mixed_2_digit_arr(_arr_n1, _arr_n2, change_flag=1):
    mixed_arr = []
    for n in range(5):
        mixed_arr.append(_arr_n1[n] + _arr_n2[n])
    return mixed_arr

def show_digital_watch(apm_hour_minute_sec_str):
    """ apm_hour_minute_sec_str = 'am 10 27 54'
      - break 'str' into apm('int' 0 or 1), hr_str, min_str, sec_str
      - show unchanged & replaced version both
      - refresh screen every 1 second!
    """
    watch_arr = apm_hour_minute_sec_str.strip().split()
    print(watch_arr)

    if watch_arr[0].lower == 'am':
        apm = 0
    else:
        apm = 1

    hr_str = watch_arr[1]
    min_str = watch_arr[2]
    sec_str = watch_arr[3]

    _0_arr = get_mixed_2_digit_arr(AMPM_ARR[apm], SYMBOL_ARR[0])

    _1_arr = get_mixed_2_digit_arr(_0_arr, NUM_ARR[int(hr_str[0])])
    _2_arr = get_mixed_2_digit_arr(_1_arr, NUM_ARR[int(hr_str[1])])
    _3_arr = get_mixed_2_digit_arr(_2_arr, SYMBOL_ARR[1])
    _4_arr = get_mixed_2_digit_arr(_3_arr, SYMBOL_ARR[0])

    _5_arr = get_mixed_2_digit_arr(_4_arr, NUM_ARR[int(min_str[0])])
    _6_arr = get_mixed_2_digit_arr(_5_arr, NUM_ARR[int(min_str[1])])
    _7_arr = get_mixed_2_digit_arr(_6_arr, SYMBOL_ARR[1])
    _8_arr = get_mixed_2_digit_arr(_7_arr, SYMBOL_ARR[0])

    _9_arr = get_mixed_2_digit_arr(_8_arr, NUM_ARR[int(sec_str[0])])
    _10_arr = get_mixed_2_digit_arr(_9_arr, NUM_ARR[int(sec_str[1])])

    print('\n\n')
    show_digit_arr(_10_arr,0)
    print('\n\n')

    _1_arr = get_mixed_2_digit_arr(AMPM_ARR[apm], NUM_ARR[int(hr_str[0])])
    _2_arr = get_mixed_2_digit_arr(_1_arr, NUM_ARR[int(hr_str[1])])
    _3_arr = get_mixed_2_digit_arr(_2_arr, SYMBOL_ARR[1])
    _4_arr = get_mixed_2_digit_arr(_3_arr, NUM_ARR[int(min_str[0])])
    _5_arr = get_mixed_2_digit_arr(_4_arr, NUM_ARR[int(min_str[1])])
    show_digit_arr(_5_arr,1)

    _1_arr = get_mixed_2_digit_arr(SYMBOL_ARR[0], SYMBOL_ARR[0])
    # _2_arr = get_mixed_2_digit_arr(_1_arr, SYMBOL_ARR[0])
    # _3_arr = get_mixed_2_digit_arr(_2_arr, SYMBOL_ARR[0])
    _2_arr = get_mixed_2_digit_arr(_1_arr, NUM_ARR[int(sec_str[0])])
    _3_arr = get_mixed_2_digit_arr(_2_arr, NUM_ARR[int(sec_str[0])])
    show_digit_arr(_3_arr,1)



show_digital_watch('am 10 27 54')
