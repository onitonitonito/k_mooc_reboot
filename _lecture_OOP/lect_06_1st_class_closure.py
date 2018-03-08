""" 클로저 함수() : Nested Function (적층, 고차함수)
  '클로저'란 1st.Class함수의 '네임바인딩'기술로서. 클로저는 어떤 함수(inner)를 환경
   과 함께 저장한 레코드. 프리변수(free variable)를 클로저가 만들어지는 당시의 값과
   레퍼런스에 맵핑하여 주는 역할을 한다.

  - 껍데기(래퍼함수)가 알맹이에 값을 전달해주고,
  - 알맹이(이너함수)결과를 함수보디 형태로 반환한다 -- 변수에 할당하면 변수가 함수
  - 알맹이(이너함수)의 반환값을 기억한다(?) -- 어디에? 클로저(셀)에 저장
  - 알맹이(이너함수)가 종료해도 클로저셀에 저장 해뒀기 때문에 반복호출(?) 가능하다.
  - refer : http://jonnung.blogspot.kr/2014/09/python-easy-closure.html
  - refer to : SchoolOfWeb = https://goo.gl/CmMaqo : 파이썬 '클로저'
"""
import _script_run_utf8
_script_run_utf8.main()

""" 1급 클래스 함수()와 클로저(): (1급 시민이란? 함수와 객체클래스를 모두 받음)
x,y 를 받아서 내부함수로 전달
내부함수는 x+y를 합해서 외부함수로 전달
....
클로져 함수()를 만드는 순서
  - 1.외부함수 정의 (자유변수 정의) : 자유변수란 코드블럭, 외부에서 정의된 변수
  - 2.내부함수 정의 (자유변수를 받아서 사용)
  - 3.내부함수 결과를 외부로 전달 (외부함수 환경 공유)
  - 4.전달받은 내부함수(결과)를 호출한 곳에 반영 (실행)
"""


# define outter function : 인수를 받아서 내부로 전달
def closure_out(x, y):
    # define inner function : 인수를 가공해서 외부로 반환
    def closure_in():
        return x+y
    # deliver function : 반환한 인수를 받아서 또, 외부로 전달
    return closure_in

_="""1. 클로저 함수의 실행방법 : 변수에 2차함수를 할당하면, 변수가 함수가 됨 """
print(_)
close = closure_out(5, 10)  # 내부에서 받은 x+y를 반환한다
print("  close 가 함수가 된다 = %s\n" % close())              # return closure_in() = 5+10 = 15

_="""2. __closure__ 매서드는 튜플, 'int'값의 셀 오브젝트를 가지고 있음 """
print(_,"\n__closure__ 갯수 = %s"% len(close.__closure__))
print("  첫번쩨 클로저 셀 = ", close.__closure__[0].cell_contents)   # 5
print("  두번째 클로저 셀 = ", close.__closure__[1].cell_contents)   # 10




def logger(msg):
    def say_msg():
        print('say=', msg)
    return say_msg

_="""3. 함수가 2중으로 쓰워진 상태 = 호출해서, 변수에 할당하면, 그것이 함수 """
print('\n'+_)
log_hi = logger('Hi~!')     # log_hi() 가 함수가 된다.
print(log_hi)               # '함수보디' 와 '주소'가 표시된다.
# log_hi()        # Method which runs logger('hi~!') function

print(logger('hihi'))
a = logger('hihi')





def say_hello(name):            # '클로저' = 고차함수(2차함수)
    trail_msg = 'good morning!'
    def helper():               # 이너함수(), or 핼퍼함수()
                                # 껍데기가 전달한 값을 사용한다
        print('Hello %s, '% name + trail_msg)
    return helper               # 함수보디를 반환한다.


_="""1. 두곂으로 쌓인 껍데기는 버려도 된다, 알맹이(?) 버리면 에러발생 """
print('\n'+_)
_a = say_hello('Jung-Eun')      # a = return value (function object)
_a()                            # function call
# del helper                      # delete function object
del say_hello
_a()                            # delete function object



