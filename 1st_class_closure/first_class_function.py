''' first class funtion
        - function in function (double wrapped function)
        - return function itself as a value
'''
num_list = [1,3,5,7,9]

def square (x):
    return x*x

def cube (x):
    return x*x*x

def quard(x):
    return x*x*x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))      # can apply various functions
    return result

def simple_map(arg_list):
    result = []
    for i in arg_list:
        result.append(i*i)          # only the difference
    return result

def test_01():
    ''' test_01: function can be assined as a vari.
    - gotta know the diff. between func & func(n)
    - func shows its address where they're placed.
    '''
    print("Firtst Class Function TEST \n"+"---"*10)
    print('square(5)=%s' % square(5))    # 5 * 5 = 25
    print('square=   %s' % square)       # <function square at 0x024ECC00>
    print()

    f = square                           # assign in vari.
    print('f(5)=     %s' % f(5))         # 5 * 5 = 25
    print('f=        %s' % f)            # <function square at 0x024ECC00>
    print()

def test_02():
    ''' test_02: FCF can use a funcion like variable
    - can be used as much useful as it is
    - simple_map supports only 1 equation but my_map doesn't
    '''
    squares = my_map(square, num_list)  # <class 'list'> of squares
    squaress = simple_map(num_list)     # <class 'list'> of squares-simple

    print("my_map function TEST \n"+"---"*10)
    print("INPUT    = %s" % num_list)
    print()

    print("SQUARES  = %s" % squares)
    print("SQUARESS = %s" % squaress)
    print()
    print()  # list

def test_03():
    ''' First Class Function : Change functions
    - mapping list value according to various funcs.
    - functions = squares, cubes, quards
    '''
    squares = my_map(square, num_list)  # <class 'list'> of squares
    cubes   = my_map(cube,   num_list)  # <class 'list'> of cubes
    quards  = my_map(quard,  num_list)  # <class 'list'> of quards

    print("my_map function TEST \n"+"---"*10)
    print("INPUT  = %s" % num_list)
    print()

    print("SQURES = %s" % squares)
    print("CUBES  = %s" % cubes)
    print("QUARDS = %s" % quards)
    print()
    print()  # list


def main():
    print(test_01.__doc__)
    test_01()

    print(test_02.__doc__)
    test_02()

    print(test_03.__doc__)
    test_03()

if __name__ == '__main__':
    main()
