import chess
import chess.svg

# board = chess.Board()

def test01():
    _a_str = 'd2d4'
    move = chess.Move.from_uci(_a_str)

    if move in board.legal_moves:
        print('%s = %s'% (type(move), move))
    else:
        print('NG..')

""" HTTP API =
  1. https://backscattering.de/web-boardimage/board.svg?
  2. fen=5r1k/1b4pp/3pB1N1/p2Pq2Q/PpP5/6PK/8/8
  3. lastMove=f4g6
  4. check=h8
"""

board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
squares = board.attacks(chess.E4)
_a = chess.svg.board(board, squares)
# print(_a)
