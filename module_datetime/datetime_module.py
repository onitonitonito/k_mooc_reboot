"""
# datetime_module.py - some datetime module example
"""
# https://www.programiz.com/python-programming/datetime

import datetime

print(__doc__)

ttime_dict = {
        'now'       : datetime.datetime.now(),
        'today'     : datetime.date.today(),
        'certain'   : datetime.date(2019, 11, 30),
    }



def run00_basic():
    """00.datetime 과 date 오브젝트의 차이"""
    # print(ttime_dict['now'])
    # print(ttime_dict['today'])
    # print(ttime_dict['certain'])

    [print(item) for item in ttime_dict.values()]
    return f"{run00_basic.__doc__:-^40}\n\n"

def run01_time_delta():
    """01.타임델타 오브젝트"""
    from datetime import datetime, date
    t1 = date(year = 2018, month = 7, day = 12)
    t2 = date(year = 2017, month = 12, day = 23)
    t3 = t1 - t2            # t3 = 201 days, 0:00:00
    print("t3 =", t3)

    t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
    t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
    t6 = t4 - t5            # t6 = -333 days, 1:14:20
    print("t6 =", t6)

    print("type of t3 =", type(t3))         # <class 'datetime.timedelta'>
    print("type of t6 =", type(t6))         # <class 'datetime.timedelta'>
    return f"{run01_time_delta.__doc__:-^40}\n\n"

def run03_td_differences():
    """03.타임델타의 차이 계산"""
    from datetime import timedelta
    t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
    t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
    t3 = t1 - t2
    print("t3 =", t3)
    print("type of t3 =", type(t3))
    return f"{run03_td_differences.__doc__:-^40}\n\n"

def run04_negative_calc():
    """04.네가티브 타임델타 계산/처리"""
    from datetime import timedelta
    t1 = timedelta(seconds = 33)
    t2 = timedelta(seconds = 54)
    t3 = t1 - t2
    print("t3 =", t3)
    print("t3 =", abs(t3))
    return f"{run04_negative_calc.__doc__:-^40}\n\n"

def run05_timezone_change():
    """05.로컬타임과 다른타임존 처리"""
    import pytz
    from datetime import datetime
    local = datetime.now()
    print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    time_London = datetime_London.strftime("%m/%d/%Y, %H:%M:%S")
    print("London:", London_time)

    return f"{run05_timezone_change.__doc__:-^40}\n\n"


if __name__ == '__main__':
    """ 런 올 런즈 """
    import datetime_module

    [print(val())
        for key, val in datetime_module.__dict__.items()
        if key.startswith("run")]



# def run00_():
#     """00."""
#     return f"{run00_.__doc__:-^40}\n\n"
