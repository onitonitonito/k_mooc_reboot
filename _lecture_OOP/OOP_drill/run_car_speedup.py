from sys import path as sys_path
from os.path import dirname

# inc'l x1 upper from file exist.
sys_path.append(dirname(dirname(__file__)))


from package_i.model_car import *

a = Car('ACCENT')
b = Car('ODYSSAY')

a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()
a.speed_up()


b.speed_up()
b.speed_up()
b.speed_up()

print()
b.speed_down()
b.speed_down()
b.speed_down()
b.speed_down()

c = SportCar('Porsche')
d = Truck('Scannia')
e = Cart('SuperMarket')
