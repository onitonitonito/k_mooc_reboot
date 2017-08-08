class MyClass(object):
    def __init__(self):
        self.field_public = 5
        self.__field_private = 15

    def get_field_private(self):
        return self.__field_private

    @classmethod
    def get_field_private_of_instance(clas, instance):
        return instance.__field_private


class MyClassChild(MyClass):
    """ child function can not access parent's private value. """
    def get_field_private(self):
        # 'MyClassChild' object has no attribute '_MyClassChild__field_private'
        # return self.__field_private         # ERROR
        return "CAN BE ACCESSIBLE"

def main():
    _foo = MyClass()
    _bar = MyClass()
    assert _foo.field_public == 5
    assert MyClass.get_field_private_of_instance(_bar) == 15

    print(_foo.field_public)        # 5, always accessivle!!
    print(_foo.get_field_private()) # 15, difficult, but accessivle
    # print(_foo.__field_private) # 'MyClass' has no attribute '__field_private'

    _barz = MyClassChild()

    parent_private = _barz.get_field_private()
    print(parent_private)               # return 'str' = "CAN BE ACCESSIBLE"
    """ CALLABLE = instance._class__private_value """
    print(_barz._MyClass__field_private)# 15 , able to access to private value!!
    print(_bar._MyClass__field_private) # 15 , able to access to private value!!
    print(_bar.field_public)            # 5
    print(_bar.__dict__)    # {'field_public': 5, '_MyClass__field_private': 15}
# main()

""" Mangle Method = Double underscore """
class A(object):
    _b = 10
    _bb = 20
    _bbb = 30
    def __init__(self):
        self._a = 5
        self._aa = 10
        self._aaa = 15

    def _single_method(self):
        pass

    def __double_method(self): # mangling method
        pass


class B(A):
    def __double_method(self): # mangling method
        pass

""" The same names are being distinctive, Not be overrided
   _class__double_name : _A__double_method / _B__double_method
 """
print(dir(A())) # ['_A__double_method', ..., '_single_method']
print(dir(B())) # ['_A__double_method', '_B__double_method', .. '_single_method']

print(A().__dict__)     # {'_a': 5, '_aa': 10, '_aaa': 15}
print(B().__dict__)     # {'_a': 5, '_aa': 10, '_aaa': 15} - inherited -

_a = B()

print(_a._a)                #5
print(_a._aa)               #10
print(_a._aaa, end='\n\n')  #15

print(_a._b)                #10
print(_a._bb)               #20
print(_a._bbb, end='\n\n')  #30


""" POINTS & LESSONS
 - private attribute (__a ) are not that strict, be able to access
 - use protective attribute (_a) and show how to use to subclass.
 - only if you want mangle method, use private value (__a) to prevent.
"""
