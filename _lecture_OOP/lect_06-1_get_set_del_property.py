""" 프로퍼티(게터, 세터, 델리터) """


class Car(object):
    doc="""
    # >>> help(property)
    # x = property(getx, setx, delx, "I'm the 'x' property.")
    """

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

    # 'price'는 GET, SET, DEL의 속성을 가지고 있음.
    price = property(get_price, set_price, del_price)




if __name__ == '__main__':
    my_car = Car()

    # property 를 호춣한다.
    print(my_car.doc)
    my_car.price = 2000                     # set_x
    print("PRICE : {:,}".format(my_car.price))          # get_x
    del my_car.price                        # del_x
