"""
# QinputDialog
"""
# https://pythonspot.com/pyqt5-input-dialog/

import sys
from assets.modules_qt import QApplication, MyApp

NUM_TURTLES = 1

def main():
    import turtle

    t = turtle.Turtle()
    t.speed('fastest')
    t.home()

    ma = MyApp()
    posxy = (0,0)
    windowsize = (300,200)
    ma.setGeometry(*posxy, *windowsize)

    while True:
        moves = ma.getText("Turtle Moves", "Enter angle, move forward :")
        print(f"*** ENTER ANGLE, FORWARD MOVE : {moves}")

        if moves:
            move_turtles([t,], moves, start=False)
            temp_moves = moves
        else:
            move_turtles([t,], temp_moves, start=False)

def move_turtles(turtles, moves, start=True):
    """ to move muti-turtles along w/ (angle,move)
    # move_turtles(turtles, moves, start=True):
    #  - turtles = list of turtle objects
    #  - moves   = input str 'angle,move' will be --> int (angle, move)
    #  - start   = if True, when First movements set
    #              radiation directions of each turtles by 360/n
    """
    angle, move = get_angle_move_from(moves)
    heads = [n for n in range(0, 361, int(360/NUM_TURTLES))]

    for i, tur in enumerate(turtles):
        if start:
            tur.setheading(heads[i])

        tur.left(angle) if angle > 0 else tur.right(abs(angle))
        tur.forward(move)

def get_angle_move_from(moves):
    """ to make str-moves into int(angle, move)
    # get_angle_move_from(moves):
    #  - return int (angle, move)
    """
    angle, move = moves.split(",")
    angle, move = angle.strip(), move.strip()
    return int(angle), int(move)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())
