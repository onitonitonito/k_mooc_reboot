""" 데코레이터와 플라워 : 누가 먼저 실행될까?
"""
import random
import datetime

def flower(other_func):
    def wrapper(*args, **kwargs):
        print(" ...  I'll give you a @;>---   ...")
        print(args, kwargs, '\n')
        return other_func(*args, **kwargs)
    return wrapper


def decorator(other_func):
    def wrapper(*args, **kwargs):
        message = other_func(*args, **kwargs)
        print(''
              '--------- This is Decorator ------------\n'
              '   ... IT ALWAYS RUNS BEFORE HAND ...\n'
              '----------------------------------------\n'
              '  ' + '%s' % message + '\n'
              '----------------------------------------\n\n')
        # return other_func(*args, **kwargs)
    return wrapper


@flower
@decorator
def other_func(name, greeting='Hi???'):
    says = ['Nice to meet you!', 'How have you been?', "What's up?", "A-hoy!"]
    say = random.choice(says)
    return "{}! My name is '{}'! {}".format(greeting, name, say)

@flower
@decorator
def another_func(name, greeting=77):
    print("AAAA %s ... print value"% name)
    return "BBB %d ... return value"% greeting

other_func('Emma', greeting='HELLO')
another_func('Jay', greeting=55)

# if without 'DECORATOR' -----------
# a = decorator(other_func)
# a('kay', greeting='Say Hi')

# if with 'DECORATOR' ---------------
# other_func('Kay', greeting='HELLO')
# other_func('Jay', greeting='HI')

# repeatedly call funcs -------------
# other_func('Kay', 'HELLO')
# other_func('Jay', 'HI')

# using 'zip()' ---------------------
# names = 'Ai, Jay, Kay, El'.split(', ')
# says = 'HELLO, HI, SAY-YO, AH!'.split(', ')
# for name, say in zip(names, says):
#     other_func(name, greeting=say)


def makebold(other_func):
    def wrapped(*args, **kwargs):
        print('..안에는 두껍게..')
        return "<b>" + other_func(*args, **kwargs) + "</b>"
    return wrapped


def makeitalic(other_func):
    def wrapped(*args, **kwargs):
        print('..밖에는 기울게..')
        return "<i>" + other_func(*args, **kwargs) + "</i>"
    return wrapped


@makeitalic
@makebold
def hello():
    return "hello world"

@makeitalic
@makebold
def say(name):
    return "A-Yo! '%s'! Welcome"% name


print(hello())
print(say('Jay'))

""" __ 2차 함수에 넣었을 때 ___ """
# ..안에는 두껍게..
# ..밖에는 기울게..
# <i><b>hello world</b></i>
#
# ..안에는 두껍게..
# ..밖에는 기울게..
# ..안에는 두껍게..
# ..밖에는 기울게..
# <i><b>hello world</b></i>
# <i><b>A-Yo! 'Jay'! Welcome</b></i>


""" __ 3차 함수에 넣었을 때 ___ """
# ..밖에는 기울게..
# ..안에는 두껍게..
# <i><b>hello world</b></i>
#
# ..밖에는 기울게..
# ..안에는 두껍게..
# <i><b>A-Yo! 'Jay'! Welcome</b></i>


import datetime

class DatetimeDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('\n')
        print(datetime.datetime.now())
        print('--'*15)
        self.func(*args, **kwargs)
        print('--'*15)
        print(datetime.datetime.now())


class MainClass:
    @DatetimeDecorator
    def main_function_1():
        print("  MAIN FUNCTION 1 START")

    @DatetimeDecorator
    def main_function_2():
        print("  MAIN FUNCTION 2 START")

    @DatetimeDecorator
    def main_function_3():
        print("  MAIN FUNCTION 3 START")


my = MainClass()
my.main_function_1()
my.main_function_2()
my.main_function_3()
