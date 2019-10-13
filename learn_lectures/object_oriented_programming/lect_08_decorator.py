"""------------------------------------ 세션.1 클로저 함수()
  refer to SchoolOfWeb = https://goo.gl/XdOvVv : 파이썬 데코레이터
  - 적층된 이차함수(고차함수) : nested double functions
  - 레퍼(이너)함수는 아우터 함수의 인사를 받는다: inner() uses outer function args.
  - return inner(wrapper) function object
  - 클로저() + 일반함수()가 데코레이터의 포맷이 된다.
"""

def outer(args):
    def inner():
        print(args)
    return inner

_="""1. 일반적인 클로저 함수()의 실행 방법
 - #1. 변수에 클로저 함수()를 할당한다.
 - #2. 변수()를 함수화 하여 호출한다.
"""
print('\n'+_)
hi_func = outer("  * hi_func = " + 'Hi~!!')    #1
bye_func = outer("  * bye_func = " + 'Bye~!')  #1
hi_func()                                            #2
bye_func()                                           #2




"""------------------------------------ 세션.2 데코레이터 함수()
 - 오리지날 함수()를 래퍼(이너)함수에서 호출()로 반환 한다.
 - 데코레이터 함수()는 래퍼(이너)함수의 몸통(바디)을 반환한다
"""
def decorator(original_function):      #1
    def wrapper():                     #2
        return original_function()              #7
    return wrapper                     #6

def display():                                  #2
    print('DISPLAY function is activated!...')


_="""2. 적층함수()를 생각해보자 : 클로저 함수() + 함수()를 인자로 추가 - 3차 함수()
 - #1. 클로저 함수()를 만든다. -- 2차 함수
 - #2. 일반 함수()를 만든다 -- 1차 함수
 - #3. 변수에 클로저(일반함수'바디')를 곂쳐 할당 -- 클로저()가 퍼스트클래스()
 - #4. 변수()를 함수화 하여 호출한다. -- 클로저 호출방식(But, 이것은 3차 함수)
 - #5. 일반함수()도(?) 원래대로 호출 가능하다.
"""
print('\n\n'+_)
decorated_display = decorator(display) #3

print('  #4: 3차함수 실행 = ', end='')
decorated_display()                           #4 - 클로저를 거쳐 나온 함수
print('  #5: 1차함수 실행 = ', end='')
display()                                     #5 - 원래의 일반 함수()






"""--------------------------------------- SESSION 03---
"""
def decorator(original_function):
    def wrapper():
        print("  (1) 저는 '%s'클로저의 장식자입니다..."% (original_function.__name__))                     #2
        return original_function()              #7
    return wrapper                     #6

def display_01():               #2
    print("  (2) 일반함수() 'display_01' 이 실행되었습니다.!...\n")

def display_02():               #2
    print("  (2) 일반함수() 'display_02' 이 실행되었습니다.!...\n")

_="""3. 데코레이터() : 1차함수 실행 전, 장식자(이너함수) 실행 함.
 - #1. 클로저 장식함수()에 1차함수()를 더함 = 3차 함수
 - #2. 변수를 만들어 합쳐진, 3차 함수를 할당 한다.
 - #3. 변수()를 호출하면 2단으로 작동 함.
    (1) 첫번째, 클로저의 이너함수()는 먼저 실행 됨 - 장식자입니다
    (2) 두번째, 원래 함수()가 실행 됨. -- 여기선, '프린트'
"""
print('\n\n'+_)
display_01 = decorator(display_01)         #1
display_02 = decorator(display_02)         #1

display_01()    # 3차 함수클로저 = 함수2개가 작동 함 (2번 작동)
display_02()





"""--------------------------------------- SESSION 04---"""
def decorator(original_function):
    def wrapper():
        print("  '%s' function is NOT activated..."% (original_function.__name__))                     #2
        return original_function()              #7
    return wrapper                     #6

@decorator             #1
def display_01():               #2
    print('  - display_01 function is activated!...\n')

@decorator             #1
def display_02():               #2
    print('  - display_02 function is activated!...\n')

_="""4. '@데코레이터'를 붙이면 @함수()인자로 쓰겠다는 의미 : '@'붙이는 이유는?
   - 3차함수의 인자로 쓰일 함수()가 분명하게 보인다  .. 너! 인자구나
   - 3차함수의 인자로 자동 대입해준다 (인자를 쓸 필요 없음.)
   - 1차함수를 실행시키면 자동으로 데코함수()의 인자로써 실행한다 -- 완전자동!
  def somefunc_name()         ... 데코함수()
  @somefunc_name              ... 데코레이터'@' + 데코함수명
  def otherfunc()             ... 바로 아래 일반함수()는 자동으로 대입된다.

  -- 실행 방법은? :
  otherfunc()  ... otherfunc()를 실행하면, 자동 '데코함수'부터 실행된다.
"""
print('\n\n'+_)
display_01()            # .. 데코함수()의 인자로 대입해서 실행한다.
display_02()



"""--------------------------------------- SESSION 05---"""
'''' wrapper has no arguments but 2 given : Error '''
def decorator(original_function):
    def wrapper(*args, **kwargs):
        print("  ?.'%s' function is NOT activated..."% (original_function.__name__))                     #2
        return original_function(*args, **kwargs)              #7
    return wrapper                     #6

@decorator             #1
def display_03():               #2
    print('  ?.DISPLAY(_03_) function is activated!...\n')

@decorator             #1
def display_info(name, age):
    print('  ?.DISPLAY_INFO(%s, %s) function is activated...\n' %(name, age))

_="""5. 다양한 @데코레이터의 변종활용 해보자!
  - 1차 함수에 인자를 더하는 순간!, 'TypeError'가 발생함!!.. 왜?
   TypeError: wrapper has no arguments, but 2 given !
    -> 뭔가 이너함수(래퍼함수)에 조치가 필요하다 -- 만능인자: *args, **kwargs
"""
print('\n\n'+_)
display_03()
display_info('제이콥', 24)



"""--------------------------------------- SESSION 06--CLASS-"""
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('  ** {} function is NOT activated...'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass     #2
def display_03():               #2
    print('  = DISPLAY(_03_) function is activated!...')

@DecoratorClass     #3
def display_info(name, age):
    print('  = DISPLAY_INFO({}, {}) function is activated...'.format(name, age))


_="""6.클래스로 데코레이터(클래스)를 정의해 보자 (3가지로 정의)
  - 동일한 효과, 동일한 방식, 데코레이션 함수가 아닌 클래스로 정의
  - __init__ : 오리지널 평션을 인자로 불러서, self.func = func 로 저장한다.
  - __call__ : (self, *args, **kwargs) 자동실행 함수로 정의 (가변인자)
  - 호출의 리턴값으로 저장된 self.func(*args, **kwargs) 로 돌려준다.
"""
print('\n\n'+_)
display_03()
print()
display_info('제이콥', 24)