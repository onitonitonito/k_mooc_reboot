"""
* Section.07 - Lecture.18
* The Diamond Shape Problem in Mutiple Inheritance
* .........(A)
* ...(B)..........(C)
* .........(d)
"""


class A(object):
    def method(self):
        comment = "This methood -- belong to CLASS-(A)"
        print(comment)
    pass


class B(A):
    def method(self):
        comment = "This methood -- belong to CLASS-(B)"
        print(comment)
    pass


class C(A):
    def method(self):
        comment = "This methood -- belong to CLASS-(C)"
        print(comment)
    pass


class D(B, C):
    """ 방법 : 순서대로 매서드를 추가해서 실행 함 (A), (C), (B)
    B가 없을 때 - (A), (C) 충돌 때는 직계(C)를 상속 함
    같은 직계레벨 (B), (C)가 충돌, (B)를 상속 받음 (검색순서 나열)
    """
    pass



d = D()
d.method()
