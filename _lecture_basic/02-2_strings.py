""" ---------------------------- CHAPTER.02 LESSON.01--- multi-str, operators
 (1) multi strings = triple qoutations -> change to 1 string
 (2) string operators = +, *
"""
def lesson_01():
    a = """
      o  !
      --%
      |
     //
     !!
    """

    b ='\a\n\t  o  !\n\t  --%\n\t  |\n\t //\n\t !!\n'

    print(a)
    print(b)      # make sound. '\a'

    """ String Operater = +. * """

    c = "This is"
    _c = " my \"fathere's\" own...."

    d = (c + _c + '\n')*10
    print(d)

    e = a + d
    # print(e)
# lesson_01()

""" ---------------------------- CHAPTER.02 LESSON.02---int,str,float, byte
  (1) int, float has no len()
  (2) int(), str(), float(),
  (3) Buil-in function, a.__dir__()
"""
def lesson_02():
    a = 'Life is short, you need python'
    # a = 3.1415          # TypeError: object of type 'float' has no len()
    # a = '3.1415'

    b = len(a)

    print('This Phrase = "%s" ...' %a)
    print('Total charactors = %d ea...' %b)


    '''object

    '''

    a = 'park is not a parrot only a human...'
    # print(a.__dir__())
    # print()

    print(a.count('r'))
    print(a.find('x'))
    # print(a.index('x'))       # the same, but occure 'Error' -- if not find.

    print(','.join(a.replace(" ",""))) # 'p,a,r,k,i,s,n,o,t,a,p,a,r,r,o,t,o,n,l,y,a,h,u,m,a,n,.,.,.'
    print(a.split(' ')) #['park', 'is', 'not', 'a', 'parrot,', 'only', 'a', 'human...']
    # print(a.split('a')) #['p', 'rk is not ', ' p', 'rrot, only ', ' hum', 'n...']

    b = "    YOU!  "
    print(b, "number= %s" %len(b))              #     YOU!   number= 10
    print(b.strip(), "number= %s" %len(b.strip()))  # YOU! number= 4
    # ...
# lesson_02()

""" BYTES ENCODING : 1byte= ASCII, 2byte= UTF-8, CP949, EUC-KR
 byte funcs. : a.encode()=to byte, a.decode('CP949')=to char, bytearray(b'ab')
"""
# a = bytes(3)    # OK but N/G-b'\x00\x00\x00', (return size, Null)
""" (1) bytes() """
def bytes_test():
    print(bytes([3]))                   # b'\x03'
    print(bytes([112,52,52]))           # b'p44'
    a = bytes([112,52,52])
    print("".join(map(chr, a)))         # p44 = decode format.
    print(b'p44'.decode())              # p44 - UTF-8 (default)

    # a = bytes('한글', 'ASCII')        # ERROR = UnicodeEncodeError:
    # a = bytes('English', 'ASCII')    # b'English'

    a = bytes('한글', 'UTF-8')        # b'\xed\x95\x9c\xea\xb8\x80'
    a = bytes('漢文', 'UTF-8')        # b'\xe6\xbc\xa2\xe6\x96\x87'
    a = bytes('كورية شم', 'UTF-8')   # b'\xd9\x83\xd9\x88\xd8\xb1\xd9\x8a\xd8\xa9\xd8\xb4\xd9\x85'
    a = bytes('ΓΣ', 'UTF-8')          # b'\xce\x93\xce\x94\xce\xa3'
    a = bytes('English', 'UTF-8')     # b'English'

    # a = bytes('한글', 'CP949')        # b'\xc7\xd1\xb1\xdb' = EUC-KR = CP949
    # a = bytes('漢文', 'CP949')        # b'\xf9\xd3\xd9\xfe' = EUC-KR = CP949
    # a = bytes('English', 'CP949')     # b'English'
    #
    # a = bytes('한글', 'EUC-KR')        # b'\xc7\xd1\xb1\xdb' = EUC-KR = CP949
    # a = bytes('漢文', 'EUC-KR')        # b'\xf9\xd3\xd9\xfe' = EUC-KR = CP949
    # a = bytes('English', 'EUC-KR')     # b'English'

    print(a)
# bytes_test()

""" (2) bytearray() """
def bytearray_test():
    a = bytearray('abc','UTF-8') # '글','UT-8' 234, 284, 128
    print(a[0])         # 97
    print(a[1])         # 98
    print(a[2])         # 99
    # print(a[3])       # IndexError = bytearray index out of range

    print(chr(99))      # c

    for n in a:         # 97, 98, 99
        print(n)

    for n in 'abc':     # 97, 98, 99
        print(ord(n))
# bytearray_test()

""" (3) Encrypt & Decrypt module = bz2 : byte conversion. """
string = '파란하늘이 유난히 맑아서 \n\
 좁은새장을 풀려난 새처럼 모두.. \n\
 낡은기억은 이제는 몰아내고 싶어.. \n'

import bz2

def encrypt_decrypt():
    src = bytes(string,'UTF-8')     # use - 'byte' type
    enc_file = bz2.compress(src)
    dec_file = bz2.decompress(enc_file)

    print("Source  :\n", src.decode('UTF-8'))
    print("Encrypt :\n", enc_file, end="\n\n")
    print("Decrypt :\n", dec_file.decode('UTF-8'))   # Can't Decode w/'EUC-KR'
