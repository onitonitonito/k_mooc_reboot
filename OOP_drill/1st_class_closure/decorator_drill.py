"""--------------------------------------- SESSION 01--To make Closure function
  refer to SchoolOfWeb / Decorator = https://goo.gl/XdOvVv
  - nested double functions
  - inner(wrapper) func uses outer function args.
  - return inner(wrapper) function object   """

def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('Hi~!!')
bye_func = outer_function('Bye~!')

hi_func()
bye_func()

"""--------------------------------------- SESSION 02--to make decorator_function

  """
def decorator_function(original_function):
    def wrapper_function():                     #2
        return original_function()              #7
    return wrapper_function                     #6

def display():               #2
    print('DISPLAY function is activated!...')

# decorated_display = decorator_function(display) #3
# decorated_display()
# display()

"""--------------------------------------- SESSION 03---"""
def decorator_function(original_function):
    def wrapper_function():
        print('{} function is NOT activated...'.format(original_function.__name__))                     #2
        return original_function()              #7
    return wrapper_function                     #6

def display_01():               #2
    print('DISPLAY(_01_) function is activated!...')

def display_02():               #2
    print('DISPLAY(_02_) function is activated!...')

# display_01 = decorator_function(display_01)
# display_02 = decorator_function(display_02)
#
# display_01()
# print()
# display_02()
# print()

"""--------------------------------------- SESSION 04---"""
def decorator_function(original_function):
    def wrapper_function():
        print('{} function is NOT activated...'.format(original_function.__name__))                     #2
        return original_function()              #7
    return wrapper_function                     #6

@decorator_function             #1
def display_01():               #2
    print('DISPLAY(_01_) function is activated!...')

@decorator_function             #1
def display_02():               #2
    print('DISPLAY(_02_) function is activated!...')

# display_01()
# print()
# display_02()
# print()

"""--------------------------------------- SESSION 05---"""
'''' wrapper_function has no arguments but 2 given : Error '''
def decorator_function(original_function):
    def wrapper_function():
        print('{} function is NOT activated...'.format(original_function.__name__))                     #2
        return original_function()              #7
    return wrapper_function                     #6

@decorator_function             #1
def display_03():               #2
    print('DISPLAY(_03_) function is activated!...')

@decorator_function             #1
def display_info(name, age):
    print('DISPLAY_INFO({}, {}) function is activated...'.format(name, age))

# display_03()
# print()
#
# ''' wrapper_function has no arguments but 2 given : Error '''
# display_info('Jung-Eun', 24)

"""--------------------------------------- SESSION 06---"""
def decorator_function(original_function):
    def wrapper_function(*args, **Kwargs):
        print('{} function is NOT activated...'.format(original_function.__name__))                     #2
        return original_function(*args, **Kwargs)              #7
    return wrapper_function                     #6

@decorator_function             #1
def display_03():               #2
    print('DISPLAY(_03_) function is activated!...')

@decorator_function             #1
def display_info(name, age):
    print('DISPLAY_INFO({}, {}) function is activated...'.format(name, age))

# display_03()
# print()
# display_info('Jung-Eun', 24)

"""--------------------------------------- SESSION 06--CLASS-"""
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} function is NOT activated...'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass     #2
def display_03():               #2
    print('DISPLAY(_03_) function is activated!...')

@DecoratorClass     #3
def display_info(name, age):
    print('DISPLAY_INFO({}, {}) function is activated...'.format(name, age))

# display_03()
# print()
# display_info('Jung-Eun', 24)

"""--------------------------------------- SESSION 07--PROJECT-
(1) Logging file is written in display_info.log file
 - INFO:root:[2017-10-05 16:27] achieved result args -('Jung-Eun', 24), kwargs= {}
 - INFO:root:[2017-10-05 16:27] achieved result args -('Hello World!!',), kwargs= {}
(2) display_info(Jung-Eun, 24) function is activated...
"""
import datetime
import time

def my_logger(original_function):
    import logging
    logging.basicConfig(
        filename='{}.log'.format(original_function.__name__),
        level=logging.INFO)

    def wrapper_function(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] achieved result args -{}, kwargs= {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)
    return wrapper_function

@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) funtion is activated...'.format(name, age))

@my_logger
def display_04(msg):
    time.sleep(2)
    print('display_04({}) function is activated...'.format(msg))

# display_info('Jung-Eun', 24)
# display_04('Hello World!!')
