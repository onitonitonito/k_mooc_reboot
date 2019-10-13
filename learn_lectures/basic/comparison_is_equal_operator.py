"""
# [python] "is" 와 "==" 차이 | Server Side - http://bit.ly/2q6UQsR
# 2016.12.21 17:54    7325
"""
# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.getcwd().partition(root_name)[:2])                    # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------
# 아래 숫자도 마찬가지도 +1로 계산을 하면 값은 같지만 메모리 할당공간이 서로 다르다.
# 'is' 연산자는 포인터(레퍼런스)를 비교하는 연산자이지 데이터를 비교하는
# 연산자가 아니라점을 확인 할 수 있다.
# 고로 is 연산자는 가급적 None, True, False 등을 비교할때 사용하자.
import script_run
import _comparison_operator

def main():
    func_names = get_func_names()
    print(f"EXECUTABLES = {func_names}")
    run_all_executables(func_names)
    pass

def app_01():
    """
    # Python 콘솔실행(cmd)과 Editor실행 결과(주소배치)가 다름
    # 두 결과가 같을 경우 ... 값과 포인터가 서로 동일하다
    """
    a = 3
    b = 2 + 1
    show_comp_id_op(a,b)

    a = "str"
    b = "str"
    show_comp_id_op(a,b)

    a = 257
    b = 257
    show_comp_id_op(a,b)

def app_02():
    """
    #  두 결과가 다를 경우 ... 배치주소(id) 가 다를때만 False 가 나온다
    """
# ... False!!
    a = [1,2,3,4,5]
    b = [1,2,3,4] + [5]
    show_comp_id_op(a, b)

# ... Flase!!
    a = "This is Anfield, This is Anfield, This is Anfield " + str(32)
    b = "This is Anfield, This is Anfield, This is Anfield 32"
    show_comp_id_op(a,b)

def get_func_names():
    """HELPER(): needs this.module """
    func_names = [func for func in dir(_comparison_operator)
                        if func.startswith("app_")
                        ]

    return func_names

def run_all_executables(func_names):
    """HELPER(): needs this.module """
    for i, name in enumerate(func_names, 1):
        print(f"\n\n** METHOD NAME = {i}. {name}() : ")
        func = getattr(_comparison_operator, name)
        print(func.__doc__)
        func()

def show_comp_id_op(a, b):
    """결과 비교포맷"""
    print(f"a = {a}") if str(a).isnumeric() else print(f"a = '{a}' ")
    print(f"b = {b}") if str(b).isnumeric() else print(f"b = '{b}' ")
    print("-----"*10)
    print(f"id comp: {id(a) == id(b)} = {id(a)} / {id(b)}")
    print(f"a == b : {a == b}") # True
    print(f"a is b : {a is b}") # True
    print("\n")


if __name__ == '__main__':
    print(__doc__)
    main()
