# Bulit-in Special Method __something__
#

class Complex(object):                  # Run first, initialize class.
    def __init__(self,arg_real, arg_imagin):
        self.r = arg_real
        self.i = arg_imagin
#c = Complex(1,2)
#print(c)            # <__main__.Complex object at 0x021CC5F0> Memory Address

class Complex2(Complex): # explanation string
    def __str__(self):
        return "[str] " + self.__repr__()

    def __repr__(self): # more descrete string
        return "Complex number: real=%0.2f, imagin=%0.2f" %(self.r, self.i)
#c2 = Complex2(3,4)
#print(c2)           # [str] Complex number: real=3.00, imagin=4.00
#print(__str__(c2))      # [str] Complex number: real=3.00, imagin=4.00

class Complex3(Complex2):
    def __getitem__(self, key):     # c3[] = available
        if key == 'r':
            return self.r

        if key == 'i':
            return self.i

    def __delitem__(self, key):
        if key == 'r':
            self.r = 0
            #print("DELETE r...")


        if key == 'i':
            self.i = 0
            #print("DELETE i...")

c3 = Complex3(5,6)
#print(c3)           # [str] Complex number: real=5.00, imagin=6.00
#print(c3['r'])      # 5
#print(c3['i'])      # 6

#print()
#print(c3.r)         # 5
#print(c3.i)         # 6

print(str(c3))
print(repr(c3))
print(c3['r'])
print(c3['i'])

del(c3['r'])
print(str(c3))

del(c3['i'])
print(str(c3))
