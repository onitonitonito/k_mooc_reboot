import time

def triangle(tree_base_width, leaf_step):
    tree_leaf_step = leaf_step
    tree_base_with = tree_base_width

    for x in range(1,tree_leaf_step+1,2):
        print(("*"*x).center(tree_base_width))

def trunk(tree_base_width, trunk_height):
    tree_trunk_height = trunk_height
    tree_base_with = tree_base_width

    for x in range(tree_trunk_height):
        print(("|"*1).center(tree_base_width))

def ground(tree_base_width):
    print(("W"*tree_base_width).center(tree_base_width))
    print(("Christmas season is just around the corner!").center(tree_base_width))
    print("Tree size = %s" %tree_base_width,"!!!","\n\n")

def starbucks(tree_base_width):
    print(("STAR").center(tree_base_width))
    print(("BUCKS").center(tree_base_width))


def x_mas_tree(leaf_step, trunk_height):
    tree_leaf_step = leaf_step
    tree_trunk_height = trunk_height

    tree_base_width = (tree_leaf_step + 20)

    print(("STAR").center(tree_base_width))
    print(("BUCKS").center(tree_base_width))

    for x in range(1,tree_leaf_step+1,2):
        print(("*"*x).center(tree_base_width))

    for x in range(tree_trunk_height):
        print(("|"*1).center(tree_base_width))

    print(("W"*tree_base_width).center(tree_base_width))
    print(("Christmas season is just around the corner!").center(tree_base_width))
    print("Tree size = %s" %tree_base_width,"!!!","\n\n")
