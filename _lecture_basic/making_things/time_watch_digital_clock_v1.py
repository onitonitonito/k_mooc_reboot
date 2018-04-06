#! python
import os
import time
import datetime
""" """

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
    '.oo....',
    'o..o...',
    'oooo...',
    'o..o.o.',
    'o..o.o.',],
    [
    'ooo....',
    'o..o...',
    'ooo....',
    'o....o.',
    'o....o.',],
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
    'a' : AMPM_ARR[0],
    'p' : AMPM_ARR[1],
    }

def show_1_digit_of(arr_name, change_flag=1):
    for n in range(5):
        if change_flag == 1:
            print(arr_name[n].replace('o','■').replace('.','∴'))
        else:
            print(arr_name[n].replace('.',' '))
    print()

def get_2_mixed_arr(num_arr_1, num_arr_2):
    mixed_arr = []
    for n in range(5):
        mixed_arr.append(num_arr_1[n] + num_arr_2[n])
    return mixed_arr

def get_multi_mixed_arr(*arr_names):
    multi_arr = ['', '', '', '', '']
    for name in arr_names:
        multi_arr[0] += name[0]
        multi_arr[1] += name[1]
        multi_arr[2] += name[2]
        multi_arr[3] += name[3]
        multi_arr[4] += name[4]
    return multi_arr

_a = get_multi_mixed_arr(
    AMPM_ARR[0],
    SYMBOL_ARR[0],
    NUM_ARR[1],
    NUM_ARR[2],
    SYMBOL_ARR[1],
    SYMBOL_ARR[0],
    NUM_ARR[2],
    NUM_ARR[3],
    SYMBOL_ARR[1],
    SYMBOL_ARR[0],
    NUM_ARR[4],
    NUM_ARR[5],
    )
show_1_digit_of(_a, 0)

_b = get_multi_mixed_arr(
    CONTROL_DICT['a'],
    CONTROL_DICT['_'],
    CONTROL_DICT['1'],
    CONTROL_DICT['2'],
    CONTROL_DICT[':'],
    CONTROL_DICT['_'],
    CONTROL_DICT['2'],
    CONTROL_DICT['3'],
    CONTROL_DICT[':'],
    CONTROL_DICT['_'],
    CONTROL_DICT['4'],
    CONTROL_DICT['5'],
    )
show_1_digit_of(_b, 0)
