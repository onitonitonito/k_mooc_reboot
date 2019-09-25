import os
import sys
from os.path import dirname, join

WORK_DIR = join(dirname(dirname(__file__)), 'module_custom', '')
print(WORK_DIR)
sys.path.append(dirname(dirname(__file__)))

from module_custom.xmas_tree import *

# order_leaf = [10, 20, 30, 40, 50, 60, 70, 80, 90,]
# order_trunk = [1, 2, 3, 4, 5, 6, 7, 8, 9,]


def growing_tree():
    order_leaf = [x for x in range(10, 45, 5)]
    order_trunk = [x for x in range(1, 8, 1)]
    tree_base_width = int(order_leaf[-1]*1.40)  # 140% of last biggest width

    for leaf_step, trunk_height in zip(order_leaf, order_trunk):
        clear()               # with script or IDLE screen
        # os.system('cls')        # with CMD screen

        set_starbucks(tree_base_width)
        set_tree(leaf_step, trunk_height, tree_base_width)
        time.sleep(0.5)

    print('order_leaf=', order_leaf)
    print('order_trunk=', order_trunk)
    print("ground_width(last order_leaf * 140%%) = %s" % tree_base_width)
    print()


def xmas_tree():
    ground_width = 60
    set_starbucks(ground_width)
    triangle(15, ground_width)
    trapezoid(7, 20, ground_width)
    trapezoid(12, 30, ground_width)
    trunk(3, ground_width)
    ground(ground_width)

growing_tree()
time.sleep(3)
clear()

xmas_tree()

# Class module should be placed at {module_custom} folder.
