from sys import path as sys_path
from os.path import dirname

# inc'l x1 upper from file exist.
sys_path.append(dirname(dirname(__file__)))


from package_i.game_charactors import Warrior, Magician, Begger
from time import sleep
import os

def status():
    print()
    print("NAME:%s / LIFE:%s"%(a.attribution['NAME'], a.attribution['LIFE']))
    print("NAME:%s / LIFE:%s"%(b.attribution['NAME'], b.attribution['LIFE']))
    print("NAME:%s / LIFE:%s"%(c.attribution['NAME'], c.attribution['LIFE']))


a = Warrior('ALEXANDER')
b = Magician('HILLARY')
c = Begger('TRUMPH')
sleep(3)


a.attacked(b.attribution['HIT'],verbose=1)
sleep(0.5)

b.attacked(a.attribution['HIT'])
sleep(0.2)
print()

status()
sleep(3)
print()

b.assult(a)
sleep(0.5)
print()

c.assult(b)
sleep(0.5)
print()

c.assult(b)
sleep(0.5)
print()

c.assult(b)
sleep(0.5)
print()

c.assult(b)
sleep(0.5)
print()

status()
sleep(1)
print()

# os.system('cls')
b.assult(c)
