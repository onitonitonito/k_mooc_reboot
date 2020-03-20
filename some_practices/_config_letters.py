"""
# HELPER MODULE TO : some_practices/xmas_tree_2018_scroll.py
 - DEFINE LETTERS for SCROLLING SIGN
"""

print(__doc__)

digits = {
    # size of letter - 14x11 digits
        'x' : [
            "     A     ",
            "  <STAR>   ",
            "   BUGS    ",
            "     V     ",
            "    ***    ",
            "   *****   ",
            "  *******  ",
            "    ***    ",
            "   *****   ",
            " ********* ",
            "***********",
            "     H     ",
            "     H     ",
            "  ^^^^^^^  ",
            "MERRY XMAS!",
        ],
        '2' : [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "   ******* ",
            "  ***   ***",
            "        ***",
            "   ******* ",
            "  ***      ",
            "  ***     *",
            "  *********",
        ],
        '0' : [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "   ******* ",
            "  ***   ***",
            "  ***   ***",
            "  ***   ***",
            "  ***   ***",
            "  ***   ***",
            "   ******* ",
        ],
        '!' : [
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            "    ***    ",
            "    ***    ",
            "   ***     ",
            "   ***     ",
            "           ",
            "  ***      ",
            "  ***      ",
        ],
    }

digit_h = len(digits['x'])
digit_w = len(digits['x'][0])


if __name__ == '__main__':
    c = lambda key, width : [print(digits[key][i].center(width)) for i in range(digit_h)]
    c('2', 40)
    c('0', 40)
    c('2', 40)
    c('2', 40)
    c('!', 40)
    c('x', 40)

    print(f"{digit_h}")
    print(f"{digit_w}")
