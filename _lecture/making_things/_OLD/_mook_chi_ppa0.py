import random
import os

pieces_array = [
            ['MOOK', 'CHI', 'PPA'],
            ['바위', '가위', '보'],
            ['Rock', 'Scissors', 'Paper'],]

_pieces_array = [
            ['Rock', 'MOOK', '바위'],
            ['Scissors', 'CHI', '가위'],
            ['Paper', 'PPA', '보'],]

def get_random_pick(_n_random, kind_piece=1):  # default = Korean
    picked_piece = pieces_array[kind_piece][_n_random]
    return (picked_piece, (_n_random, _n_random+3))

def _test0_random_pick(_n_random, kind_piece=1):
    for n in range(20):
        pick_oppo, arr_n = get_random_pick(_n_random, kind_piece)
        print('%2s = %s'% (n+1, pick_oppo))
# _test0_random_pick(kind_piece=0)

total_score_arr = [0, 0, 0]

while True:
    for n in range(10):
        _n_random = random.randint(0,2)
        pick_mine_arr = get_random_pick(_n_random)   # ('str', ('int','int'))

        _n_random = random.randint(0,2)
        pick_oppo_arr = get_random_pick(_n_random)   # ('str', ('int','int'))

        print('%s vs %s'% (pick_mine_arr[0], pick_oppo_arr[0]))

        judge_win_lose_arr = []
        judge_win_lose_arr.append(pick_mine_arr[1][0] - pick_oppo_arr[1][0])
        judge_win_lose_arr.append(pick_mine_arr[1][0] - pick_oppo_arr[1][1])
        judge_win_lose_arr.append(pick_mine_arr[1][1] - pick_oppo_arr[1][0])
        judge_win_lose_arr.append(pick_mine_arr[1][1] - pick_oppo_arr[1][1])

        if 1 in judge_win_lose_arr:
            total_score_arr[2] += 1
            print("DEFEATED....")

        elif 0 in judge_win_lose_arr:
            total_score_arr[1] += 1
            print("___ DRAW ______")

        elif -1 in judge_win_lose_arr:
            total_score_arr[0] += 1
            print("VICTORY!!!................. ^^")
        print()

    print('Your Score [W,D,L] = ', total_score_arr)
    print('__'*30 + '\n')

# ---------------------------------------------------------------
    try:
        int(input('Try Again? [Y="1" / No="Enter"]'))

    except:
        raise SystemExit
# ---------------------------------------------------------------
    os.system('cls')
    total_score_arr = [0, 0, 0]
