import time
S_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....'],
                     ]
Z_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],

                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....'],
                     ]
I_SHAPE_TEMPLATE = [
                    ['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....'],
                     ]
O_SHAPE_TEMPLATE = [
                    ['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....'],
                     ]
J_SHAPE_TEMPLATE = [
                    ['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....'],
                     ]
L_SHAPE_TEMPLATE = [
                    ['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],

                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....'],
                     ]
T_SHAPE_TEMPLATE = [
                    ['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],

                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],

                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],

                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....'],
                     ]
PIECES = {
          'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE,
          }

def clear():
    print("\n"*70)

def show_block(shape, number):
    for n in range(5):
        for m in range(5):
            b_line = PIECES[shape][number][n][m]
            if b_line == ".":
                b_line = PIECES[shape][number][n][m].replace('.','　')
            elif b_line == "O":
                b_line = PIECES[shape][number][n][m].replace('O','■')
            print(b_line, end="")
        print()

def rotate_block(shape, times=4, interval=0.5):
    turn = len(PIECES[shape])

    for n in range(times):
        clear()
        show_block(shape, n%turn)
        time.sleep(interval)

def main():
    rotate_block('S')
    rotate_block('L')
    rotate_block('T',50, 0.1)


if __name__ == '__main__':
    main()
