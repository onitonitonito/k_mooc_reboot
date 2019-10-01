def main():
    import _test_some

    function_names = [func
                        for func in _test_some.__dir__()
                        if not func.startswith("_")
                        ]

    function_names.remove('main')
    print(function_names)

    # ['test01_dateformat', 'test02_reduce', 'test03_setter']
    # test01_dateformat()           # 2015-06-12
    # test02_reduce()               # 24
    # test03_setter()               # 3 5.196152422706632

    for i, name in enumerate(function_names, 1):
        print(f"{i}. {name:20}: ", end='')
        func = getattr(_test_some, name)
        func()
        print(func.__doc__)


def test01_dateformat():
    """[python] 날짜, 시간관련 모듈 = https://goo.gl/SQuimv
    # import datetime
    # d = datetime.date(2015, 4, 15)
    # t = datetime.time(12, 23, 38)
    # dt = datetime.datetime.combine(d, t)
    # print(dt) # 2015-04-15 12:23:38
    """
    import datetime

    date_fields = (2015, 6, 12)
    date = datetime.date(*date_fields)
    print(date)


def test02_reduce():
    """람다와 map, filter, reduce = https://goo.gl/223gH1
    # >>> a = [1, 2, 3, 4, 5]
    # >>> from functools import reduce
    # >>> reduce(lambda x, y: x + y, a)
    # 15
    """
    from functools import reduce

    def product(*numbers):
        return reduce(lambda x, y: x * y, numbers)

    # 1 * 2 * 3 * 4 = 24   ... concatenate
    print(product(1, 2, 3, 4))


def test03_setter():
    from math import sqrt

    class SmartPoint(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def hypotenuse(self):
            return sqrt(self.x ** 2 + self.y ** 2)

        @hypotenuse.setter
        def hypotenuse(self, z):
            # Sily setter example .. 값을 정(set)해주면 self.y를 변경
            self.y = sqrt(z ** 2 - self.x ** 2)

    point = SmartPoint(3, 4)
    # Callable 함수는 없다. 속성 값만 있다.
    # print(point.hypotenuse)     # 5.0  ... sqrt(3**2 + 4**2) = sqrt(25)

    point.hypotenuse = 6         # 리턴값(set) = 정해진값(x)를 놔두고 (y역산)
    print(point.x, point.y)      # 3 5.196152422706632 ... 역산(y) = 5.1961..
    print()


if __name__ == '__main__':
    main()
