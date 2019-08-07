"""
# GitHub /niklasf/python-chess
# Documentations : https://github.com/niklasf/python-chess
#
# A pure Python chess library with move generation and validation,
# PGN parsing and writing, Polyglot opening book reading, Gaviota tablebase
# probing, Syzygy tablebase probing and UCI engine communication
"""
print(__doc__)

import chess
import os
import time

board = chess.Board()
turn = 0
move_dict = {}


def get_player():
    global turn
    _n = turn % 2
    turn += 1

    if _n == 0:
        return 'LOWER PLAYER'
    else:
        return 'UPPER PLAYER'


def get_input():
    turn_str = get_player()   # 0,1 = lower, upper
    pos_str = input('%s type move :   ' % turn_str)   # 'str'
    pos_class = chess.Move.from_uci(pos_str)
    if pos_class in board.legal_moves:
        return pos_str, pos_class
    else:
        print('*** WRONG MOVE, Try again')
        time.sleep(1)
        get_input()


def show_board():
    _a = board.board_fen() + '/'
    print(_a)
    print()

    _b = ' ' + ' '.join(_a).replace('8', ' '.join('.' * 8))
    _c_arr = _b.rstrip().split('/')
    del(_c_arr[-1])

    _head = ' ' + ' '.join('abcdefgh')
    print(_head)
    print(' ' + '__' * 8)

    for i, _c in enumerate(_c_arr):
        print('%s| ... %s' % (_c, 8 - i))
        if i == 7:
            print('\n')


def show_available():
    global move_dict
    for i, _a in enumerate(board.legal_moves):
        print(i, str(_a), end=" / ")
        move_dict[str(i)] = str(_a)
    print('\n\n')


while True:
    show_board()
    print(board)
    print()

    show_available()
    pos_str, pos_class = get_input()
    os.system('cls')
    board.push_san(pos_str)


"""
HTTP API =
     1. https://backscattering.de/web-boardimage/board.svg?
     2. fen=5r1k/1b4pp/3pB1N1/p2Pq2Q/PpP5/6PK/8/8
     3. lastMove=f4g6
     4. check=h8
"""
