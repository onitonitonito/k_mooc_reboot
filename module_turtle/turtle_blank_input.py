"""
# draw poligin with turtle
"""
print(__doc__)

import turtle

t = turtle.Turtle()

def main():
    while 1:

        moves = input('move, angle :')

        if len(moves):
            move, angle = get_move_angle(moves)
        else:
            move, angle = temp_moves

        temp_moves = (move, angle)

        t.right(angle) if angle > 0 else t.left(abs(angle))
        t.forward(move)


    # app01_test()
    turtle.mainloop()

def get_move_angle(moves, echo=True):
        _m, _a = moves.split(',')
        move, angle = _m.strip(), _a.strip()
        if echo:
            print(f"move, angle = {move}, {angle}")
        return int(move), int(angle)

def app01_test():
    """simple test the way it works"""
    t.speed('fastest')
    t.penup()
    t.setpos(0, 0)

    t.pendown()
    t.forward(100)


if __name__ == '__main__':
    # print(get_move_angle('100,'))   # FOR TEST!
    main()
