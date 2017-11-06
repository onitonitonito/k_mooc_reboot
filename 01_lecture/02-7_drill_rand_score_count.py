"""  Randome Score counting in enuberate, zip,
"""
import random

NUM_CLASS = 40      # Total num of person in a class.
CUT_LINE = 90       # limit line of ove all average score of three subjects

def get_name_arr_to(number):        # OUT = 'list'
    first_nameDB = '김이박최남오주전류유천방지축마골피'
    middle_nameDB= '경정현상아나인진이류주미철난성천'
    trail_nameDB = '수주민현하나진철순주나연선은꼴'

    name_arr = []
    counter = 0

    while True:
        counter += 1
        name = (random.choice(first_nameDB) + \
                random.choice(middle_nameDB) + \
                random.choice(trail_nameDB))

        if name in name_arr:
            counter -= 1
            pass
        else:
            name_arr.append(name)

        if counter >= number:
            break
    return name_arr

class_name_arr = get_name_arr_to(NUM_CLASS)
score_korean = [5*(random.randint(64, 104)//5) for n in range(NUM_CLASS)]
score_math = [5*(random.randint(64, 104)//5) for n in range(NUM_CLASS)]
score_english = [5*(random.randint(64, 104)//5) for n in range(NUM_CLASS)]

num_success = 0

for i, card  in enumerate(zip(class_name_arr, score_korean, score_english, score_math)):
    # show personal score card incl' (name-korean-english-math)
    print('%3s. %s'% (i+1, card))
    _average = (card[1] + card[2] + card[3]) / 3

    if _average >= CUT_LINE:
        num_success += 1
        print('----- %s SUCCESSES to achieve %s -------%s\n\n'%(
                            card[0], CUT_LINE, num_success))

print('\n\n ::: TOTAL %s Achiever(s) is(are) %s person(s)...'% (
                                CUT_LINE, num_success))
