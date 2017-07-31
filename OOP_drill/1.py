# result = 0
# n = 1
#
# for x in range(9):
#     result = 2 * n
#     print(result)
#     # print(" 2 x %s = %s" % (n,result))
#     n += 1
# ---------------------------------------------

result = 0
n = 1
m = 2

for x in range(8):
    for y in range(9):
        result = m * n
        print(result)
        n +=1
    m +=1
    n = 1
