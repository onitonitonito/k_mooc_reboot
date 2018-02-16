import datetime
import random
import os

pieces_arr = [                              # smaller POS will WIN!
            ['BAWUI', 'KAWUI', 'BO'],       # KOREAN Version..
            ['Rock', 'Scissors', 'Paper'],  # ENGLISH Version..
            ['MOOK', 'CHI', 'PPA'],]        # KOREAN in slang Version..

total_score_arr = [0, 0, 0]

def get_user_arr(_n_random, kind_piece=1):  # default = Korean
    picked_piece = pieces_arr[kind_piece][_n_random]
    return picked_piece, (_n_random, _n_random+3)

def set_piece_arr_to_user():                  # OUT= ('str', ('int','int'))
    _n_random = random.randint(0,2)
    user_arr = get_user_arr(_n_random, kind_piece=1)   # ('str', ('int','int'))
    return user_arr

def get_judge_table(mine_arr, oppo_arr):      # OUT= [n0, n1, n2, n3]
    """ if judge_table contains a value ( -1 = Win / 0 = draw / 1 = lose )
        A-B difference calculations : 2 x 2 = 4 cases
    """
    judge_table = []        # [n0, n1, n2, n3]

    judge_table.append(pick_mine_arr[1][0] - pick_oppo_arr[1][0])
    judge_table.append(pick_mine_arr[1][0] - pick_oppo_arr[1][1])
    judge_table.append(pick_mine_arr[1][1] - pick_oppo_arr[1][0])
    judge_table.append(pick_mine_arr[1][1] - pick_oppo_arr[1][1])
    return judge_table      # [n0, n1, n2, n3]

n_trial = 0                 # trial number of set trials.

time_laps_start = datetime.datetime.now()

while True:
    if n_trial == 0:
        print('\n'*10 + '\t\t ...... thinking ......' + '\n'*15)

    n_trial += 1
    os.system('cls')
    for n in range(10):     # competes 20 times
        pick_mine_arr = set_piece_arr_to_user()   # ('str', ('int','int'))
        pick_oppo_arr = set_piece_arr_to_user()   # ('str', ('int','int'))
        print('%s vs %s'% (pick_mine_arr[0], pick_oppo_arr[0]))

        # [n0, n1, n2, n3]
        judge_table = get_judge_table(pick_mine_arr, pick_oppo_arr)

        if -1 in judge_table:
            total_score_arr[0] += 1
            print("VICTORY!!!................. ^^")

        elif 0 in judge_table:
            total_score_arr[1] += 1
            print("--- DRAW ---")

        elif 1 in judge_table:
            total_score_arr[2] += 1
            print("DEFEATED....")
        print()

    print('Your Score [W,D,L] = %s :   Try = %d times'% (total_score_arr, n_trial))
    print('__'*30 + '\n')

    if total_score_arr[0] == 7:            # if, 20 wins in a row
        time_laps_end = datetime.datetime.now()
        time_laps = (time_laps_end - time_laps_start)
        # print(type(time_laps))
        print('\a', end='')                 # make beep sounds = escape[a]
        print('Your Score [W,D,L] = %s :   Try = %s times / %s Sec'%(
                            total_score_arr,
                            str(n_trial)[:-3] + ',' + str(n_trial)[-3:],
                            str(time_laps)[-13:-3]))
        print('__'*35 + '\n')
        print(n_trial, end=' : ') # for compare to combo-string

        # ------------------ [ PAUSE for KEY-IN] ------------------------
        try:
            int(input('Try Again? [Y="1" / No="Enter"]'))
        except:
            raise SystemExit
        # ---------------------------------------------------------------

        n_trial = 0
        time_laps_start = datetime.datetime.now()

    total_score_arr = [0, 0, 0]

""" How much times will it takes if I win 10 times in a row...!!!!! *.*
  because it's too slow to get result, MASKED all lazy processes (Like, print)
  if achieve, break, show(trials, times)

     8/10 :  -->         542 times /     0.791 sec
     9/10 :  -->       1,726 times /     1.092 sec
    10/10 :  -->     131,250 times /    55.607 sec

    15/20 :  -->      80,647 times /    10.562 sec
    16/20 :  -->     227,400 times /    36.350 sec
    17/20 :  -->     702,584 times /  1:33.682 sec
    18/20 :  -->   2,095,919 times /  4:42:590 sec
    19/20 :  -->  22,123,903 times / 48:48:660 sec
    20/20 :  -->   times /   sec
"""
