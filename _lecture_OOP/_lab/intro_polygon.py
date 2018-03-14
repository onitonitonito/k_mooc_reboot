# Class TEST -- We're Polygons
# All Classes are inherited from RePolygon()
# code : UTF-8

class RePolygon:

    def __init__(self):
        self.setSide()

    def setSide(self,side=0):
        self.side = side
        self.inAngle = None
        self.exAngle = None

    def show(self):
        print("  (1) Length of Lines = ",self.side)
        print("  (2) Inner Angles = ",str(self.inAngle)+" Degree")
        print("  (3) External Angles = ",str(self.exAngle)+" Degree\n")


class Triangle(RePolygon):

    def setSide(self,side=0):
        self.side = side
        self.inAngle = 180-360/3
        self.exAngle = 180 - self.inAngle

    def show(self):         # Show() is overrided on PARENT's (So,it Shows Own)
        print("** THIS IS A TRIANGLE ~!!! **")
        super().show()      # Show() is Overrided, but Super().Show() Shows PARENT'S


class Quadrilateral(RePolygon):

    def setSide(self,side=0):
        self.side = side
        self.inAngle = 180-360/4
        self.exAngle = 180 - self.inAngle

    def show(self):
        print("** THIS IS A RECTANGLE ~!!! **")
        super().show()


class Pentagon(RePolygon):

    def setSide(self,side=0):
        RePolygon.setSide(self,side)
        self.inAngle = 180-360/5
        self.exAngle = 180 - self.inAngle

    def show(self):
        print("** THIS IS A PENTAGON ~!!! **")
        super().show()


class Hexagon(RePolygon):

    def setSide(self,side=0):
        super().setSide(side)
        self.inAngle = 180-360/6
        self.exAngle = 180 - self.inAngle

    def show(self):
        print("** THIS IS A HEXAGON ~!!! **")
        super().show()

a = Triangle()              # Declair Class of Objects (a) is TRIANGLE
b = Quadrilateral()         # Declair (b) is Class of QUADRILATERAL
c = Pentagon()              # Declair (c) is Class of PENTAGON
d = Hexagon()               # Declair (d) for HEXAGON

a.setSide(3)        # setSide() is Override on PARENT'S (RePolygon)

a.show()            # Show() is overrided on PARENT's (So, it Shows Own)
b.show()            # Show() is Overrided, but Super().Show() Shows PARENT'S
c.show()
d.show()
