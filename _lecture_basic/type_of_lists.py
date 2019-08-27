"""
#
#
#
#
"""
# print(__doc__)
import numpy as np


def sep(arg="-"):          # make seperator '----------------'
    print("-" * 20 + "%s\n" % arg)


def x_weird_indexing():
    """
    # trash : 'x' = means temporarily dumped into gabage
    """
    global m
    m = 0

    def diffsum(x1, x2, x3):
        global m                # declair global.. at in def()
        # print(m, end=', ')
        y1 = x1 + x2 + x3
        y2 = x1 * 2 + x2 * 2 + x3**2

        if ((y2 - y1) > m):
            m = (y2 - y1)
        return (x1, x2, x3), m, (y2 - y1), y1, y2

    m_list = []

    for x in range(3):
        for y in range(3):
            for z in range(3):
                _, m_, *_ = diffsum(x, y, z)
                m_list.append(m_)             # a[1] = value 'm'

    print('\n', m_list)

    # [
    #   0, 0, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4,
    #   4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6
    # ]


def numpy_():
    # make NUMPY range [0 1 2 3 4] there's no ',' : NOT array
    a = np.arange(5)
    print(type(a))
    print(a)
    sep('NUMPY')


def range_():
    a = [x for x in range(5)]
    print(type(a))
    print(a)
    sep('Comprehensive_List')


def tuffle_():
    a = (0, 1, 2, 3, 4)
    print(type(a))
    print(a)
    sep('Type_TUFFLE')


def enumerate_():
    a = [x for x in range(5)]
    print(type(enumerate(a)))
    for i, x in enumerate(a):        # always! use along with (for i,x)
        print("i=%s, x=%s :" % (i, x))
    print(enumerate(a))             # <enumerate object at 0x024945A8>
    sep('ENUM with fori-x')


def dict_():
    a = {i: value for i, value in enumerate([y for y in range(5)])}
    print(type(a))
    print(a)
    print("a[%s]= %s" % (3, a[3]))    # enumerated index num = 3
    sep('Enum_DICT')


def iterate_():
    import itertools
    y = 3
    x = 2

    a = list(itertools.product(range(1, y + 1), repeat=x))

    print(a)
    print(len(a))
    print(a[0])
    print(a[0][1])
    sep('with Itertools')

    b = eval(str(a[3][0]) + str(a[3][1]))
    print(b)
    print(type(b))
    sep('eval+str')

    for x in range(len(a)):
        print(a[x])
    sep('print(a[x] for x in range(len(a)))')

    for x in range(1, 4):
        for y in range(1, 4):
            print("(%s, %s)" % (x, y))
    sep('for.x-for.y combo')

    c1 = [(x, y) for y in range(1, 4) for x in range(1, 4)]
    c2 = [(x, y) for x in range(1, 4) for y in range(1, 4)]
    c3 = sorted([(x, y) for y in range(1, 4) for x in range(1, 4)])
    print(c1)
    print(c2)
    print(c3)
    sep('comparison')


if __name__ == '__main__':
    x_weird_indexing()
    # numpy_()
    # range_()
    # tuffle_()
    # enumerate_()
    # dict_()
    # iterate_()
    pass
