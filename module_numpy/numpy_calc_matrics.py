import numpy as np

def get_result_matrics(x, y, z):
    print('x =\n', x)
    print('y =\n', y)
    print()
    print('z =\n', z)
    print()

x = np.array([
    [1, 2, 1],
    [0, 1, 0],
    [2, 3, 4],
    ])

y = np.array([
    [2, 5],
    [6, 7],
    [1, 8]])

z = np.dot(x, y)

get_result_matrics(x, y, z)
""" Show matrics multify  """

x = np.c_[x, [1, 2, 3]]      # [[1],[2],[3]] <--single brackets mean nothing
y = np.r_[y, [[4, 5]]]      # [[4,5]] <-- to Add a row uses double brackets
z = np.dot(x, y)

get_result_matrics(x, y, z)

"""
a = [[1,2,1],
    [0,1,0],
    [2,3,4]]

b = [[2,5],
    [6,7],
    [1,8]]
print(a)
print(b)

d = a . b
print(d)
d = [[15,27],
    [6,7],
    [26,63]]
-------------------- FAIL"""
