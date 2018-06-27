"""
* section.07 - lecture.18
* The Diamond Shape Problem in Mutiple Inheritance
* ............(A)
* ......(B)..........(C)
* ............(d)
"""


class A(object):
    def method(self):
        comment = "This methood -- belong to CLASS-(A)"
        print(comment)
    pass


class B(A):
    pass


class C(A):
    def method(self):
        comment = "This methood -- belong to CLASS-(C)"
        print(comment)
    pass


class D(B, C):
    pass



d = D()
d.method()
