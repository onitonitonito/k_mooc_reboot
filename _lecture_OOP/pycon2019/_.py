"""
# Jupyter notebook '%time' code substitution
#
"""
# import numpy as np
#
# my_arr = np.arange(10**6)
# my_list = list(range(10**6))
#
# %time
# for _ in range(10):
#     my_arr2 = my_arr * 2

print(__doc__)

import timeit
import numpy as np

my_arr = np.arange(100)
my_list = list(range(100))

def test():
    for _ in range(10):
        my_arr2 = my_arr * 2

# 11.81385137899997

def run(func, arg=None):
    print("I'm thinking...")

    print('pass=', timeit.timeit(stmt="pass", setup="pass", ))
    print('test=', timeit.timeit(stmt="test()", setup="from __main__ import test"))

    print('Done!...')



if __name__ == '__main__':
    run(test, arg=None)

    pass
