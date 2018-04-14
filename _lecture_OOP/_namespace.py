""" 네임 스페이스(NS) 검색 오더 = LEGB Rules
글로벌 NS(Name Space : 이름공간) / 로컬 NS 의 검색순서
: 로컬(L) --> 인클로즈(E) --> 글로벌(G) --> 빌트인(B)
"""

# x = 3
# def my_function():
#     """한 줄씩 해석을 할것 같지만, 실행전 모든 해석을 마치고 바이트 캐시에 저장 함
#     * 해석 중, 로컬 네임스페이스에 x등록하는데, 변수선언(바인딩)이 안되 있음.
#     * 해석 중, 2개의 라인(print(x))이, NonLocalBoundError 을 발생시킴
#     """
#     print(my_function.__doc__)
#     global x            # 로컬변수를 등록하거나, 글로벌 선언을 해줘야 함.
#     print(x)            # 로컬변수가 정의 되지 않음 ---> NonLocalBoundError -> 3
#     x += 3
#     print(x)            # 로컬변수가 정의 되지 않음 ---> NonLocalBoundError -> 6
#     return locals(), globals()
#
#
# local_dict, global_dict = my_function()     # 3, 6을 프린터
#
# # 로컬 NS에 없어서 글로벌 NS 선언값을 가져왔음 : global x 선언
# # 글로벌 NS에서 가져왔으므로, 로컬 NS에 저장된 값은 없다
# print(local_dict)       # {} --> 빈 dict를 반환 한다.
#
# # RuntimeError: dictionary changed size during iteration
# # dict가 iter를 반환해서 사이즈가 줄어들 때, list 함수로 묶는다.
# for _kv in list(global_dict.items()):
#     print("%-15s %s"%_kv)




class One(object):
    market = 'class_one'

    def __init__(self):
        pass


a = One()
b = One()

a.market = 'instance_one_a'


for _kv in One.__dict__.items():
        print("%-15s %s"%_kv)

""" 클래스 네임스페이스 : 클래스 변수(market)을 지정(class_one)했다 """
# __module__      __main__
# market      class_one
# __init__        <function One.__init__ at 0x000002EBA07F3620>
# __dict__        <attribute '__dict__' of 'One' objects>
# __weakref__     <attribute '__weakref__' of 'One' objects>
# __doc__         None



""" 인스턴스 네임스페이스 = 1줄 : 인스턴스 변수(a.market)를 외부에서 추가 """
# market      instance_one

for _kv in a.__dict__.items():
        print("%-15s = %s"%_kv)


""" 인스턴스 네임스페이스 = 0줄 : b 의 네임스페이스(dict)는 비어있다 = 출력안됨 """
for _kv in b.__dict__.items():
        print("%-15s = %s"%_kv)


print("a.market = ", a.market)   # instance_one_a
print("b.market = ", b.market)   # class_one

""" 네임 스페이스 검색순서 :
오브젝트 : #인스턴스 -> #클래스 -> #오브젝트(수퍼)
  스코프 : #로컬 -> # 인클로즈 -> #글로벌 -> 빌트인
"""

print('\n\n\n')
for _kv in globals().items():
    print("%-17s %s"%_kv)
