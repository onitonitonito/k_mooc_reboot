import random
import time
import os

GROUND_WIDTH = 50
FILLER = '.'
ORNAMENTS_LIST = ('*' * 3).join('o$@#&')

while True:
    # Blinking Xmas Tree
    for n in range(1, 40, 2):
        if n <= 3:
            string = '*' * n
        else:
            inner = ""
            for x in range(n - 2):
                inner += random.choice(ORNAMENTS_LIST)
            string = '*' + inner + '*'
        print(string.center(GROUND_WIDTH, FILLER))

    # Tree trunk & Stand
    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print(('#' * 19).center(GROUND_WIDTH, FILLER))

    # wait 0.3 sec & clear screen
    time.sleep(0.3)
    os.system('cls')
