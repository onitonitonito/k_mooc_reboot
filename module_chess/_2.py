import chess
import os

b = chess.Board()
move_arr =[]
print(b)

while True:
    _a = input('\nMove?  :  ')
    move_arr.append(_a)

    b.push_san(_a)

    os.system('cls')
    print(b)
    print('\n', _a, move_arr)
    print('\n', b.legal_moves)
