import random
import time
import os

GROUND_WIDTH = 50
FILLER = '.'
ORNAMENTS_LIST = ('*' * 3).join('o$@#&')

while True:
    for n in range(1, 40, 2):
        if n <= 3:
            string = '*' * n
        else:
            inner = ""
            for x in range(n - 2):
                inner += random.choice(ORNAMENTS_LIST)
            string = '*' + inner + '*'
        print(string.center(GROUND_WIDTH, FILLER))

    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print('W'.center(GROUND_WIDTH, FILLER))
    print(('#' * 19).center(GROUND_WIDTH, FILLER))

    time.sleep(0.3)
    os.system('cls')
