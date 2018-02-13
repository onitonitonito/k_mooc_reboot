class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print("... {} Destroyed! ....".format(class_name))

pt1 = Point()
pt2 = Point()
# pt2 = pt1
pt3 = pt1

print("pt1= {} \npt2= {} \npt3= {}\n\n".format(
    id(pt1),
    id(pt2),
    id(pt3)))

print("pt1= {} \npt2= {} \npt3= {}\n\n".format(
    pt1,
    pt2,
    pt3))

del(pt1)
del(pt2)
del(pt3)
