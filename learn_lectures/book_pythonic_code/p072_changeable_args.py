#! python
""" BETTER WAY 13. - Use changeable args : *Args  p.072
 (1) star values        =  *Args   --> turn to 'list' / but give 'tuple' func.
 (2) double star values = **Kwargs --> turn to 'dict'
"""
def _log(message, values=[]):       # IN= 'str', 'list'
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s : %s'% (message, value_str))

def log(message, *values):          # * <---ONLY ONE CHANGED
    """ *value : automatically turn into array type
    ('str', value1, value2, value3 .....) -> ('str', [v1,v2,v3...])
    """
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print('%s : %s'% (message, value_str))

def main_log():
    """ COMPARE : log file use """

    _log('My number is....', [1, 2, 3])  # My number is.... : 1,2,3
    _log('Just say, HELLO~!!...')        # Just say, HELLO~!!...
    print()

    """ THESE! are much EASY to read/understand
    """
    log('My number is....', 1, 2, 3)    # My number is.... : 1,2,3
    log('Just say, HELLO~!!...')        # Just say, HELLO~!!...
    print()

    likes = ['Banana', 'Python', 'Drone', 'Game']
    log('My favorites', likes)  # My favorites: ['Banana', 'Python',... 'Game']
    log('My favorites', *likes) # My favorites: Banana, Python, Drone, Game
    print()
# main_log()

""" PROBLEMATIC Side Effects : pass it as a 'tuple' to function
"""
def my_generator():
    for n in range(10):
        yield n

def my_function(*args):
    print(args)
    print(type(args))

def my_main_problem():
    """ at first, it was (GENERATOR) but changed into (TUPLE) """
    _a = my_generator()         # generator make just once..
    print(*_a)                  # 0 1 2 3 4 5 6 7 8 9
    print(type(_a))             # <class 'generator'>
    print()

    _a = my_generator()         # generator make just once..
    my_function(*_a)            # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) = <class 'tuple'>
    print()
# my_main_problem()

""" PROBLEMATIC 02. Can not change (TUPLE)
"""
def log_(sequence, message, *values):
    if not values:
        print('%s : %s'% (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s : %s : %s' %(sequence, message, values_str))

def main_log():
    """ To solve this, have to use **Kwargs --> refer to BETTER WAY.21 """
    log_(1, 'Favorites', 7, 33)     # 1 : Favorites : 7, 33
    log_('Favorite numbers', 7, 33) # Favorite numbers : 7 : 33 <-male function
# main_log()

""" BETTER WAY.21 - USE Keyworded Arguments (**Kwargs) to be Explicit p.083
"""
def safe_division(number, divisor,
                            ignore_overflow,
                            ignore_zero_division):
    try:
        return number / divisor

    except OverflowError as e:
        if ignore_overflow:
            return 0
        else:
            raise

    except ZeroDivisionError as e:
        if ignore_zero_division:
            return float('inf')     # type <class 'float'>, - infinite -
        else:
            raise

def main_safe():
    """ Args. can be Implicit, can not force to be Explicit """
    _result = safe_division(1, 10**500, 1, 0)   # 0.0, ignore float OverflowError
    _result = safe_division(1, 0, 0, 1)         # inf, ignore ZeroDivisionError
    print(_result)
# main_safe()

def safe_division_b(number, divisor,
                            ignore_overflow=False,
                            ignore_zero_division=False):
    _a = safe_division(number, divisor, ignore_overflow, ignore_zero_division)
    print(_a)

def safe_division_c(number, divisor,* ,        # * = separator Args / KWargs
                            ignore_overflow=False,
                            ignore_zero_division=False):
    _a = safe_division(number, divisor, ignore_overflow, ignore_zero_division)
    print(_a)

def main_explicit():
    """ Args. can be Implicit, can not force to be Explicit """
    safe_division_b(1, 10**500, ignore_overflow=True)   # 0.0
    safe_division_b(1, 0, ignore_zero_division=True)    # inf
    safe_division_b(1, 0, False, True)                  # inf
    print()

    safe_division_c(1, 10**500, ignore_overflow=True)   # 0.0
    safe_division_c(1, 0, ignore_zero_division=True)    # inf

    """ CAN NOT BE IMPLICIT.. be very obvious # ERROR - CAN'T USE Args """
    # safe_division_c(1, 0, False, True)   # ERROR: takes 2 args. but 4 given
    print()
# main_explicit()

""" POINTS & LESSONS
 - Kwargs make function's planed purpose more obvious.
 - If function need to take many bull-flags, it is more than neccessity
 - Python3 support exclusive grammer for KW-Arguments, separator '*'
   while Python2 doesn't....
 - Use raising TypeError dealing with Python2
"""
