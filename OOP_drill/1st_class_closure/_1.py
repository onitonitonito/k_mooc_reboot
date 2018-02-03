"""
# 1st Class function and Decorater

x,y 를 받아서 내부함수로 전달
내부함수는 x+y를 합해서 외부함수로 전달
=====
Closure 함수를 만드는 순서
  - 1.외부함수 정의 (자유변수 정의)
  - 2.내부함수 정의 (자유변수를 받아서 사용)
  - 3.내부함수 결과를 외부로 전달 (외부함수 환경 공유)
  - 4.전달받은 내부함수(결과)를 호출한 곳에 반영 (실행)
"""
# define outter function
def closure_out(x, y):
    # define inner function
    def closure_in():
        return x+y
    # deliver function
    return closure_in

close = closure_out(5, 10)
print(close())              # return closure_in() = 5+10 = 15
print(close.__closure__[0].cell_contents)   # 5
print(close.__closure__[1].cell_contents)   # 10

def test1_closer():
    def logger(msg):
        """ 1st class function,
        # arg(msg) will remains after (return:end)
        """
        def say_msg():
            print('say=', msg)

        return say_msg()

    # log_hi = logger('Hi~!')
    # print (log_hi)  # show OBJECT(say_msg) - instance & address
    # log_hi()        # Method which runs logger('hi~!') function

    print(logger('hihi'))
    a = logger('hihi')
