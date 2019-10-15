"""
# [Python] global / nonlocal
# https://devbruce.github.io/python/py-13-global,nonlocal/
# 글로벌 변수를 선언해야 하는 경우를 알아본다
"""
# global / nonlocal
#   - 지역변수를 전역변수에 영향을 줄 수 있도록 해주는 명령어
#   - global 명령어는 사용하지않는 것을 권장

import assets.script_run

print(__doc__)
a = 1


def just_show_a():
    """ O.K - only refer a """
    print(f"a = {a}")


def change_local_a():
    """ UnboundLocalError: local variable 'a' referenced before assignment """
    global a
    a +=1
    just_show_a()


def main():
    just_show_a()
    change_local_a()
    change_local_a()
    change_local_a()
    change_local_a()


x = 15  # 전역변수 (global variable)
def f():
    """ 지역변수는 전역변수에 영향을 주지못한다 """
    x = 30  # 지역변수 (local variable)

f()
# print(x) # 15
# ------------------------------------------------------------

x = 15  # 전역변수 (global variable)
def g():
    global x   # 지역변수가 전역변수를 사용하게 선언
    x = 30     # 지역변수 (local variable)


g()
# print(x) # 30
# ------------------------------------------------------------


x = 15  # 전역변수 (global variable)
def f():
    x = 30
    def g():
        x = 60
        def h():
            global x
            x = 120
        h()
    g()


f()
# print(x) # 120
# ------------------------------------------------------------


x = 20 # 전역변수 (global variable)
def f():
    x = 40
    def g():
        nonlocal x
        x = 80

    g()  # 함수 g를 실행하여 nonlocal이 적용되도록 한다.
    print(x)  # 함수 f에서의 x값이 출력된다.(함수 g에서 nonlocal 의 영향을 받아 변수가 80으로 변경되었다.)
    return x

# f() # 80
# print(f()) # 80, 80
# print(x)  # 모든 함수 실행이 끝나고, 변수 x를 출력한다.(출력값은 처음값인 20이다)
# ------------------------------------------------------------




# nonlocal 은 아래와 같이, 함수 한개를 정의하고 전역변수에 영향을 주게 하는 것은 안된다.
x = 70  # 전역변수 (global variable) ... 전역변수가 nonlocal 선언에 영향받음

def f():
    # nonlocal x  # 그러므로, 에러 발생 ... no binding for nonlocal 'x' found
                # nonlocal 을 쓸수 없는 상황 ... Syntax Error
    x= 140

f()
# print(x)
# ------------------------------------------------------------


# global, nonlocal 혼용사례
x = 50
def f():
    a = 777
    def g():
        a = 100
        def h():
            global x
            x = 999
            nonlocal a
            a = 333
        h()
        print(f"[Level 2] a = {a}") # 333 넌로컬 선언
    g()
    print(f"[Level 1] a = {a}") # 777 아무선언 없으므로 현단계 전역변수 값 사용

f()
print(f"[Level 0] x = {x}")   # 999 글로벌 선언,
