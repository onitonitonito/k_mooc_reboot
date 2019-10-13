#!/usr/bin python
""" ------------------- CHAPTER.02 LESSON.06--- Set, Boolean
 set function = intersection(), union(), difference()
"""
import random

a_arr = [ random.randint(0,10) for n in range(10)]
# a_arr.sort()

def test1_array_n_set():
    """ What's the difference? : array & set """
    print(a_arr, end='\n\n')       # a_arr = [4, 10, 7, 7, 10, 4, 0, 1, 8, 8]

    b_set = set(a_arr)
    print(b_set, end='\n\n')       # b_set = {0, 1, 4, 7, 8, 10}
# test1_array_n_set()

def test1_set_data():
    _str_1 = 'hello'
    _s1_set = set(_str_1)
    print(_s1_set)

    _str_2 = 'how are you'
    _s2_set = set(_str_2)
    print(_s2_set, '\n\n')

    """ (1) Union() """
    union_ = _s1_set.union(_s2_set)
    print(len(union_), union_)

    """ (2) intersection() """
    inter_ = _s1_set.intersection(_s2_set)
    print(len(inter_), inter_)

    """ (3) Difference(s2 - s1) """
    differ_ = _s1_set.difference(_s2_set)
    print(len(differ_), differ_)

    _a = [1, 2, 3, 4]

    for n in range(4):
        print(_a.pop())
# test1_set_data()

def test2_various_for_loops():
    """ Various Expressions : FOR-LOOP """
    for n in range(10):             # range(start=0, stop=10, step=1)
        print(a_arr[n], end=",")
        if n > 8:
            print('\n')

    for n in range(len(a_arr)):     # range(n) n = 'int' ... int('str')
        print(a_arr[n], end="-")
        if n > 8:
            print('\n')

    for _a in a_arr:
        if _a == a_arr[-1]:
            print(_a, end="\n")
        else:
            print(_a, end="")
    print()
# test2_various_for_loops()

def get_number_postfix(n):          # IN='int' / OUT='str'
    """ input 'int' / return postficx 'str' - st. nd. rd. th """
    if n == 1:
        postfix = 'st.'
    elif n == 2:
        postfix = 'nd.'
    elif n == 3:
        postfix = 'rd.'
    else:
        postfix = 'th.'
    return postfix

def test3_use_enumerate1():
    """ 1.Try to use : enumerate() = add index number into array(list) data """
    for i, _a in enumerate(a_arr):
        postfix = get_number_postfix(i+1)
        print("%2s %s. array data, a_arr[%s]= '%s'"% (i+1, postfix, i, _a))
# test3_use_enumerate1()

def test3_use_enumerate2():
    """ 2.Try to use : enumerate() = YOUR BAD HABBIT LIST out of Array """
    bad_list = ['talking to much in class',
                'noisy in public places',
                'being easily annoyed',
                'lazy in the morning',
                ]

    for index, bad_habit in enumerate(bad_list):
        if index == 0:
            print('\n == YOUR BAD ATTITUDES LIST ==')
        print('%s. You are.. %s'% (index + 1, bad_habit))
# test3_use_enumerate2()
