""" 데코레이터(), 어떻게 쓸 것인가? -- 클로저()를 먼저 알아라...
# 클로저(데코레이터)함수를 만든다.  --> 일반함수 위에 '@데코레이터'를 올린다.
# 일반함수(*args, **kwargs)는 이너함수()에 그대로 반한: return(*args, **kwargs)
"""
COUNTER = 0

def decorator(other_func):
    global COUNTER
    COUNTER +=1
    print("I'm counting # %s ..."% COUNTER)
    def wrapper(*args, **kwargs):
        print('\n== I am The Wrapper # %s ==== !'% COUNTER)
        return other_func(*args, **kwargs)
    return wrapper





# @decorator
def this_func():
    this_args = 'this is a vass'
    return this_args

# @decorator
def that_func():
    that_args = "That's the decorator"
    return that_args

# @decorator
def those_func(greeting):
    those_args = "'{}' Those args were applied!".format(greeting)
    return those_args

# @decorator
def these_those_func(greeting, date, name='name', age=0):
    these_those_args = "..'{}'..{} {} is age of '{}'".format(
        greeting, date, name, age, )
    return these_those_args



# delete '@decorator' defore running : '@데코레이터'를 삭제하고 실행.
def if_without_decorator():
    a = decorator(this_func)
    b = decorator(that_func)
    c = decorator(those_func)
    d = decorator(these_those_func)
    print(a())
    print(b())
    print(c('HELLO WORLD??'))
    print(d('HELLO?', '1999?', name='Kay_baby', age=5))
if_without_decorator()

print('\n\n\n\n')
def if_with_decorator():
    print(this_func())
    print(that_func())
    print(those_func('HELLO WORLD!'))
    print(these_those_func('HI!', '2018!', name='Kay_adult', age=25))
if_with_decorator()
