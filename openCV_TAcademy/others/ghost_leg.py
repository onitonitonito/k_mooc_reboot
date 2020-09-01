"""
# CodinGame.com Solutions by pathosDev
# github.com/pathosDev = https://bit.ly/3jldALh
"""
# * Date solved: 22.02.2019
# * Puzzle: GhostLegs
# * Difficulty: Easy

import time
import random
from typing import (List, Dict)

asks = {
    'excludes' : 'Key-In Exceptions   [Ent.]: No!',
    'name' : 'Names of Participants? (divid by comma) :',
    'reward' : 'How Many Rewards?      [Ent.]: 1 (default)',
    'result' : '[SPC+Ent]:See Result / [Ent.]: Skip! :',
    'again'  : '[SPC+Ent]:Again!     / [Ent.]: Quit! : ',
}

num_story = 10
num_reward = 4
# check = input(asks['reward'])
# num_reward = 1 if check.startswith('') else int(check)

names = ['Kay', 'June', 'Philip', 'David', 'Baek', 'Tsong', 'Json'] * 2
# names = input(asks['name']).split(',')
random.shuffle(names)

# excludes = input(asks['excludes']).split(',')
excludes = ['Kay',]
if excludes != '':
    for ex in excludes:
        # remove all the same value in list! : SOF = https://bit.ly/3llL4ez
        # names = list(filter(ex.__ne__, names))
        names = list(filter(lambda x: x != ex, names))


# '1' can't be placed in a row more than once, '0' can.
ladder_pattern = "001001001000101001010100101001010" + \
                "010100100101010010000100101010010" + \
                "101010100100101001010101010101001"

num_person = len(names)
idx_person = list(range(num_person))


def get_random_reward(
    num_reward:int,
    num_person:int,) -> List[str]:
    """# shuffle reward array"""

    idx_reward = ['OK'] * num_reward + [' '] * (num_person - num_reward)
    random.shuffle(idx_reward)
    return idx_reward

def get_random_ladders(
        ladder_pattern:str,
        num_person:int,
        num_story:int) -> List[str]:
    """# get Array of 1-story patterns from random ladder pattern"""

    ladders = []
    for i in range(num_story):
        pos = random.randint(0, len(ladder_pattern)-num_person-1)
        line = ladder_pattern[pos:pos+(num_person-1)]
        line = line.replace('0', '|  ').replace('1', '|--') + '|'
        ladders.append(line)
    return ladders

def get_result(
    idx_person:List[int],
    ladders: List[str]) -> List[int]:
    """# Read diagram lines."""

    num_person = len(idx_person)
    idx_person_reorder = list(range(num_person))

    for i, line in enumerate(ladders):
        steps = line.split('|')
        for j, step in enumerate(steps):
            if step == '--':
                for k in range(num_person):
                    if idx_person_reorder[k] == j - 1:
                        idx_person_reorder[k] += 1
                    elif idx_person_reorder[k] == j:
                        idx_person_reorder[k] -= 1

    return idx_person_reorder

def show_board(
        idx_person:List[int],
        idx_reward:List[str],
        ladders:List[str]) -> None:
    """# display ladder-board """

    person, lining, ladder, reward = ("",) * 4

    for idx in idx_person:
        person += f"{str(idx+1):<3}"

    for i in range(len(idx_person)):
        lining += f"{'.':<3}"

    for i, lad in enumerate(ladders):
        ladder += lad if i == len(ladders)-1 else (lad + '\n')

    for idx in idx_reward:
        reward += f"{idx:<3}"

    print(person)
    print(lining)
    for lad in ladder.split('\n'):
        print(lad, flush=1)
        time.sleep(0.1)
    print(lining)
    print(reward)

def show_result(
    idx_person:List[int],
    idx_reward:List[str],) -> None:
    """# show result of luck person"""

    for i in range(len(idx_person)):
        if idx_reward[idx_person[i]] == 'OK':
            print(f"{i+1:02}.{names[i]} = {idx_reward[idx_person[i]]}")
        else:
            print(f"{i+1:02}.{names[i]}")

while True:
    idx_reward = get_random_reward(num_reward, num_person)
    ladders = get_random_ladders(ladder_pattern, num_person, num_story)
    idx_person_reorder = get_result(idx_person, ladders)

    show_board(idx_person, idx_reward, ladders)
    print('\n')

    if input(asks['result']).startswith(' '):    # SPC_Ent.= see result
        print('--' * 15)
        show_result(idx_person_reorder, idx_reward)
        print('--' * 15, '\n\n')

    if not input(asks['again'] + '\n\n').startswith(' '):  # Ent.=break
        break
