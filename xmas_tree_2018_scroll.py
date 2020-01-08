"""
# the sign board used to make once at this time of years
# [TODO:] there's further developement
"""
# 매년 이맘때, 한번 쯤 만드는, 스크롤 싸인보드를 만들어 보자

import os
import time

from array_letters import digits, digit_h, digit_w

# print(__doc__)

screen = 70
time_lag_blinking = 0.1

show_width = digit_w * 6
blanks = [ " " * int((screen-show_width)/2) for i in range(digit_h)]
signs = [blanks[i] +
            digits['x'][i] +
            digits['2'][i] +
            digits['0'][i] +
            digits['2'][i] +
            digits['0'][i] +
            digits['!'][i]
            for i in range(digit_h)]

def main():
    while 1:
        sign_bottom_up(signs)
        clear_after(1)
        sign_blinking(times=5, interval=0.1)

        sign_up_bottom(signs)
        clear_after(1)
        sign_blinking(5, 0.1)

        sign_left_right(signs)
        clear_after(1)
        sign_blinking(5, 0.1)

        sign_right_left(signs)
        clear_after(1)
        sign_blinking(5, 0.1)

def clear_after(time_waiting):
    time.sleep(time_waiting)
    os.system('cls')

def show_tag(index):
    print()
    print('A')
    print('|')
    print(f'o====== index[{index}]')

def sign_whole(signs):
    """HELPER() for sign_blinking() """
    for i in range(digit_h):
        print(signs[i])

def sign_blinking(times, interval):
    """shows blinking sings"""
    for i in range(times):
        sign_whole(signs)
        clear_after(interval)
        time.sleep(interval)

def sign_up_bottom(signs):
    """shows up to bottom direction"""
    for j in range(1, digit_h + 1):
        for i in range(j):
            print(signs[i])
        time.sleep(time_lag_blinking)
        if j < digit_h:
            os.system('cls')

def sign_bottom_up(signs):
    """shows bottom to up direction"""
    for j in range(1, digit_h + 1):
        for k in range(digit_h + 1 - j):
            if k > 0:
                print()
        for i in range(j):
            print(signs[i])
        time.sleep(time_lag_blinking)
        if j < digit_h:
            os.system('cls')

# TODO: FURTHER DEVELOP BELOW!
def sign_left_right(signs):
    """shows left to right direction"""
    width_signs = len(signs[0])
    for i in range(width_signs):
        clear_after(0.1)
        for j in range(digit_h):
            print(signs[j][width_signs - 1 -i:width_signs])
        show_tag(i)

def sign_right_left(signs):
    """shows right to left direction"""
    width_signs = len(signs[0])
    for i in range(width_signs):
        clear_after(0.1)
        for j in range(digit_h):
            print(" " * (width_signs - 2 - i) + signs[j][0:i])
        show_tag(i)


if __name__ == '__main__':
    from pyprnt import prnt
    print("\nsigns = digits['x'] ..['2'] ..['0'] ..['2'] ..['0'] ..[!]")
    prnt(signs)

    print("\ndigits['x'] :")
    prnt(digits['x'])

    answer = "\n\n... To Continue ==> YES=[Enter] / NO=[!]: "
    if input(answer).startswith("!"):
        quit()

    main()
    pass
