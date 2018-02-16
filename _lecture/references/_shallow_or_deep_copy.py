""" SHALLOW COPY vs. DEEP COPY
 (1) Shallow copy =
 (2) Deep copy =
 """

import copy

def test1_mutable_object():
    """ 'list' = mutable OBJECT, if changes, affects both """
    _a = [1, 2, 3, [4, 5, 6]]
    _b = _a
    print('_a = ', _a)
    print('... chage \'_b\' = 100 \n')

    _b[0] = 100

    print('_a = ',_a)
    print('_b = ',_b)
    """
    _a =  [100, 2, 3, [4, 5, 6]]
    _b =  [100, 2, 3, [4, 5, 6]]
    """

def test2_immutable_object():
    """ 'str' or 'int' = immutable OBJECT(not changeable),
    the changes are not affects to one another
    """
    _c = 100
    _d = _c
    print('_c = ', _c)
    print('... chage \'_d\'= 200 \n')

    _d = 200
    print('_c = ',_c)
    print('_d = ',_d)
    """
    _c =  100
    _d =  200
    """

def main_comparison():
    test1_mutable_object()
    print('\n\n')
    test2_immutable_object()
# main_comparison()




a = [1, [1, 2, 3]]
b = copy.copy(a)    # shallow copy 발생

print('a= ', a)
print('b= ', b)    # [1, [1, 2, 3]] 출력
print('... change... b[0] = 100')
b[0] = 100
print('a= ', a)
print('b= ', b)    # [100, [1, 2, 3]] 출력,
print('\n\n\n')

# [1, [1, 2, 3]] 출력, shallow copy 가 발생해 복사된 리스트는
# 별도의 객체이므로 item을 수정하면 복사본만 수정된다. (immutable 객체의 경우)

print('a= ', a)
c = copy.copy(a)
print('c= ', c)
c[1].append(4)    # 리스트의 두번째 item(내부리스트)에 4를 추가
print('... change... c[1].append(4) ')
print('c= ', c)    # [1, [1, 2, 3, 4]] 출력
print('a= ', a)
# [1, [1, 2, 3, 4]] 출력, a가 c와 똑같이 수정된 이유는
# 리스트의 item 내부의 객체는 동일한 객체이므로 mutable한 리스트를
# 수정 할 때는 둘다 값이 변경 됨


print('\n\n\n')

a = [1, [1, 2, 3]]
b = copy.deepcopy(a)    # deep copy 실행

print('a= ', a)
print('b= ', b)
b[0] = 100
b[1].append(4)
print('a= ', a)
print('b= ', b)

"""
정리해보면,
    1.단순복제는 완전히 동일한 객체,
    2.얕은복사(shallow copy)는 복합객체(껍데기)만 복사, 그 내용은 동일한 객체
    3.깊은복사(deep copy)는 복합객체 복사 + 그 내용도 재귀적으로 복사
"""
