#! python
""" HOW TO MAKE A FUNCTION : PEP RULES
  --------------------
  Definition = Call by Value () / Call by Reference (mem.address)
"""

def test01_call_by_reference():
    """ TEST.01 - Where's address :: id() """
    _a = 3
    print('id(_a) = ', _a, id(_a))
    print('id(3)  = ', 3, id(3), end='\n\n')

    _b = 3
    print('id(_b) = ', _b, id(_b))
    print('id(3)  = ', 3, id(3), end='\n\n')

    _b = 4
    print('id(_b) = ', _b, id(_b))
    print('id(4)  = ', 4, id(4), end='\n\n')

    _c = _b + 0
    print('id(_c) = ', _c, id(_c))
    print('id(0)  = ', 0, id(0), end='\n\n')

def spam(eggs):
    """ TEST.02 - SPAM(EGGS), SPAM(HAM)"""
    print('eggs_01 =',id(eggs), eggs)

    eggs.append(1)
    print('eggs_02 =',id(eggs), eggs)

    eggs = [2, 3]           # New one! New address!
    print('eggs_03 =',id(eggs), eggs)

def main():
    ham = [0,]
    print('before_ham =',id(ham), ham)

    spam(ham)
    print('after_ham',id(ham), ham)
# main()
    # before_ham = 38687768 [0]
    # eggs_01 = 38687768 [0]
    # eggs_02 = 38687768 [0, 1]
    # eggs_03 = 38687808 [2, 3]     **** different eggs
    # after_ham 38687768 [0, 1]

def get_quadratic_eq(a, b, c):  # IN='int' x 3 / OUT=2 'float'
    """ TEST.03 - quadratic formula : quadratic equation
    max 2 answers for f(x) = a.x**2 + b*x + x = 0 """
    import math

    _a_arr = []
    _D = b**2 - 4*a*c

    if _D >= 0:
        _a_arr.append((-b + math.sqrt(_D))/2*a)
        _a_arr.append((-b - math.sqrt(_D))/2*a)
        print()
        print('id(_a_arr) =',_a_arr ,id(_a_arr), end='\n\n')

    else:
        _a_arr.append('[ -%s+SQRT(%.3f.i) ] / %s'% (b, -_D, 2*a))
        _a_arr.append('[ -%s-SQRT(%.3f.i) ] / %s'% (b, -_D, 2*a))
        print('if D < 0, 2 Imaginary Numbers')
        print('id(_a_arr) =', _a_arr, id(_a_arr), end='\n\n')

    return _a_arr

def main(a, b, c):
    _a_arr = get_quadratic_eq(a, b, c)

    for _a in _a_arr:
        print(_a)
    print('id(_a_arr) =', id(_a_arr))
main(1, 3.6, 4)         # Imaginary number
