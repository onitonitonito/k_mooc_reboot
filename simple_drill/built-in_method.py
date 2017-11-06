""" Bulit-in Special Method ... __something__
    __str__  = return 'str'
    __repr__ = return 'str'
    __getitem__ = being called self[key]
    __delitem__ = being called self[key]
"""

class Complex(object):   # Run first, initialize class.
    """ (1) assing self.r = real, self.i = image"""
    def __init__(self,arg_real, arg_imagin):
        self.r = arg_real
        self.i = arg_imagin
#c = Complex(1,2)       # 1 = real, 2=imagin
#print(c)            # <__main__.Complex object at 0x021CC5F0> Memory Address


class Complex2(Complex): # explanation string
    def __str__(self):
        return "[str] " + self.__repr__()

    def __repr__(self): # more descrete string
        return "Complex number: real=%0.2f, imagin=%0.2f" %(self.r, self.i)
# c2 = Complex2(3,4)     # 3 = real, 4 = imagin
# print(c2)              # [str] Complex number: real=3.00, imagin=4.00
# print(__str__(c2))     # [str] Complex number: real=3.00, imagin=4.00


class Complex3(Complex2):
    def __getitem__(self, key):     # c3['r'], c3['i'] = available
        if key == 'r':
            return self.r
        if key == 'i':
            return self.i

    def __delitem__(self, key):     # if del(c3['r'], c3['i'])
        if key == 'r':
            self.r = 0
            # print("DELETE r...")
        if key == 'i':
            self.i = 0
            # print("DELETE i...")

def test1_BI_function():
    """ Built-In function test... """
    c3 = Complex3(5,6)  # real = 5, imagin = 6
    #print(c3)           # [str] Complex number: real=5.00, imagin=6.00
    #print(c3['r'])      # 5
    #print(c3['i'])      # 6

    #print()
    #print(c3.r)         # 5
    #print(c3.i)         # 6

    print(str(c3))
    print(repr(c3))
    print('real   = ', c3['r']) # 5
    print('imagin = ', c3['i']) # 6

    del(c3['r'])
    print(str(c3))

    del(c3['i'])
    print(str(c3))
test1_BI_function()

def test2_difference_str_repr():
    class Sic1(object):
      def __repr__(object): return 'foo'

    print('str  =', str(Sic1()))             # 'foo'
    print('repr =', repr(Sic1()), end='\n\n')# 'foo'

    class Sic2(object):
      def __str__(object): return 'foo'

    print('str  =', str(Sic2()))             # 'foo'
    print('repr =', repr(Sic2()), end='\n\n')# <__main__.Sic object at 0x2617f0>
# test2_difference_str_repr()
