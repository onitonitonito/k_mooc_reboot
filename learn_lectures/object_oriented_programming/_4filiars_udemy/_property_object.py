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
    print("%-10s %s" % (key, value))

price = property(**price())
print(price, "\n\n")
