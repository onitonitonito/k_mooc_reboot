"""  _dict = inspect.currentframe().f_back.f_locals
 - 클래스와 관련된 모든 정보가 담긴 'dict'를 반환 한다.
 - 필요에 따라서 골라 쓰면 됨.
"""
import inspect


class Animal(object):

    def __init__(self, name, kind, color):
        self.name = name
        self.kind = kind
        self.color = color

    def show_my_name(self):
        # '클래스'관련 모든 정보가 'dict'형태로 반환 됨.  --- 중요!
        _dict = inspect.currentframe().f_back.f_locals

        # keys = _dict.keys()     # inst_name
        # values = _dict.values() # __main__

        print(_dict, end='\n\n\n')

        for key, value in _dict.items():
            # Animal <class '__main__.Animal'>
            if key == self.__class__.__name__:
                print(key, value)

            # aa <__main__.Animal object at 0x00000200332AF160>
            if isinstance(value, self.__class__):
                print(key, value)       # key = <class 'str'>


aa = Animal('Ai','dog', 'white')
bb = Animal('Jay','dog', 'black')
cc = Animal('Kay','cat', 'pink')

aa.show_my_name()
