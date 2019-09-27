"""
# [코드잇] 파이썬에서 하기 쉬운 실수 #1 네임 스페이스 - http://bit.ly/2mye496
# 온라인 코딩 스쿨 / 2019. 9/23. 18:00 ... (전역변수/지역변수)
"""
# print(__doc__)
#
#


#first_example.py
x = 1               # ... (c) : Global namespace
def func_1():
	print(x)

func_1()            # 1 ... : Global namespace
print(func_1.__dict__)


#second_example.py
def func_2():
    """
    newly set L/N
    """
    x = 2          # ... (b) : Local namespace (newly assigned)

func_2()            # ... commit set Local namespace (newly)
print(x)            # 1 ... : Global namespace
print(func_2.__dict__)



#third_example.py
def func_3():
    """
    (d)처럼 쓰게되면 이제 전역 네임 스페이스
    에 있는 변수 x를 사용하겠다고 선언.

    하지만 프로그램에서 사실 global 키워드를 자주 쓰는 건 바람직하지 않습니다.
    프로그램의 여러 함수에 (d)처럼 x를 건드리는 부분이 있다면 x가 어떤 이유로,
    어떤 순서로 변하는지 파악하기가 힘듭니다.
    """
    global x       # ... (d) claim to use G/N inside func_3()
    x = 3          # ... change Global namespace



"""
# [코드잇] 파이썬에서 하기 쉬운 실수 #2 네임 스페이스 - http://bit.ly/2liYZrG
# 온라인 코딩 스쿨 / 2019. 9/26. 14:00 ... (Nonlocal)
"""
# print(__doc__)
# 전역 네임 스페이스의 변수는 global,
# 현재 위치보다 더 상위지역 네임스페이스 변수는 nonlocal
#

#first_example.py
def outer_func():
	x = 1             # ... (a)
	def inner_func():
		nonlocal x    # ... (e)
		x = 2         # ... (b)

	inner_func()
	print(x)          # ... (c)



func_3()           # ... commit change method()
print(x)           # 3 ... : Global namespace
print(func_3.__dict__)

outer_func()          # w/o nonlocal=1 / w/ nonlocal=2
