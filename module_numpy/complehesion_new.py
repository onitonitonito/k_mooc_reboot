""" 컴프리핸션 리스트로 매트릭스 만들기 -- 디스 이즈 파이써닉!
# making pair-wise squired difference matrics in 2 ways
#   - using double for-looping function in several lines
#   - using comprehension list in simple way
# let's check that out. -- making matrics
# \n\n"""
print(__doc__)

import numpy as np
import pandas as pd
from pprint import pprint


def calc_pairwise_squared_difference(_z):
    """_z is list data"""
    num_data = len(_z)
    matrix = []

    for i in range(num_data):
        line = []
        for j in range(num_data):
            var = (_z[i] - _z[j]) ** 2
            line.append(var)
        matrix.append(line)
    return np.array(matrix)




_ints = [0, 1, 2, 3, 4, 5]

_a = calc_pairwise_squared_difference(_ints)
pprint(_a)

_b = np.array([[(_ints[i] - _ints[j])**2 for i in _ints] for j in _ints])
pprint(_b)

# _c = list(map(lambda x: (x[i] - x[j])**2, _ints))
# _c = lambda x: [[int(i==j) for i in range(x)] for j in range(x)]
_c = lambda x: [[int(i==j) for i in range(x)] for j in range(x)]
pprint(list(map(_c, _ints)))




"""
# making pair-wise squired difference matrics in 2 ways
#   - using double for-looping function in several lines
#   - using comprehension list in simple way
# let's check that out.
#

array([[ 0,  1,  4,  9, 16, 25],
       [ 1,  0,  1,  4,  9, 16],
       [ 4,  1,  0,  1,  4,  9],
       [ 9,  4,  1,  0,  1,  4],
       [16,  9,  4,  1,  0,  1],
       [25, 16,  9,  4,  1,  0]])

array([[ 0,  1,  4,  9, 16, 25],
       [ 1,  0,  1,  4,  9, 16],
       [ 4,  1,  0,  1,  4,  9],
       [ 9,  4,  1,  0,  1,  4],
       [16,  9,  4,  1,  0,  1],
       [25, 16,  9,  4,  1,  0]])

Process returned 0 (0x0)        execution time : 0.746 s
계속하려면 아무 키나 누르십시오 . . .
"""
