import turtle as tu
import random
import time


tu.speed(0)
tu.color('black', 'white')

def move(pos_x, pos_y):
    tu.penup()
    tu.setpos(pos_x, pos_y)
    tu.pendown()

def card(pos_x, pos_y, size=100):
    move(pos_x-(size*0.6*0.5), pos_y-(size*0.5))
    tu.begin_fill()
    tu.forward(size*0.6)
    tu.left(90)

    tu.forward(size)
    tu.left(90)

    tu.forward(size*0.6)
    tu.left(90)

    tu.forward(size)
    tu.left(90)
    tu.end_fill()

def heart():
    def curvemove():
        for i in range(25):
            tu.right(8)
            tu.forward(8)

    tu.color('red','pink')
    tu.begin_fill()
    tu.left(140)
    tu.forward(111.65)
    curvemove()
    tu.left(120)
    curvemove()
    tu.forward(111.65)
    tu.end_fill()
heart()
tu.heading()
card(0,0,size=300)
#
# x_arr = [-160, -80, 0, 80, 160]
# y_arr = [(lambda x: x*0)(x) for x in range(5)]
#
# for x in x_arr:
#     card(x, 0, size=200)




tu.mainloop()
