"""
# 여러가지 지능, 모듈, 함수관련 잡다한 테스트~
#   01.날짜, 시간관련 모듈 = https://goo.gl/SQuimv
#   02.람다와 map, filter, reduce = https://goo.gl/223gH1
"""
import script_run
import _test_some

def main():

    function_names = [func
                        for func in _test_some.__dir__()
                        if func.startswith("run")
                        ]


    print(function_names)
    # ['run_01_dateformat', 'run_02_reduce', 'test03_setter']
    # run_01_dateformat()           # 2015-06-12
    # run_02_reduce()               # 24


    for i, name in enumerate(function_names, 1):
        print(f"{i}. {name:20}: ", end='')
        func = getattr(_test_some, name)
        func()
        print(func.__doc__)

    this_filename = __file__.split("\\")[-1]
    print(this_filename)


def run_01_dateformat():
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


def run_02_reduce():
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



if __name__ == '__main__':
    print(__doc__)
    main()
