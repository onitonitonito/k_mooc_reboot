colors = ['Red','Green','Blue','Hue']

# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(colors[3])
#
# print(colors)
# print(type(colors))
#
# string="I'm soo sexy"
# print(len(string))
# print(type(string))

# #--------------------------------
import os
os.system('cls')
#
# cities = ['서울','부산','인천','대구','대전','광주','울산','수원','제주',]
#
# print(cities)
# print('LEN=',len(cities))
# print(type(cities))
# print(cities[::+2])
# print(cities[::-2])
# print(cities[::-1])

# #---------------------------------e
# color1 = ['Red','Green','Blue','White','Black']
# color2 = ['Orange','Gray','Purple','Mint']
#
# color3 = color1 + color2
# print(color3)

# color4 = color1 *2
# print(color4)

# a = 'Blue' in color1
# print(a)
# print(color2)
# print(len(color2))
#
# color2.append('Lime')
# color2.extend(['Magenta','Cyan'])
#
# print(color2)
# print(len(color2))
# #-----------------------------------------------------
SCORE='''
+----------+-------+-------+-------+-------+-------+
|  구  분  |   A   |   B   |   C   |   D   |   E   |
+----------+-------+-------+-------+-------+-------+
| 국어점수 | %5s | %5s | %5s | %5s | %5s |
+----------+-------+-------+-------+-------+-------+
| 수학점수 | %5s | %5s | %5s | %5s | %5s |
+----------+-------+-------+-------+-------+-------+
| 영어점수 | %5s | %5s | %5s | %5s | %5s |
+----------+-------+-------+-------+-------+-------+'''

KOR_SCORE = [67,87,98,100,95]
MAT_SCORE = [56,99,93,96,87]
ENG_SCORE = [66,89,99,75,66]
MIDTERM = [KOR_SCORE, MAT_SCORE, ENG_SCORE]

print(MIDTERM)

print(MIDTERM[0][0])

print(MIDTERM[0][4])
print(MIDTERM[0][-1])

print(SCORE %(
    MIDTERM[0][0], MIDTERM[0][1], MIDTERM[0][2], MIDTERM[0][3], MIDTERM[0][4],
    MIDTERM[1][0], MIDTERM[1][1], MIDTERM[1][2], MIDTERM[1][3], MIDTERM[1][4],
    MIDTERM[2][0], MIDTERM[2][1], MIDTERM[2][2], MIDTERM[2][3], MIDTERM[2][4],)
    )
