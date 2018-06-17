import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
#---- ADD Parent folder ----------------------

# import subf.subsubf.equetion_area as eq
from subf.subsubf import equetion_area as eq

# import equetion_area as eq
# from equetion_area import *

x, y= 10, 10
x2= 20

rect= eq.calc_rect(x,y)
tri= eq.calc_tri(x,y)
circle= eq.calc_circle(x)
trap= eq.calc_trap(x,x2,y)

a = eq.TABLE % (x, x2, y, rect, tri, circle, trap)
print(a)