_="""2. 함수'바디'를 반환할 때 -고차함수의 실행순서 (호출순서 참조)
  - 함수바디를 반환한다 - 변수에 할당할때, 변수가 '함수'가 된다.
  - 함수()결과를 반환한다 - 변수에 할당할때, 변수가 '결과값'이 된다.
"""
print('\n'+_)

def outer_func():           #1
    message = '  ex.1 = Foo!' #3 = free variable
    def inner_func():       #4
        print(message)      #6
    return inner_func()     #5 - 차이점1: 함수()를 반환할 때
outer_func()                #2

_b = outer_func           #
_b()                      # 결과'값'을 반환했기 때문에 이제, 이렇게는 안된다.
# del inner_func              # 알맹이 = 버리면 안됨.
del outer_func              # 껍데기 = 버려도 유효함
_b


_="""3. 함수()반환값을 반환할때 """
print('\n'+_)

def outer_func1():          #1
    message = '  ex.2 = Bar!' #3 = free variable
    def inner_func1():      #4
        print(message)      #6
    return inner_func1      #5 (!) not call, only object return
outer_func1()                #2


_c = outer_func1()           #
_c()
# del inner_func1              # 알맹이 = 버리면 안됨.
del outer_func1              # 껍데기 = 버려도 유효함
_c()








_="""------ 본격!!! 클로저 함수() 예제 엄선!!! ----------------
"""
print('\n\n\n'+_)

_="""1a. 일반함수로는 재활용에 제약이 있다 (1가지 형식만 재활용)"""
print(_)

def simple_html_tag(tag, msg):
    print ('  <{0:}>{1:}</{0:}>'.format(tag, msg))
    print ('  <{tag_name:}>{content:}</{tag_name:}>'.format(tag_name=tag, content=msg))
simple_html_tag('h1', 'THIS-IS-HEAD-TITLE')




def tag_name(html_tag):
    def wrapper(content):
        print('  <{0:}>{1:}</{0:}>'.format(html_tag, content))
        return '확인! = 이너함수()의 반환값'
    return wrapper          # 함수'바디'를 반환

_="""2a. 클로저 함수()를 쓰면 배리에이션이 가능하다 (다양한 형식에 재활용)"""
print('\n'+_)
h1 = tag_name('h1')     # h1 변수에 '레퍼함수(껍데기함수)'를 전달한다 - '함수바디'
h1('H1-HEAD-TITLE')     # h1 변수를 '함수'로서 호출한다

get_h1 = h1('H1-QUESTION')  # h1 변수가 '함수'로써 반환한 값을 get_h1에 저장
print("\n  레퍼함수의 반환 값 : ", get_h1)
print(type(h1('함수도 실행하고, 값도 반환받고...')))          # <class 'NoneType'>




_="""3a. '리스트' 와 '집합'의 동시 교차정렬 (키값을 활용하여 앞/뒤 정렬)
 - 집합 = 홀수 ('집합'은 순서가 없는 데이터)
 - 리스트'정렬' 키값 쓰는법(참조)
 - a.sort(key=), sorted(a,ke=) 둘다 쓸 수 있음
 - 파이썬3.6 도큐멘테이션(참조) : https://docs.python.org/3/howto/sorting.html
"""
print('\n'+_)

numbers = [8, 3, 1, 2, 5, 4, 7, 6,]     # '리스트' <class 'list'> - 1 to 8
sets = {1, 7, 5, 3}                     # '집합' <class 'set'> - 홀수

def sort_priority(numbers, sets):
    def helper(x):
        if x in sets:
            return False, x         # '넘버스'가 '집합'에 있으면 0,x 반환 - 홀수면
        return True, x             # '넘버스'가 '집합'에 없으면 1,x 반환 - 짝수면
    numbers.sort(key=helper)    # '넘버스'를 정렬 할 때, 헬퍼()우선정렬

numbers.sort()                  # [1, 2, 3, 4, 5, 6, 7, 8] -경우1.일반정렬
print("  일반 정렬 = ", numbers)

sort_priority(numbers, sets)    # [2, 3, 5, 7, 1, 4, 6, 8] -경우2.클로저정렬
print("  Key값 정렬= ", numbers)
