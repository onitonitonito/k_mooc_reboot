"""
# turtle draws a heart & cards
"""
print(__doc__)


import turtle as tu

ASK = 0

tu.speed('fastest')

def main():
    draw_heart()
    ask_go()

    # tu.home()

    x_arr = [-160, -80, 0, 80, 160]
    y_arr = [(lambda x: -100 + x * -2)(x) for x in range(5)]

    for i, x in enumerate(x_arr):
        card_size=200
        move(x - (card_size * 0.6 * 0.5), y_arr[i] - (card_size * 0.5))
        draw_card(x, y_arr[i], size=card_size)
        ask_go()


    # tu.mainloop()
    ask_go(finish=True)
    pass

def ask_go(finish=False):
    if finish:
        input('*** FINISH? : [ENTER]')
    else:
        if ASK:
            if input('*** CONTINUE? : [ENTER]').startswith('?'):
                quit()

def move(x, y):
    tu.penup()
    tu.setpos(x, y)
    tu.pendown()

def draw_card(x, y, size=100):
    tu.color('black', 'yellow')
    tu.begin_fill()

    for i in range(2):
        tu.forward(size * 0.6)
        tu.left(90)

        tu.forward(size)
        tu.left(90)

    tu.end_fill()

def draw_heart():
    def curvemove():
        for i in range(25):
            tu.right(8)
            tu.forward(8)

    tu.color('red', 'pink')
    tu.begin_fill()

    # tu.left(140)
    tu.setheading(140)
    tu.forward(128)

    curvemove()
    tu.left(122)

    curvemove()
    tu.forward(111.65)

    tu.end_fill()



if __name__ == '__main__':
    main()
