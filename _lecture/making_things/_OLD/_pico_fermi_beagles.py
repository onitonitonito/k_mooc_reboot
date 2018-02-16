import random
""" file: doc_string : random drill
 (1) random.randint(start, end) : incl'd end number
 (2) random.choice(arr)
 (3) random.shuffle(arr)
 """

def test1_rand_func():
    _a = random.randint(0, 9)
    print('\nrandint= %s' %_a)

    _a = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print('\nrand.choice= %s' %_a)

    _a_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('\nbefore... %s \n\n' %_a_arr)

    for n in range(10):
        random.shuffle(_a_arr,)
        print('shuffle!...  %s' %_a_arr)
# test1_rand_func()
