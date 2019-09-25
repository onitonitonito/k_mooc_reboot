class Area(object):                         # ... [ PARENT ]
    def __init__(self, arg_xi, arg_yi):
        self.xi = arg_xi
        self.yi = arg_yi

    def __str__(self):
        self.intro = "calc area of [rect], [tri], [circle] with arg_xi,arg_yi"
        return self.intro

    def calc_rect_area(self):
        return self.xi*self.yi

    def calc_Tri_area(self):
        return (0.5 * (self.xi * self.yi))

    def calc_circle_area(self):
        return (0.25*(3.141519 * self.xi**2))


class Rectangular(Area):                    # ... [ CHILD ]
#    def __init__(self, arg_xi, arg_yi):    ... INHERIT from PARENT
#        self.xi = arg_xi
#        self.yi = arg_yi

    def __str__(self):                    # ... REPEAT = OVERRIDE!
        self.intro = "I'm an Rectangular!\narea of RECT:  %dm x %dm = %dm2 \n\n"%(
        self.xi, self.yi, (self.xi*self.yi), )
        return self.intro

#    def area(self):                      # .... REPEAT = USE PARENT : calc_rect_area
#        return (self.xi * self.yi)

    def height(self):
        return self.yi

    def width(self):
        return self.xi
