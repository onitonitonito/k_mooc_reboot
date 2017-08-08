""" ---------------------------------- CHAPTER.01 LESSON.01---Numbers
 (1) INTEGER
 (2) FLOAT
 (3) Octa-decimal, Binary, Hexa-decimal
"""
def lesson_01():
    a = 5.2                             # float
    b = 2                               # int
    c = a / b                           # float c=2.6

    print("FLOAT answer=" ,c)           # c=2.6
    print("INTEGER answer=" ,int(c))    # c=2

    d = int(c)
    print(d)           # d = int(2.6) = 2

    e = float(d)       # e = float(2) = 2.0
    print(e)

    print(0b_1110)     # 8+4+2+0 = 14
    print(0b_0111)     # 4+2+1 = 7
    print(0b_111)      # 0+4+2+1 = 7
    print(0b_111)      # 0+4+2+1 = 7
# lesson_01()

""" ---------------------------------- CHAPTER.01 LESSON.02---OPERATORS
+ - / * = four essencial operaters
%, **, //
"""
# iterator (LOOP)
print(7%7)              # 0
print(7%6)              # 1
print(7%5)              # 2
print(7%4)              # 3
print(7%3)              # 1
print(7%2)              # 1
print(7%1, end='\n\n')  # 0

""" '%' drill : """
for n in range(7, 0, -1):
    print('7 %% %s ='%n, 7%n)
print()

""" '//' drill """
for n in range(10, 0, -1):
    print('10/{} = '.format(n), 10//n)
    # print('10/%s = '%n, 10//n)
print()

""" '**' drill """
for n in range(1, 8, 1):
    print('%s ** 2 = '%n, n**2)
print()
