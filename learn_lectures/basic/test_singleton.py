"""
# Python Korea - http://bit.ly/2GSdzOw
# 싱글턴 패턴을 공부하다 궁금한 점이 생겨 올려봅니다.
# 위의 코드를 실행하면 5개의 print 함수 결과값이 모두 같습니다.
# 하지만 대부분의 경우 super 함수 구현시 super(Singleton, cls)의 형태를 따르는데요.
# 아래 4개가 아니라 맨 위의 코드가 권장되는 특별한 이유가 있을까요?
"""
# -----
# 기본적으로는 super()가 타입과 인스턴스를 받는 함수이기 때문일텐데요. object를
# 상속하느냐 다른걸 상속하느냐에 따라 어떤 경우에는 맞고 어떤 경우에는 틀린코드를
# 짜는 것보단 항상 일관성있게 맞는 코드를 짜는게 유리하기 때문이겠지요. 한편 저도
# 클래스메서드에서 super()를 써본 기억이 나지 않아 찾아보니 이런 글이 있었습니다.
print(__doc__)


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

singleton1 = Singleton()
singleton2 = Singleton()

singleton1.value = 1
print(singleton2.value)
# print 1



class TestSingleton(object):
    def __new__(cls):
        print(super(TestSingleton, cls).__new__)
        print(super(cls, TestSingleton).__new__)
        print(super(TestSingleton, TestSingleton).__new__)
        print(super(cls, cls).__new__)
        print(object.__new__)


test_singletone = TestSingleton()
# <built-in method __new__ of type object at 0x000000007187C580>
# <built-in method __new__ of type object at 0x000000007187C580>
# <built-in method __new__ of type object at 0x000000007187C580>
# <built-in method __new__ of type object at 0x000000007187C580>
# <built-in method __new__ of type object at 0x000000007187C580>
