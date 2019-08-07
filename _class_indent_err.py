"""
#
#
#
#
"""
# print(__doc__)

PI = 3.14


class Math(object):
    def solv(self, r):
        return PI * (r**2)


def sum(a, b):
    return a + b


if __name__ == '__main__':
    print(PI)

    a = Math()

    print(a.solv(4.4))
    print(sum(2, 3))
