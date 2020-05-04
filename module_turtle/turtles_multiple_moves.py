"""
# Test Turtle : multiple turtles movement
"""
# - Enable = blank enter
# - Enable = set number of turtles
# - Enable = echo dict drawing (record drawing)

print(__doc__)

import sys
import turtle

from _assets._add_syspath_root import root
from _assets.modules_qt import QApplication, MyApp

FILE_DIR = root + 'module_turtle\\_statics\\'
FILENAME_ECHO = FILE_DIR + 'turtle_echo.txt'

POSXY = (1300, 900)
WINDOWSIZE = (400,300)

def main():
    global MA, NUM_TURTLES, TURTLES
    MA = MyApp()
    # w = a = s = d = turtle.Turtle()
    NUM_TURTLES = int(qt_input('NUMBERS OF TURTLES? : '))
    TURTLES = [turtle.Turtle() for i in range(NUM_TURTLES)]

    mode_select = qt_input('MODE - [Enter]=DRAW / [1]=DICT INPUT : ')

    turtle.speed('fastest')

    if mode_select.startswith('1'):
        echoes = get_read_echo(filename_echo=FILENAME_ECHO)
        dict_moves = get_moves_from_echoes(echoes)
        draw_from_dict(TURTLES, dict_moves)
    else:
        draw_from_manual(TURTLES)

def qt_input(captionHead="INPUT :", winTitle="TITLE!"):
    MA.setGeometry(*POSXY, *WINDOWSIZE)
    qtInput = MA.getText(winTitle, captionHead)
    if qtInput: return qtInput
    return ""

def get_read_echo(filename_echo):
    """ """
    with open(filename_echo, mode='r', encoding='utf8') as f:
        echoes_string = f.read()
    return echoes_string

def get_moves_from_echoes(echoes):
    """ get string-moves array from string-echoes"""
    echoes_array = echoes.split('\n')
    moves_array = [echo.split(':')[1]
                    for echo in echoes_array
                    if echo.startswith('*** ENTER ANGLE')]
    dict_moves = {}
    for i, move in enumerate(moves_array, 1):
        if move != '':
            angle, move = move.split(',')
            angle, move = int(angle.strip()), int(move.strip())
            temp_move = (angle, move)
        dict_moves[i] = temp_move
    return dict_moves

def draw_from_dict(turtles, dict):
    """ # read movements from dict, draw multi-turtles"""
    start=True

    for vals in dict.values():
        moves = "{}, {}".format(vals[0], vals[1])
        print(f"*** ENTER ANGLE, FORWARD MOVE : {moves}")

        if start:
            move_turtles(turtles, moves, start=True)
            start = False
        else:
            move_turtles(turtles, moves, start=False)

    qt_input('QUIT : [Enter]')
    quit()

def draw_from_manual(turtles):
    """ # manual draw """
    start = True

    while True:
        # CASE-01: correct moves     = Move, Angle
        # CASE_02: Incorrect moves   = Enter (blank), ?
        moves = qt_input('ENTER ANGLE, FORWARD MOVE : ')
        print(f"*** ENTER ANGLE, FORWARD MOVE : {moves}")

        if moves.startswith('?'):
            quit()

        if len(moves):
            move_turtles(turtles, moves, start=start)
            temp_moves = moves
            start = False
        else:
            move_turtles(turtles, temp_moves, start=False)

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
