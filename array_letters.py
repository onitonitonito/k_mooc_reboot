"""
#
"""

print(__doc__)

(digit_h, digit_w) = (14, 11)
digits = {
    # size of letter - 14x11 digits
        'x' : [
            "     A     ",
            "    < >    ",
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
            "    ***    ",
            "    ***    ",
            "   ***     ",
            "   ***     ",
            "           ",
            "  ***      ",
            "  ***      ",
        ],
    }



if __name__ == '__main__':
    c = lambda key, width : [print(digits[key][i].center(width)) for i in range(digit_h)]
    c('2', 40)
    c('0', 40)
    c('2', 40)
    c('2', 40)
    c('!', 40)