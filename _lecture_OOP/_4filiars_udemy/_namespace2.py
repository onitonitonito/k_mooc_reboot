"""
* 클래스와 인스턴스의 네임스페이스 비교
* 파이썬 알고리즘 트레이딩 = https://wikidocs.net/1743
"""
# 이름공간(namespace)의 검색순서 = LEGB Rules
# - global namespace --> local namespace 순서로 검색
# - 로컬이름공간(L) --> 인클로저(E) --> 글로벌이름공간(G) --> 빌트인(B)


class Stock(object):
    market = "KOSPI"


dirs = dir(Stock)
print(dirs, "\n\n")

# print("\n".join(dirs))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'market']


print("Stock=", Stock)          # <class '__main__.Stock'>
