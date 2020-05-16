"""
# some circles and poligons
"""
import turtle

ts = [turtle.Turtle() for i in range(4)]
posXYs = [
    (0,     0),
    (-200,  0),
    (200,   0),
    (0,     200),
]

def main():
    move_pen(ts[0], *posXYs[0])
    show_rect(turtle_obj=ts[0], width=100, hight=50)

    radius = 50

    # move_pen(ts[1], *posXYs[1])
    move_pen(ts[1], posXYs[1][0]+radius, posXYs[1][1])
    ts[1].setheading(90)
    ts[1].circle(radius)

    move_pen(ts[2], *posXYs[2])
    ts[2].setheading(220)
    ts[2].circle(radius, extent=300, steps=30)

    # move_pen(ts[3], *posXYs[3])
    move_pen(ts[3], posXYs[3][0]+radius, posXYs[3][1])
    ts[3].setheading(90)
    ts[3].circle(radius, steps=6)

    input_enter_to_quit()

    turtle.mainloop()

def input_enter_to_quit():
    if input('*** ENTER TO QUIT! ***').startswith(''):
        quit()
    return True

def move_pen(turtle_obj, posX, posY):
    turtle_obj.penup()
    turtle_obj.goto(posX, posY)
    turtle_obj.pendown()

def go_angle(turtle_obj, forward, angle):
    turtle_obj.forward(forward)
    turtle_obj.right(angle)

def show_rect(turtle_obj, width, hight):
    move_pen(turtle_obj, -width/2, 0)
    for i in range(2):
        go_angle(turtle_obj, width, 90)
        go_angle(turtle_obj, hight, 90)


if __name__ == '__main__':
    main()
