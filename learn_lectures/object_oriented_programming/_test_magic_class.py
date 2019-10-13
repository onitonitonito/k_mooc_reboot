"""
# magic methods test!
# [번역] 파이썬 매직 메소드 (Python's Magic Methods)
# 2017-01-30
# https://ziwon.dev/post/python_magic_methods/
"""
# print(__doc__)

class TestClass(object):
    """ this is magic method test! """

    def __init__(self):
        """ 인스턴스 호출시 제일 먼저 실행 """
        print("init!")

    def __main__(self):
        self.test_test(7)
        self.read_read(3)
        return True

    def __str__(self):
        """ __repr__ 보다 우선순위 """
        return "-- magic string --"

    def __repr__(self):
        """ 인스턴스를 프린트할 때, 주소가 아닌 설명을 출력 """
        return "-- representives --"

    def test_test(self, n):
        """ 01.첫번째 함수 """
        print("test_test! " * n)

    def read_read(self, n):
        """ 02.두번째 함수 """
        print("read_read! " * n)


def main():
    print('out main')

    tc = TestClass()
    print(tc.__repr__)
    print(tc.__str__)
    print(tc)

    tc.__main__()


    # AttributeError: type object 'TestClass' has no attribute '__main__'
    # TypeError: __main__() missing 1 required positional argument: 'self'


if __name__ == '__main__':
    main()
