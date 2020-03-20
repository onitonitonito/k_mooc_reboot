"""
# 3년 전 이 맘때, ... 쓸 데 없이 복잡!
# http://bit.ly/37k5HQf
"""
# https://gist.github.com/onitonitonito/d1cac8fb7a07229b238bf4534efea41b

import os
import time

ground_width=60


def main():
    growing_corn_shape_tree()
    time.sleep(1)
    clear()
    whole_xmas_tree(ground_width)

def clear():
    print("\n\n"*50)

def set_starbucks(tree_base_width):
    print(("STAR").center(tree_base_width))
    print(("BUCKS").center(tree_base_width))

def triangle(tree_leaf_end, tree_base_width):
    for x in range(1,tree_leaf_end+1, 2):
        print(("*"*x).center(tree_base_width))

def trapezoid(tree_leaf_start, tree_leaf_end, tree_base_width):
    for x in range(tree_leaf_start, tree_leaf_end+1, 2):
        print(("*"*x).center(tree_base_width))

def trunk(tree_trunk_height, tree_base_width):
    for x in range(tree_trunk_height):
        print(("|"*1).center(tree_base_width))

def ground(tree_base_width):
    print(("M"*tree_base_width).center(tree_base_width))
    print(("Christmas season just is around the corner!").center(tree_base_width))
    print("TREE SIZE = %s"%tree_base_width,"!!!","\n\n")

def corn_shape_tree(tree_leaf_end, tree_trunk_height, tree_base_width):
    """# whole corn shape tree"""
    triangle(tree_leaf_end, tree_base_width)
    trunk(tree_trunk_height, tree_base_width)
    ground(tree_base_width)

def growing_corn_shape_tree():
    #order_leaf = [10, 20, 30, 40, 50, 60, 70, 80, 90,]
    #order_trunk = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    order_leaf = [x for x in range(10, 45, 5)]
    order_trunk = [x for x in range(1, 8, 1)]
    tree_base_width = int( order_leaf[-1]* 1.40 )        # 140% of last biggest width

    for leaf_step, trunk_height in  zip(order_leaf, order_trunk):
        clear()               # with script or IDLE screen
        # os.system('cls')        # with CMD screen

        set_starbucks(tree_base_width)
        corn_shape_tree(leaf_step, trunk_height, tree_base_width)
        time.sleep(0.5)

    print('order_leaf=',order_leaf)
    print('order_trunk=',order_trunk)
    print("ground_width(last order_leaf * 140%%) = %s"% tree_base_width)
    print()

def whole_xmas_tree(ground_width):
    set_starbucks(ground_width)
    triangle(15, ground_width)
    trapezoid(7,20,ground_width)
    trapezoid(12,30,ground_width)
    trunk(3, ground_width)
    ground(ground_width)



if __name__ == '__main__':
    main()
