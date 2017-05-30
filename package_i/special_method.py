class Complex(object):
    def __init__(self,arg_real, arg_imagin):
        self.r = arg_real
        self.i = arg_imagin


class Complex2(Complex):

    def __repr__(self):
        return "Complex number: real=%0.2f, imagin=%0.2f" %(self.r, self.i)

    def __str__(self):
        return "[str] "+self.__repr__()


class Complex3(Complex2):
    def __getitem__(self, key):     # c3[] = available
        if key == 'r':
            return self.r

        if key == 'i':
            return self.i


#c = Complex(1,2)
#print(c)            # <__main__.Complex object at 0x021CC5F0>

#c2 = Complex2(3,4)
#print(c2)           # [str] Complex number: real=3.00, imagin=4.00
#print(str(c2))      # [str] Complex number: real=3.00, imagin=4.00

c3 = Complex3(5,6)
print(c3)           # [str] Complex number: real=5.00, imagin=6.00
print(c3['r'])      # 5
print(c3['i'])      # 6

print()
print(c3.r)         # 5
print(c3.i)         # 6