# encrypt_decrypt()


""" --------------------CHAPTER.02 LESSON.03-- Drill.01-MAP
  PRACTICE.01 : MAKE = 50 x 20 map with rulers on each 4 sides.
  (1) use +, *
  (2) use for-loop range(25)
  (3) use string format '%'
  (4) use .join()
"""
def horizontal_ruler(tabs):
    f = " "*2
    a = "012345"
    b = " "*4 + "." + " "*4

    c = "1234567890"
    d = " " + c*5

    ruler = (tabs + f + b.join(a) +"\n") + (tabs + f + d)
    return ruler

def middle_body(tabs):
    body = ""
    e= "."*50
    for n in range(1,25,1):
        body = body + (tabs + "%2d %s %2d" %(n, e, n) + "\n")
    body = body + (tabs + "%2d %s %2d" %(25, e, 25))
    return body

def main():
    for n in range(3):
        tabs = "\t"*n
        a = horizontal_ruler(tabs)
        b = middle_body(tabs)

        print(a)
        print(b)
        print(a)
        print("\n\n")
main()

""" --------------------CHAPTER.02 LESSON.04-- Drill.02-TEXT AMIME
  PRACTICE.02 : TEXT ANIMATION
"""

J = [[
    '.....',
    '.O...',
    '.OOO.',
    '.....',
    '.....'],[

    '.....',
    '..OO.',
    '..O..',
    '..O..',
    '.....'],[

    '.....',
    '.....',
    '.OOO.',
    '...O.',
    '.....'],[

    '.....',
    '..O..',
    '..O..',
    '.OO..',
    '.....'],]

# J = [[
#     'O........',
#     '.O.......',
#     '..O......',
#     '..O......',
#     '.O.......'],[
#
#     'O........',
#     '..O......',
#     '...O.....',
#     '..O......',
#     '.O.......'],]

# print(type(J))  # <class 'list'>
# print(len(J))   #
#
# print(J[0])
# print(J[0][0])
# print()
import time, os

def clear():
    print("\n\n\n\n\n\n"*10)

def main():
    while True:
        for n in range(len(J)):
            # clear()
            os.system('cls')
            print('\n\n'*10)
            # replace() --> . = "　", O = "■"
            for k in range(len(J[n])):
                a = J[n][k]
                a = a.replace(".","　")
                a = a.replace("O","■")
                print(a)
                # print(J[n][k].replace(".","　").replace("O","■"))
            print()
            time.sleep(0.4)
# main()

"""  Other String functions --- str_word.__dir__():
    for command_ in str_word.__dir__():
    print(command_)

    encode
    replace
    split
    rsplit
    join
    capitalize
    casefold
    title
    center
    count
    expandtabs
    find
    partition
    index
    ljust
    lower
    lstrip
    rfind
    rindex
    rjust
    rstrip
    rpartition
    splitlines
    strip
    swapcase
    translate
    upper
    startswith
    endswith
    islower
    isupper
    istitle
    isspace
    isdecimal
    isdigit
    isnumeric
    isalpha
    isalnum
    isidentifier
    isprintable
    zfill
    format
    format_map
"""


""" -------------------CHAPTER.02 LESSON.05-- Drill.03-
  PRACTICE.03 : Binary to text graph converting
"""

def is_input_string():
    """ input value test - string -> integer value """
    while True:
        try:
            x = int(input('X = '))
        except:
            x = 1
        print('.....', x)
        print('X is ..',type(x), end='\n\n')
# is_input_string()

def temporary_storage():
    """ to mask personal information """
    AA = "0123456789"
    print(AA)
    print()
    print(AA[:3])   # 012
    print(AA[4:])   # 3456789

    AA = AA[:3] + "?"*6 + AA[9:]    # 3 + 6 = 9
    print(AA)

    PERSON_INFO = "KIM BONG-EUI = 001210-1009696"

    print(PERSON_INFO[:-7])
    PERSON_INFO_MASKED = PERSON_INFO[:-7] + "*"*7
    print('ORIGINAL =', PERSON_INFO)
    print('MASKED   =', PERSON_INFO_MASKED)
# temporary_storage()

def x_():
    """ to break STRING data -> to put into DICT! """
    DATA_STRING ='''
    KIM BONG-EUI  = 001212-1011205
    PARK CHAN-HO  = 751011-1234567
    LEE SEUN-CHAN = 040512-1234455
    '''

    LINE_DATA = DATA_STRING.strip().split("\n")
    INFO_DICT = {}

    for each in LINE_DATA:
        INFO_DICT[each.split("=")[0].strip()] = each.split("=")[1].strip()

    print(LINE_DATA)
    print(INFO_DICT)
# x_()

def binary_character():
    a = [
        0b_111111,
        0b_110011,
        0b_110011,
        0b_110011,
        0b_111111,]
    # [63, 51, 51, 51, 63]

    print(a)
    print()

    for n in range(5):
        b = str(bin(a[n]))[-6:]
        b = b.replace('1','■').replace('0','　')
        print(b)
# binary_character()
