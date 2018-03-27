""" 프로퍼티(게터, 세터, 델리터)
    def foo():
        doc = "The [object Object] property."

        def fget(self):
            return self._[object Object]

        def fset(self, value):
            self._[object Object] = value

        def fdel(self):
            del self._[object Object]

        return locals()
     = property(**())
 """

# def product():
#     _price = 4000
#     def fget(self):
#          return self._price
#     def fset(self, value):
#          self._price = value
#     def fdel(self):
#          del self._price
#     return locals()
#
# product = property(**product())
# print(product)          # fget


class Car(object):

    def __init__(self):
        self._price = 0
        self._speed = 0
        self._color = None

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def del_price(self):
        print("...del_price...")
        del self._price

    """
        # >>> help(property)
        # x = property(getx, setx, delx, "I'm the 'x' property.")
    """
    # 'price'는 GET, SET, DEL의 속성을 가지고 있음.
    price = property(get_price, set_price, del_price)

def main1():
    my_car = Car()

    # property 를 호춣한다.
    my_car.price = 2000             # set_x
    print("PRICE :", my_car.price)  # get_x
    del my_car.price                # del_x

# main1()
