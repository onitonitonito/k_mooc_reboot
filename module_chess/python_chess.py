"""
* Python Chess - better work in Jupyter notebook
* refer to : https://github.com/niklasf/python-chess
* for SVG to : https://svgontheweb.com/ko/
"""
# pip install python-chess

import time
import chess
import chess.svg

PIECE_DIC = {
    "k": "king",
    "q": "queen",
    "b": "bishop",
    "n": "knight",
    "r": "ruke",
    "P": "pawn",
    }
BOARD = chess.Board()
SQUARES = BOARD.attacks(chess.E4)


def write_svg(piece, middle_name):
    """
    * str = chess.svg.piece(chess.Piece.from_symbol("R"))   # SVG str = Ruke
    * write_svg("R", "ruke")
    * piece = "R", middle_name = "ruke"
    * result :  write to svg_filename = 'p_ruke.svg'
    """
    svg_tag = chess.svg.piece(chess.Piece.from_symbol(piece))
    file_name = "p_{}.svg".format(middle_name)

    with open(file_name, "w") as f:
        f.write(svg_tag)

    print("... '%s' is made ..." % file_name)


def make_svg_bl_wh(piece_dict):
    prefix = "bl_"
    for key in piece_dict:
        write_svg(key, prefix + piece_dict[key])

    time.sleep(1)

    prefix = "wh_"
    for key in piece_dict:
        write_svg(key.upper(), prefix + piece_dict[key])


def make_svg_board():
    svg_str = chess.svg.board(BOARD, SQUARES)
    file_name = "p_00_board.svg"
    with open(file_name, "w") as f:
        f.write(svg_str)

    print("... '%s' is made ..." % file_name)


if __name__ == '__main__':
    # make_svg_bl_wh(PIECE_DIC)
    # make_svg_board()

    write_svg("p", "pawn")

    print(SQUARES, "\n\n")
    print(BOARD)
