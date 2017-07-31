TABLE='''
\nInput Value:
========================================
   X1=%.1f, X2=%.1f, Y=,%.1f
----------------------------------------
   1) rectangle  :  %10.2f cm2
   2) triangle   :  %10.2f cm2
   3) circle     :  %10.2f cm2
   4) trapezoid  :  %10.2f cm2
----------------------------------------\n'''




X1, X2, Y = 10, 10, 15      # Input Value by cm.


def calc_rect(bottom, height):
    area = bottom * height
    return area

def calc_tri(bottom, height):
    area = bottom * height * 1/2
    return area

def calc_circle(diameter):
    area = 3.141592653589793238462643383279 * float(diameter^2) * 1/4
    return area

def calc_trap(upper, lower, height):
    area = (upper + lower) * 1/2 * height
    return area

def show_total():
    print("  rectangle area = %10.2f cm2" % calc_rect(X1, Y))
    print("  triangle area = %10.2f cm2" % calc_tri(X1, Y))
    print("  cicle area = %10.2f cm2" % calc_circle(X1))
    print("  trapezoid area = %10.2f cm2" % calc_trap(X1, X2, Y))




def main():
    # print("Input:\tX1=%scm, (X2=%scm) Y=%scm" % (X1, X2, Y))
    print(TABLE % (X1, X2, Y, calc_rect(X1,Y), calc_tri(X1,Y), calc_circle(X1), calc_trap(X1,X2,Y)))

if __name__ == '__main__':
    main()
