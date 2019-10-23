"""
# simple pygame test
#
"""
# print(__doc__)



def fetch_three_variable_in_one():
    (a, b, c) = (5, 2, 3)
    print(f"[{a}, {b}, {c}]")

    if a < b and b < c:
        print('ASENDING!')
    else:
        print('__disturbed!__')
        _as = [a,b,c]
        _as.sort()
        print(_as)


def test_divid_percent_method():
    for n in range(10):
        # print("n=%s:  n%%3=%s" % (n, n%3))
        print(f"n={n}: ... n%3 = {n%3}")


def test_random_int_fetch():
    import random
    for n in range(10):
        print(random.randint(0, 1))


def effect_bouncing_image():
    """ images bounciing effect using pygame default LIB """
    from os.path import join
    from os.path import dirname
    from pygame.examples.mask import main

    root_dir = dirname(dirname(dirname(__file__)))

    IMG_00 = join(root_dir, 'statics', 'img', 'cat-icon.png')
    IMG_01 = join(root_dir, 'statics', 'img', 'icon_greyCAT.png')
    IMG_02 = join(root_dir, 'statics', 'img', 'icon_yellowCAT.png')

    # for test
    # print(IMG_01)

    main(IMG_00, IMG_01, IMG_02)


fetch_three_variable_in_one()
# test_divid_percent_method()
# test_random_int_fetch()
# effect_bouncing_image()
