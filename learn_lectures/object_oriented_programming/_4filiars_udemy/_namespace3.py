"""
* 클래스를 만들어 namespace를 조회한다       __dict__
* 글로벌이름공간 / 로컬이름공간 을 조회한다   __dict__
"""
# 이름공간(namespace)의 검색순서 = LEGB Rules
# - global namespace --> local namespace 순서로 검색
# - 로컬이름공간(L) --> 인클로저(E) --> 글로벌이름공간(G) --> 빌트인(B)


class One(object):
    def __init__(self, x=10, y=20):
        self.first_var = x
        self.second_var = y

    def add(self):
        """ 더한 값을 반환한다 """
        return self.first_var + self.second_var

    def multi(self):
        """ 곱한 값을 반환한다 """
        return self.first_var * self.second_var

    def local(self):
        return locals()

    @staticmethod
    def show_operands(obj):
        print("%s + %s = %s" % (obj.first_var, obj.second_var, obj.add()))
        print("%s x %s = %s" % (obj.first_var, obj.second_var, obj.multi()))


t = One()
# t.show_operands(t)
# 10 + 20 = 30
# 10 x 20 = 200

a = One(1024, 64)
# a.show_operands(a)
# 1024 + 64 = 1088
# 1024 x 64 = 65536


""" 클래스 namespace """
# for _key, _val in One.__dict__.items():
#     print("%-17s %s" % (_key, _val))
# print()

# __module__        __main__
# __init__          <function One.__init__ at 0x000002339EBE3620>
# add               <function One.add at 0x000002339EBE36A8>
# multi             <function One.multi at 0x000002339EBE3730>
# local             <function One.local at 0x000002339EBE37B8>
# show_operands     <staticmethod object at 0x000002339EC01BA8>
# __dict__          <attribute '__dict__' of 'One' objects>
# __weakref__       <attribute '__weakref__' of 'One' objects>
# __doc__           None


# 클래스 namespace _key, _val 을 어싸인 해줘야 활성화 됨
for _key, _val in One.__dict__.items():
    pass

print("Globas == locals? :", globals() == locals())         # True
print("\n\n")


""" 글로벌 namespace """
for _key, _val in globals().items():
    print("%-17s %s" % (_key, _val))
print()

# __name__          __main__
# __doc__
# * 클래스를 만들어 namespace를 조회한다       __dict__
# * 글로벌이름공간 / 로컬이름공간 을 조회한다   __dict__
# __package__       None
# __loader__        <_frozen_importlib_external.SourceFileLoader object at>
# __spec__          None
# __annotations__   {}
# __builtins__      <module 'builtins' (built-in)>
# __file__          C:\Users\ ... \_lecture_OOP\_namespace3.py
# __cached__        None
# One               <class '__main__.One'>
# t                 <__main__.One object at 0x0000024F4EB61C50>
# a                 <__main__.One object at 0x0000024F4EB61CF8>
# _key              a
# _val              a

""" 로컬 namespace """
for _key, _val in locals().items():
    print("%-17s %s" % (_key, _val))
print()
