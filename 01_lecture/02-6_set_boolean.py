#!/usr/bin python
""" ------------------- CHAPTER.02 LESSON.06--- Set, Boolean
 set function = intersection(), union(), difference()
"""
import random

def get_number_postfix(n):          # IN='int' / OUT='str'
    if n == 1:
        postfix = 'st.'
    elif n == 2:
        postfix = 'nd.'
    elif n == 3:
        postfix = 'rd.'
    else:
        postfix = 'th.'
    return postfix

""" What's the difference? : array & set """
a_arr = [ random.randint(0,10) for n in range(10)]
# a_arr.sort()
print(a_arr, end='\n\n')       # a_arr = [4, 10, 7, 7, 10, 4, 0, 1, 8, 8]

b_set = set(a_arr)
print(b_set, end='\n\n')       # b_set = {0, 1, 4, 7, 8, 10}


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

""" Try to use : enumerate() = add index number into array(list) data """
for i, _a in enumerate(a_arr):
    postfix = get_number_postfix(i+1)
    print("%2s %s. array data, a_arr[%s]= '%s'"% (i+1, postfix, i, _a))

bad_list = ['talking to much in class',
            'noisy in public places',
            'being easily annoyed',
            'lazy in the morning',
            ]

for i, bad_habit in enumerate(bad_list):
    if i == 0:
        print('\n == YOUR BAD ATTITUDES LIST ==')
    print('%s. You are.. %s'% (i+1, bad_habit))
