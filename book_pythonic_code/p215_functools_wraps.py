"""
"""
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) --> %r'% (
                func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    """ return n-th fibonacci number """
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

fibonacci(3)
help(fibonacci)

""" Using Functools.warps
 (1) w/o functools.wraps - help(fibonacci)
  Help on function wrapper in module __main__:
  wrapper(*args, **kwargs)

 (2) w/ functools.wraps - help(fibonacci)
  Help on function fibonacci in module __main__:
  fibonacci(n)
      return n-th finonacci number
 """


from threading import *
from contextlib import *
from logging import *

lock = Lock()

def try_finally():
    lock.acquire()
    try:
        print('lock is held')

    except EOFError as e:
        pass

    finally:
        lock.release()

""" The same Excution below : but way better, more simple. p.220
with lock:
    print('Lock is held')

 - it contains @contextmanager
"""
def my_function():
    debug('Some dubug data')
    error('Error log here')
    debug('More debug data')

@contextmanager
def debug_logging(level):
    logger = getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)
# my_function()

with debug_logging(DEBUG):
    print('Inside: ')
    my_function()

print('After: ')
my_function()

@contextmanager
def log_level(level, name):
    logger = getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with log_level(DEBUG, 'my-log') as logger:
    debug('This is my message')
    debug('This will not print')
