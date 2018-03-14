""" 다중 상속, 다이아몬드 상속 및 찾는 우선순위 MRO(Method Resolution Order)
"""
class Human(object):
    def greeting(self):
        print("HELLO~ '%s'!" % self.__class__.__name__)


class MaleStudent(Human):
    def greeting(self):
        print("HA-HA~ '%s'!" % self.__class__.__name__)

class FemaleStudent(Human):
    def greeting(self):
        print("HO-HO~ '%s'!" % self.__class__.__name__)


class AllStudent(MaleStudent, FemaleStudent):
    pass

a = Human()
a.greeting()        # HELLO~ 'Human'!

b = MaleStudent()
b.greeting()        # HELLO~ 'MaleStudent'!

c = FemaleStudent()
c.greeting()        # HELLO~ 'FemaleStudent'!

d= AllStudent()
d.greeting()        # 검색 우선순위 : 인스턴스-클래스 / 왼쪽 - 오른쪽

""" 찾는 우선순위 MRO(Method Resolution Order) """
# 찾는순서(mro) = All-Male-Female-Human-object
for order in d.__class__.__mro__:
    print(order)

# 찾는순서(mro) = Female-Human-object
for order in c.__class__.__mro__:
    print(order)

# 찾는순서(mro) = Male-Human-object
for order in b.__class__.__mro__:
    print(order)

# 찾는순서(mro) = Human-object
for order in a.__class__.__mro__:
    print(order)
