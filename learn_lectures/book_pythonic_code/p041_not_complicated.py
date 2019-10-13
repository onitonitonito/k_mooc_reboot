import urllib.parse
# from urllib.parse import parse_qs
""" urllib.parse.parse_qs : changes parameters into DICT_Values
  {'red': ['5'], 'blue': ['0'], 'green': ['']}
  """
my_values = urllib.parse.parse_qs('red=5&blue=0&green=', keep_blank_values=True)

def not_use_complex_method():
    # print(repr(my_values))        # all the same
    print(my_values)      # {'red': ['5'], 'blue': ['0'], 'green': ['']}

    print()
    print('RED:      ', my_values.get('red'))
    print('GREEN:    ', my_values.get('green'))
    print('OPACITY:  ', my_values.get('opacity'))
    # it shows <class 'list'> : RED:       ['5']

    print()
    RED = my_values.get('red', ['']) [0] or 0
    GREEN = my_values.get('green', ['']) [0] or 0
    OPACITY = my_values.get('opacity', ['']) [0] or 0
    print('RED =     ', RED)
    print('GREEN =   ', GREEN)
    print('OPACITY = ', OPACITY)

    print()
    RED = my_values.get('red', [''])
    RED = int(RED[0]) if RED[0] else 0
    print('RED =     ', RED)
# not_use_complex_method()

def get_first_integer(values, key, default=0):
    """ helper function = derive integer from DICT_Values """
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

def use_helper_function():
    print()
    red = get_first_integer(my_values, 'red')
    blue = get_first_integer(my_values, 'blue')
    green = get_first_integer(my_values, 'green')
    opacity = get_first_integer(my_values, 'opacity')
    print('helper func.red =     ', red)
    print('helper func.blue =    ', blue)
    print('helper func.green =   ', green)
    print('helper func.opacity = ', opacity)
# use_helper_function()

def enumerate_than_range():
    """ Better Way 10 - use enumerate more than range : page.41
    """
    import random

    random_bites = 0
    for i in range(64):
        if random.randint(0, 1):
            random_bites |= 1 << i
    flavor_list = ['vanila', 'chocolate', 'pecan', 'strawberry']

    print()
    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print('%d: %s' %(i+1, flavor))

    # use enumerate instead, all the same.
    print()
    for i, flavor in enumerate(flavor_list):
        print("%s : %s" %(i+1, flavor))
# enumerate_than_range()      # 4 : strawberry

def zip_than_enumerate():
    """ Better Way 11 - use zip more than enumerate : page.45
    """
    longest_name = None
    max_letters = 0

    names = ['Lisa', 'Celilia', 'Marie']
    letters = [len(n) for n in names]       # numbers of names = [4, 7, 5]

    """ GOOD, but a bit compex """
    for i in range(len(names)):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = letters[i]
    print("The longest_name = %10s,(%d)"%(longest_name, max_letters))

    """ BETTER, a bit neat but still confusing """
    for i, name in enumerate(names):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = letters[i]
    print("The longest_name = %10s,(%d)"%(longest_name, max_letters))

    """ BEST, using zip() will be readable! """
    for name, count in zip(name, letters):
        if count > max_letters:
            longest_name = names[i]
            max_letters = letters[i]
    print("The longest_name = %10s,(%d)"%(longest_name, max_letters))
# zip_than_enumerate()        # The longest_name =    Celilia,(7)

import os
DESTIN_DIR = os.path.join(os.path.dirname(__file__),'txt\\')
FILENAME = 'random_data.pdb'

def simeple_read_out():
    """ using try / finally, simple read out & make """
    if not os.path.isdir(DESTIN_DIR):
        os.mkdir(DESTIN_DIR)

    if not os.path.exists(DESTIN_DIR+FILENAME):
        handle = open(DESTIN_DIR+FILENAME, 'w', encoding='utf8')
        handle.write('*** START TO WRITE A DB-TEXT ***\n')
        handle.close()

    handle = open( DESTIN_DIR + FILENAME)   # can cause IOError.

    try:
        data = handle.read()
    finally:
        handle.close()                      # always CLOSE!

    print('data = ',data)
# simeple_read_out()          # data =  *** START TO WRITE A DB-TEXT ***

def devide_json(path):
    """ try / except / else / finally COMBO! always useful
    but this is just an example, not executable!. sorry
    """
    import json

    UNDEFINED = object()
    handle = open(path, 'r+')   # can cause IOError.
    try:
        data = handle.read()    # can cause UnicodeDecodeError.
        op = json.loads(data)
        value = (op['numerator'] / op['denominator'])
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seel(0)
        handle.write(result)        # can cause IOError.
        return value
    finally:
        handle.close()              # always CLOSE!

numbers = [8, 3, 1, 2, 5, 4, 7, 6,]     # <class 'list'>
group = {2, 3, 5, 7}                    # <class 'set'>

def sort_priority(numbers, group):
    """ simple closer example : double wrapped function
        aimed to remain function as a value
    """
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)     # key = helper() function

sort_priority(numbers, group)
print(numbers)                      # sorted -> [2, 3, 5, 7, 1, 4, 6, 8]
