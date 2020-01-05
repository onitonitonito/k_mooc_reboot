"""
# 이맘 때, 한번 쯤 만들어 보는 Xmas 트리 - 생활코딩
# http://bit.ly/2EXwk1r
"""
# https://www.facebook.com/photo.php?fbid=3199985326694503
# &set=gm.3602534863120357&type=3&theater&ifg=1

import os
import time

from random import random

# print(__doc__)

rate_globes = 0.2
width = 16

def main():
    while 1:
        xmas_tree(width, rate_globes)
        time.sleep(0.5)
        os.system('cls')

def xmas_tree(width, rate_globes):
    """c = center / e = exterior """
    c = lambda x: print(x.center(width))
    e = lambda : 'o' if random() < rate_globes else '*'

    # [c(r) for r in 'A-< >-V'.split('-')]  # ... original
    [c(r) for r in 'A-starbugs-V'.split('-')]
    [c(''.join(e() for _ in range(i))) for i in range(3,width,2)]
    [c(r) for r in r'| |-| |-_/_|_\_'.split('-')]
    c('^'*width)



if __name__ == '__main__':
    main()
