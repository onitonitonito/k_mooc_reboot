"""
# 3년전 이맘때 쯤, 블링킹 xmas 트리
"""
import os
import time
import random

# print(__doc__)

filler = '.'
width_ground = 50
ornaments_list = ('*' * 3).join('o$@#&')

def main():
    while True:
        # Blinking Xmas Tree
        for n in range(1, 40, 2):
            if n <= 3:
                string = '*' * n
            else:
                inner = ""
                for x in range(n - 2):
                    inner += random.choice(ornaments_list)
                string = '*' + inner + '*'
            print(string.center(width_ground, filler))

        # Tree trunk & Stand
        print('W'.center(width_ground, filler))
        print('W'.center(width_ground, filler))
        print('W'.center(width_ground, filler))
        print(('#' * 19).center(width_ground, filler))

        # wait 0.3 sec & clear screen
        time.sleep(0.5)
        os.system('cls')


if __name__ == '__main__':
    main()
