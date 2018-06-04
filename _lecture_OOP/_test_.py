def price():
    doc = "The [price object] property."
    def fget(self):
        return self._object
    def fset(self, value):
        self._object = value
    def fdel(self):
        del self._object
    return locals()

for key, value in price().items():
    print("%-10s %s"%(key,value))

price = property(**price())

class One(object):
    def __init__(self, x=10, y=20):
        self.first_var = x
        self.second_var = y

    def add(self):
        return self.first_var + self.second_var

    def multi(self):
        return self.first_var * self.second_var

    @staticmethod
    def show_operands(obj):
        print("%s + %s = %s"% (obj.first_var,obj.second_var,obj.add()))
        print("%s x %s = %s"% (obj.first_var,obj.second_var,obj.multi()))

    def local(self):
        return locals()

t = One()
# t.show_operands(t)

a = One(1024, 64)
# a.show_operands(a)


for key, value in One.__dict__.items():
    print("%-17s %s"%(key, value))
print()

# ----------------------------------------------------------------
for key, value in globals().items():
    print("%-17s %s"%(key, value))
print()

for key, value in locals().items():
    print("%-17s %s"%(key, value))
print()

print("Globas = locals? :", globals() == locals())         # True
