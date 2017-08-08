import sys, os
from os.path import dirname, abspath, realpath
sys.path.append(dirname(dirname(__file__)))
# inc'l x1 upper from file exist

# print(dirname(dirname(__file__)))
# print(os.path.abspath(__file__))
# print(os.path.pardir)
# print(os.path.realpath(os.path.pardir))

from package_i.calc_area import Area

#python run_calc_area.py 10 20 -- sys.argv
# 10 characters are given for Format %s

TABLE='''
+===============================================+
|  SPECIFIACTION OF DIMENSION                   |
+-----------------------------------------------+
|  BOTTOM = %7s (m), (or Dia of Circle)     |
|  HEIGHT = %7s (m)                         |
+--------+------------+------------+------------+
|  SHAPE | B or D (m) |    H (m)   |  AREA (m2) |
+--------+------------+------------+------------+
|  RECT  | %10s | %10s | %10.3f |
+--------+------------+------------+------------+
|   TRI  | %10s | %10s | %10.3f |
+--------+------------+------------+------------+
| CIRCLE | %10s | %10s | %10.3f |
+--------+------------+------------+------------+
'''

if len(sys.argv) < 3:
    try:
        if sys.argv[1] == None:     # out of Index Error!
            pass
    except:             # Default value
        BOTTOM = 10.5   # 10.5 float
        HEIGHT = 15.5   # 15.5 float

    # print ('*** MISSING ARGS : NEED 2, B(d)=, H= ***')
    # sys.exit()

else:
    BOTTOM = float(sys.argv[1])    # 10
    HEIGHT = float(sys.argv[2])    # 20

print('B(or d)=%s m, H=%s m'  %(BOTTOM, HEIGHT))

me = Area(BOTTOM, HEIGHT)        # me is OBJECT!

RECT =  [BOTTOM, HEIGHT, me.calc_rect_area()]
TRI  =  [BOTTOM, HEIGHT, me.calc_Tri_area()]
CIRCLE =[BOTTOM, '-',    me.calc_circle_area()]

print(TABLE %( BOTTOM, HEIGHT,
    RECT[0], RECT[1], RECT[2],
    TRI[0], TRI[1],TRI[2],
    CIRCLE[0], CIRCLE[1], CIRCLE[2],)
    )


# MAKE TABLE : http://www.tablesgenerator.com/text_tables
''' And the Result is....
+===============================================+
|  SPECIFIACTION OF DIMENSION                   |
+-----------------------------------------------+
|  BOTTOM =   122.5 (m), (or Dia of Circle)     |
|  HEIGHT =    11.3 (m)                         |
+--------+------------+------------+------------+
|  SHAPE | B or D (m) |    H (m)   |  AREA (m2) |
+--------+------------+------------+------------+
|  RECT  |      122.5 |       11.3 |   1384.250 |
+--------+------------+------------+------------+
|   TRI  |      122.5 |       11.3 |    692.125 |
+--------+------------+------------+------------+
| CIRCLE |      122.5 |          - |  11785.605 |
+--------+------------+------------+------------+
[Finished in 0.481s]'''
