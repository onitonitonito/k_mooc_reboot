"""
# GitHub /niklasf/python-chess
# Documentations : https://github.com/niklasf/python-chess
# https://python-chess.readthedocs.io/en/latest/
#
# A pure Python chess library with move generation and validation,
# PGN parsing and writing, Polyglot opening book reading, Gaviota tablebase
# probing, Syzygy tablebase probing and UCI engine communication
"""
print(__doc__)

import chess


STARTING_FEN = 'r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4'

board = chess.Board(fen=STARTING_FEN, chess960=False)
print(board)
