from package_i.game_charactors import Warrior, Magician, Begger
from time import sleep
import os

def status():
    print()
    print("NAME:%s / LIFE:%s"%(a.super['NAME'], a.super['LIFE']))
    print("NAME:%s / LIFE:%s"%(b.super['NAME'], b.super['LIFE']))
    print("NAME:%s / LIFE:%s"%(c.super['NAME'], c.super['LIFE']))


a = Warrior('ALEXANDER')
b = Magician('HILLARY')
c = Begger('TRUMPH')
sleep(3)


a.attacked(b.super['HIT'],verbose=1)
sleep(0.5)

b.attacked(a.super['HIT'])
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

os.system('cls')
b.assult(c)
