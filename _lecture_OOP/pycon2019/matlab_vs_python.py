"""
# Pycon2019- matlab user to python user
# https://www.facebook.com/groups/pythonkorea/
# permalink/2401133333303147/
#
# P.23 - pptx
"""
# print(__doc__)

from numba import jit
import random


@jit(nopython=True)
def get_monte_carlo_pi(n_samples):
    """
    JIT Decorator speed test : with/without - https://numbar.pydata.org
        - get Pi - n_samples = 10**8
        - w/o = 3.1415744 ... [Finished in 79.083s]
        - w/  = 3.1414302 ... [Finished in  2.872s]
    """
    acc = 0
    for i in range(n_samples):
        x = random.random()
        y = random.random()

        if (x**2 + y**2) < 1.0:
            acc +=1
    return 4.0*acc / n_samples


def main():
    pi = get_monte_carlo_pi(10**8)
    print(pi)


if __name__ == '__main__':
    main()
