""" 부모 메서드 사용: 수퍼() 또는 클래스 매써드(self) 호출한다. """
# super().__init__()                        # Parent init called
# super(Child, self).__init__()               # Parent init called
# super(self.__class__, self).__init__()    # Parent init called

""" 자식 -> 부모 '매서드' 호출가능 / 부모 -> 자식'매서드' 호출가능 할까? """
# 부모()


def test1_failed():
    class Parent(object):
        def __init__(self):
            print('부모 - 초기화 실행됨 (부모생성)')

        def call_child_method(self):
            self.child_method()

    class Child(Parent):
        def __init__(self):
            print('자식 - 초기화 실행됨 (자식생성)')
            # super().__init__()          # Parent init called
            Parent.__init__(self)            # Parent init called

        def child_method(self):
            print('자식 매서드가 실행 됨')

    ch = Child()
    ch.call_child_method()      # '상속'을 받았기 때문에 '자식 매서드가 실행 됨'

    """ 부모입장에서 자식 매서드 호출 = 'self'는 말이 안됨. 누구냐? 이거? """
    pa = Parent()
    # pa.call_child_method()   # ... self.child_method()    으읭??
    # AttributeError: 'Parent' object has no attribute 'child_method'


def test2_successful():
    class Parent(object):
        x = None                # default value

        def __init__(self):
            print(self.x)

        def call_every_children(self):
            SomeChild.parent_called(self)
            OtherChild.parent_called(self)

    class SomeChild(Parent):
        x = 10

        def __init__(self):
            Parent.__init__(self)

        def parent_called(self):
            print('I heard, my parent called --SomeChild--')

    class OtherChild(Parent):
        x = 20

        def __init__(self):
            super().__init__()
            # super(OtherChild, self).__init__()

        def parent_called(self):
            print('I heard, my parent called --OtherChild--')

    pr = Parent()           # output: None
    sc = SomeChild()        # output: 10
    oc = OtherChild()       # output: 20

    pr.call_every_children()


# test1_failed()
test2_successful()
