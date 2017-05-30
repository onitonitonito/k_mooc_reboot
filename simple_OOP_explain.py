from package_i.calc_area import Rectangular
from package_i.calc_area import Area

#import package_i.calc_area as calc

# 04 PART = O.O.P (Objective Oriented Programming)

me = Rectangular(10,20) # declair OBJECT            ..... [ CHILD ]
#me = calc.Rectangular(10,20) # declair OBJECT

print(me)               # return REPRESENTATIVE __str___

print(me.calc_rect_area())# Function area()
print()
print(me.width())       # Function width()
print(me.height())      # Function height()

print()
print(me.xi)             # Variable xi
print(me.yi)             # Variable yi

you = Area(15, 11)  # declaor OBJECT                .... [ PARENT ]
print()
print("YOU object:\n",you)
print()
print("xi=%dm, yi=%dm, rect_area=%dm2" %(you.xi, you.yi, you.calc_rect_area()))
print("xi=%dm, yi=%dm, tri_area=%dm2" %(you.xi, you.yi, you.calc_Tri_area()))
print("di=%dm, circle_area=%dm2" %(you.xi, you.calc_circle_area()))
print("\n")

'''
    # 01.PART = Variable (Definition)
    h = 10
    v = 20

    # 02.PART = Function (Relation)
    def area_rect(h, v):
        return h * v

    # 03.PART = CALCULATE : (Definition x Relation)
    a = area_rect(h, v)
    print("area of RECT:  %dm x %dm = %dm2" %(h,v,a) )
    '''
