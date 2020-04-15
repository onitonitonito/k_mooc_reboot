""" scale is the size parameter, the shown tree is for scale=50.
# Takes a minute or two to draw. (this is fastest mode of TURTLE)
# refer to 'codegolf.stackexchange.com' Here: https://bit.ly/2W7KxRq
"""
import turtle as tu

# scale = int(input('scale= : '))*1.0   ... SIZE(SCALE) of TREE

scale = 50

tu.speed("fastest")

def main():
    pass

def ask_go(quit=False):
    if quit:
        input('\n'*5 + '*** QUIT to EXIT? : [Enter]=FINISH' + '\n'*20)
    else:
        input('*** CONTINUE ? : [Enter]=GO')

def draw_star():
    tu.setheading(90)
    tu.color("orange", "yellow")

    tu.forward(3*scale)
    tu.begin_fill()
    tu.left(126)

    for i in range(5):
        tu.forward(scale/5)
        tu.right(144)
        tu.forward(scale/5)
        tu.left(72)

    tu.end_fill()
    tu.right(126)

def tree(d, scale):
    """ # TODO: RECURSIVE PRACTAL """

    if d <= 0:
        return

    tu.forward(scale)

    tree(d-1, scale*0.8)
    tu.right(120)

    tree(d-3, scale*0.5)
    tu.right(120)

    tree(d-3, scale*0.5)
    tu.right(120)

    tu.backward(scale)

    print(f"*** TREE! - {d:02} - ***\n")
    ask_go()

draw_star()
ask_go()

tu.color("dark green")
tu.backward(scale*4.8)
ask_go()


tree(10, scale)

tu.backward(scale/2)
ask_go(quit=True)

# tu.mainloop()


if __name__ == '__main__':
    main()
