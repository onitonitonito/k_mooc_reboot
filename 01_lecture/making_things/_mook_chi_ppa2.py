import random
import os

pieces_arr = [                              # smaller POS will WIN!
            ['BAWUI', 'KAWUI', 'BO'],       # KOREAN Version..
            ['Rock', 'Scissors', 'Paper'],  # ENGLISH Version..
            ['MOOK', 'CHI', 'PPA'],]        # KOREAN in slang Version..

total_score_arr = [0, 0, 0]

def get_user_arr(_n_random, kind_piece=1):  # default = Korean
    picked_piece = pieces_arr[kind_piece][_n_random]
    return (picked_piece, (_n_random, _n_random+3))

def set_piece_arr_to_user():                  # OUT= ('str', ('int','int'))
    _n_random = random.randint(0,2)
    user_arr = get_user_arr(_n_random, kind_piece=1)   # ('str', ('int','int'))
    return user_arr

def get_judge_table(mine_arr, oppo_arr):      # OUT= [n0, n1, n2, n3]
    """ if judge_table contains a value ( -1 = Win / 0 = draw / 1 = lose )
        A-B differences calculation : 2 x 2 = 4 cases
    """
    judge_table = []    # [0, 1, 2, 3]

    judge_table.append(pick_mine_arr[1][0] - pick_oppo_arr[1][0])
    judge_table.append(pick_mine_arr[1][0] - pick_oppo_arr[1][1])
    judge_table.append(pick_mine_arr[1][1] - pick_oppo_arr[1][0])
    judge_table.append(pick_mine_arr[1][1] - pick_oppo_arr[1][1])
    return judge_table # [0, 1, 2, 3]

n_trial = 0

while True:
    n_trial += 1
    for n in range(10):
        pick_mine_arr = set_piece_arr_to_user()   # ('str', ('int','int'))
        pick_oppo_arr = set_piece_arr_to_user()   # ('str', ('int','int'))

        print('%s vs %s'% (pick_mine_arr[0], pick_oppo_arr[0]))

        judge_table = get_judge_table(pick_mine_arr, pick_oppo_arr)

        if 1 in judge_table:
            total_score_arr[2] += 1
            print("DEFEATED....")

        elif 0 in judge_table:
            total_score_arr[1] += 1
            print("--- DRAW ---")

        elif -1 in judge_table:
            total_score_arr[0] += 1
            print("VICTORY!!!................. ^^")
        print()

    print('Your Score [W,D,L] = %s :   Try = %d times'% (total_score_arr, n_trial))
    print('__'*30 + '\n')

# ---------------------------------------------------------------
    try:
        int(input('Try Again? [Y="1" / No="Enter"]'))
    except:
        raise SystemExit
# ---------------------------------------------------------------

    os.system('cls')
    total_score_arr = [0, 0, 0]

""" 10 times - step by step
"""
