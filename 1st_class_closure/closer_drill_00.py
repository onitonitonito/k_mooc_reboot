""" Closure Example : Nested Function, same as JS
  - outer return inner itself.
  - refer : http://jonnung.blogspot.kr/2014/09/python-easy-closure.html
  - refer to : SchoolOfWeb = https://goo.gl/CmMaqo
"""

def say_hello(name):
    """ SIMPLE CLOSER :
      -inner can use (reachable) outer's args
    """
    def helper():
        print('Hello %s' % name)
    return helper               # return inner Function (object)

_a = say_hello('Jung-Eun')   # a = return value (function object)
_a()                         # function call
# del helper                  # delete function object
del say_hello
_a()              # delete function object


def outer_func():           #1
    message = 'Hi!'         #3 = free variable
    def inner_func():       #4
        print(message)      #6
    return inner_func()     #5
# outer_func()                #2

def outer_func1():          #1
    message = 'Hi!'         #3 = free variable
    def inner_func1():      #4
        print(message)      #6
    return inner_func1      #5 (!) not call, only object return


_b = outer_func1()           #

_b()
del outer_func1
_b()

def lookup_closure_cell():
    print(_a,                "\n\n")     # object address
    print(dir(_a),           "\n\n")     # __closure__

    print(type(_a),          "\n\n")
    print(_a.__closure__,    "\n\n")
    print(_a.__closure__[0], "\n\n")

    print(dir(_a.__closure__[0]),    "\n\n")
    print(dir(_a.__closure__),    "\n\n")
    print(_a.__closure__[0].cell_contents, "\n\n")       # Hi!
    # print(_a.__closure__.cell_contents)

    _a.__closure__[0]()      # cell object NOT callable ERROR
    """ print(_a.__closure__.cell_contents)
        AttributeError: 'tuple' object has no attribute 'cell_contents'
    """
# lookup_closure_cell()
