"""
# draw poligin with turtle
"""
print(__doc__)

import turtle
from typing import Dict, List, Tuple

t = turtle.Turtle()

def main():
    while 1:
        moves = input('angle, move :')

        if len(moves):
            angle, move = get_angle_move(moves)
        else:
            angle, move = temp_moves

        temp_moves = (angle, move)

        t.right(angle) if angle > 0 else t.left(abs(angle))
        t.forward(move)


    # app01_test()
    turtle.mainloop()

def get_angle_move(moves: str, echo:bool=True) -> Tuple:
        angle, move = moves.split(',')
        angle, move = angle.strip(), move.strip()
        if echo:
            print(f"*** angle, move : {angle}, {move}")
        return int(angle), int(move)

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
