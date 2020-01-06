"""
# how to stack echo file
"""

print(__doc__)

import random
from assets.config import dir_statics
from string import ascii_letters

SYMBOLS = [sym for sym in "!@#$%^&*()_-+=,.?/|;:{}~{}" + ascii_letters]
RANDOM_START = (0, 39)
RANDOM_END = (40, 78)
LINES = 50
REPEAT = 10
FILE_NAME = dir_statics + 'test_echo_array.txt'

def main():
    for i in range(REPEAT):
        print(*get_echo_array(write=True))

def get_echo_array(write=False):
    echo_array = []
    for i in range(LINES):
        random.shuffle(SYMBOLS)
        x1, x2 = (random.randint(*RANDOM_START), random.randint(*RANDOM_END))

        string_shuffled = "".join(SYMBOLS)

        add_string = string_shuffled[x1:x2]
        echo_array.append(f"\n{add_string}")

    if write:
        with open(file=FILE_NAME, mode='w', encoding='utf8') as f:
            f.write("".join(echo_array))

    return echo_array


if __name__ == '__main__':
    main()
