""" file doc-string : Pici-Fermi-Beagles game
# comp. gives clues, 10 times.... like below
# ------------
# (1) Pico : correct but wrong position
# (2) Fermi : correct and right position
# (3) Beagles : neither correct nor right postion
"""

import random
import os

HINT_FRAME = """
 _%s_ : MY NUMBER
 _________________________________________________
 MY HINT= ....... %s
 chaces left (%s) %s
 .................................................\n\n\n"""

LOOSER_FRAME = """
 _%s_ : MY NUMBER
 MY HINT= ....... %s (WHAT?..OMG! BEAGLES?!!!)
 chaces left (%s) %s\n\n\n"""

CONGRATES_FRAME = """
 \n\n\n\n
 \t~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
 \t
 \t !!.. CONGRATULATIONS ...!!!
 \t     ... YOU'VE GOT ...
 \t     ~ %s 'FERMIs' ~
 \t           =^.^=
 \t   Only just (%s) trials
 \t
 \t_*_*_*_*_*_*_*_*_*_*_*_*_*_*_
 \n\n\n\n"""

RAND_ARR = [n for n in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
GLOBAL_DIGIT = 4
CHANCE = 10

def get_rand_num_from(RAND_ARR):  # IN='list/ OUT='str' num
    """ get GLOBAL_DIGIT-number, not repeated.
 pick from RAND_ARR=[0, 1, ... 9] = 10 int_arr
 In = int_arr / Out = GLOBAL_DIGITs-num_str """
    random.shuffle(RAND_ARR)    # [1, 8, 4, 5, 2, 6, 3, 0, 7, 9]
    rand_num_str = ''
    for pos in range(GLOBAL_DIGIT):
        rand_num_str += str(RAND_ARR[pos])
    return rand_num_str

def get_input_num_str():        # OUT = 'int'
    return input('Input your %s-digit Number  : '% GLOBAL_DIGIT)

def show_num_attribute(num_str):
    if num_str.isnumeric():
        print('.......numbers/numeric...')
    if num_str.isalpha():
        print('..............alphabet...')
    if num_str.isalnum():
        print('.........alpha-numeric...')

def is_number_not_twice(num_str):
    check_str = '0123456789'

    for pos in range(GLOBAL_DIGIT):    # upto 10 digits
        if num_str[pos] in check_str:
            _pos = check_str.find(num_str[pos])
            if _pos == 0:
                check_str = check_str[1:]
                # print(check_str)
            elif _pos == 9:
                check_str = check_str[:9]
                # print(check_str)
            else:
                check_str = check_str[:_pos] + '' + check_str[_pos+1:]
                # print(check_str)
        else:
            return False        # num not exits means 'twice'
    return True

def is_valid_num(num_str, show_flag=0):
    if show_flag == 1:
        show_num_attribute(num_str)

    if num_str.isnumeric():
        if len(num_str) == GLOBAL_DIGIT:
            return True
        else:
            return False
    else:
        return False

def get_cleaned_input_loop(RAND_ARR):   # OUT= 'str' cleaned num_str
    while True:
        num_str = get_input_num_str()

        if is_valid_num(num_str, show_flag=0):
            if is_number_not_twice(num_str):
                return num_str
            else:
                print('ERROR(1) ... some number(s) input more than TWICE! \n\n')
        else:
            print('ERROR(2) ... invalid number!! \n\n')

def is_try_again():
    """ only if str.lower() = 'y', return True
    every other elses return all False """
    return input('\tTry again (y/n)?... ').lower().startswith('y')


com_num_str = get_rand_num_from(RAND_ARR)            # GD-digits 'str'
counter = 0

while True:
    counter += 1
    my_num_str = get_cleaned_input_loop(RAND_ARR)       # GD-digits 'str'

    # print('ME =', my_num_str)
    # print('COM=', com_num_str)

    judge_dict = {'PICO':0, 'FERMI':0, 'BEAGLES':0}   # [PICO, FERMI, BEAGLES]

    for pos in range(GLOBAL_DIGIT):
        if my_num_str[pos] in com_num_str:
            _pos = com_num_str.find(my_num_str[pos])
            judge_dict['PICO'] += 1

            if _pos == pos :
                judge_dict['PICO'] -= 1
                judge_dict['FERMI'] += 1

    if judge_dict['PICO'] == 0 and judge_dict['FERMI'] == 0:
        judge_dict['BEAGLES'] = 1

    judge_str = ''

    for pos in range(3):                # PICO, FERMI, BEAGLES = 3
        if list(judge_dict.values())[pos]:
            judge_str += '%s %s, '% (
                            str(list(judge_dict.values())[pos]),
                            list(judge_dict.keys())[pos])

    chance_bars = '■'*(CHANCE - counter)

    if judge_dict['BEAGLES'] == 1:
        print(LOOSER_FRAME% (
                            my_num_str,
                            judge_str,
                            (CHANCE - counter),
                            chance_bars))
    else:
        print(HINT_FRAME% (
                            my_num_str,
                            judge_str,
                            (CHANCE - counter),
                            chance_bars))

    if counter >= CHANCE:
        print("\n\n... run out of chances,  It's OVER!! ....")
        print("The Ansewer Was .... [ %s ] .. you lose"% com_num_str)

        if is_try_again():
            """ initialize all variables & again! """
            com_num_str = get_rand_num_from(RAND_ARR)   # GD-digits 'str'
            counter = 0
            os.system('cls')            # only available at 'CONSOLE SCREEN'
        else:
            """ NOT 'y' = stop playing """
            break


    if judge_dict['FERMI'] == GLOBAL_DIGIT:
        print(CONGRATES_FRAME% (GLOBAL_DIGIT, counter))

        if is_try_again():
            """ initialize all variables & again! """
            com_num_str = get_rand_num_from(RAND_ARR)   # GD-digits 'str'
            counter = 0
            os.system('cls')            # only available at 'CONSOLE SCREEN'
        else:
            """ NOT 'y' = stop playing """
            break
