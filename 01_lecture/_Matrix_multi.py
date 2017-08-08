# a = [[12,13],
#      [10,11]]
#
# b = [[1,2],
#      [3,4]]
#
# c = a + b
#
# print(c)
#
# '''
# [[12, 13], [10, 11], [1, 2], [3, 4]]
# [Finished in 0.749s]
# '''


import numpy as np

a = np.arange(2*2).reshape([2,2])
b = np.arange(2*2).reshape([2,2])
print(type(a),'\n',a)
print(type(b),'\n',b)

c = a @ b
print(type(c),'\n',c)

'''
<class 'numpy.ndarray'>
 [[0 1]
 [2 3]]
<class 'numpy.ndarray'>
 [[0 1]
 [2 3]]
<class 'numpy.ndarray'>
 [[ 2  3]
 [ 6 11]]
[Finished in 1.273s]
'''
