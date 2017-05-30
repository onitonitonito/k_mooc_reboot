import time, random

def clear():
    print("\n\n"*50)

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

def set_starbucks(tree_base_width):
    print(("STAR").center(tree_base_width))
    print(("BUCKS").center(tree_base_width))

def set_tree(tree_leaf_end, tree_trunk_height, tree_base_width):   # whole corn shape tree
    triangle(tree_leaf_end, tree_base_width)
    trunk(tree_trunk_height, tree_base_width)
    ground(tree_base_width)

# Should be placed at {package_i} folder as package.
# run run_xmastree.py at {ROOT} folder.
