def test1_list_data():
    colors = ['Red','Green','Blue','Hue']

    print(colors[0])    # Red 'str'
    print(colors[1])    # Green 'str'
    print(colors[2])    # Blue 'str'
    print(colors[3])    # Hue 'str'

    print(colors)       # ['Red','Green','Blue','Hue']
    print(type(colors)) # <class 'list'>

    string="I'm soo sexy"
    print(len(string))
    print(type(string))
# test1_list_data()

def test1_list_slicing():
    import os
    os.system('cls')

    cities = ['Seoul','Busan','Incheon','Degu','Dejeon','Gwangju','ulsan']

    print(cities)               # ['Seoul','Busan','Incheon',...,'ulsan']
    print('LEN=', len(cities))
    print(type(cities))
    print(cities[::+2])
    print(cities[::-2])
    print(cities[::-1])
# test1_list_slicing()

def test3_list_operand_func():
    color1 = ['Red','Green','Blue','White','Black']
    color2 = ['Orange','Gray','Purple','Mint']

    color3 = color1 + color2
    print(color3)

    color4 = color1 *2
    print(color4)

    a = 'Blue' in color1
    print(a)
    print(color2)
    print(len(color2))

    color2.append('Lime')
    color2.extend(['Magenta','Cyan'])

    print(color2)
    print(len(color2))
# test3_list_operand_func()


""" To make 'TEXT' table format, refer to below URL...
http://www.tablesgenerator.com/text_tables """

SCORE_CARD = '''
 +----------+-------+-------+-------+-------+-------+
 |  구  분  |   A   |   B   |   C   |   D   |   E   |
 +----------+-------+-------+-------+-------+-------+
 | 국어점수 | %5s | %5s | %5s | %5s | %5s |
 +----------+-------+-------+-------+-------+-------+
 | 수학점수 | %5s | %5s | %5s | %5s | %5s |
 +----------+-------+-------+-------+-------+-------+
 | 영어점수 | %5s | %5s | %5s | %5s | %5s |
 +----------+-------+-------+-------+-------+-------+'''

KOR_SCORE = [67, 87, 98, 100, 95]
MAT_SCORE = [56, 99, 93, 96, 87]
ENG_SCORE = [66, 89, 99, 75, 66]
MIDTERM = [KOR_SCORE, MAT_SCORE, ENG_SCORE]

def test4_how_to_zip():
    # a = list(zip(KOR_SCORE,MAT_SCORE,ENG_SCORE))
    print(MIDTERM)     # [[A...], [B...], [C...]]
    a_ = zip(*MIDTERM)  # zipping each 3 pieces out of 3 groups as TUPLE.
    print(a_)          # <zip object at 0x0207A418>
    print(tuple(a_))   # zip obj. --> tuple or list
# test4_how_to_zip()

def show_score_card1():
    print(SCORE_CARD %(
        MIDTERM[0][0], MIDTERM[0][1], MIDTERM[0][2], MIDTERM[0][3], MIDTERM[0][4],
        MIDTERM[1][0], MIDTERM[1][1], MIDTERM[1][2], MIDTERM[1][3], MIDTERM[1][4],
        MIDTERM[2][0], MIDTERM[2][1], MIDTERM[2][2], MIDTERM[2][3], MIDTERM[2][4],)
         )
show_score_card1()

def show_score_card2():
    score_arr = []
    for x in range(3):
        for y in range(5):
            score_arr.append(MIDTERM[x][y])

    print(SCORE_CARD% tuple(score_arr))   # format uses 'TUPLE' args, _NOT_'list'_
show_score_card2()

def show_score_card3():
    """ print-format uses 'TUPLE' args, _NOT_'list'_ like below """
    print(SCORE_CARD % (67, 87, 98, 100, 95, 56, 99, 93, 96, 87, 66, 89, 99, 75, 66,))
show_score_card3()
