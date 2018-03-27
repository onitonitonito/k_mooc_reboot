
def price():
    # doc = "The [object Object] property."
    _obj_object = 4000
    def fget(self):
        return self._obj_object
    def fset(self, value):
        self._obj_object = value
    def fdel(self):
        del self._obj_object
    return locals()
price = property(**price())
