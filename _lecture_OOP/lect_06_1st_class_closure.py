""" 1st. Class function and Decorater
x,y 를 받아서 내부함수로 전달
내부함수는 x+y를 합해서 외부함수로 전달
....
Closure 함수를 만드는 순서
  - 1.외부함수 정의 (자유변수 정의)
  - 2.내부함수 정의 (자유변수를 받아서 사용)
  - 3.내부함수 결과를 외부로 전달 (외부함수 환경 공유)
  - 4.전달받은 내부함수(결과)를 호출한 곳에 반영 (실행)
"""
import _script_run_utf8
_script_run_utf8.main()


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
print("close 가 함수가 된다 = %s\n" % close())              # return closure_in() = 5+10 = 15

_="""2. __closure__ 매서드는 튜플, 'int'값의 셀 오브젝트를 가지고 있음 """
print(_,"\n__closure__ 갯수 = %s"% len(close.__closure__))
print("첫번쩨 클로저 셀 = ", close.__closure__[0].cell_contents)   # 5
print("두번째 클로저 셀 = ", close.__closure__[1].cell_contents)   # 10

def logger(msg):
    def say_msg():
        print('say=', msg)
    return say_msg

_=""" 3. 함수가 2중으로 쓰워진 상태 = 변수에 할당하면, 그것이 함수 """
print('\n'+_)
log_hi = logger('Hi~!')     # log_hi() 가 함수가 된다.
print(log_hi)               # '함수보디' 와 '주소'가 표시된다.
# log_hi()        # Method which runs logger('hi~!') function

print(logger('hihi'))
a = logger('hihi')
