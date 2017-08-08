#!python
import time, os

RUN_IMAGE = [
 '''
 .ooooo.
 oo..oo.
 oo..oo.
 oo..oo.
 ooooo..''',
 '''
 ..oo...
 oooo...
 ..oo...
 ..oo...
 oooooo.''',
 '''
 .ooooo.
 o...oo.
 ..ooo..
 ooo....
 oooooo.''',
 '''
 .ooooo.
 ....oo.
 .oooo..
 ...ooo.
 ooooo..''',
 '''
 ...oo..
 .oo.o..
 oo..o..
 oooooo.
 ....o..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 ....oo.
 ooooo..''',
 '''
 .ooooo.
 oo.....
 oooooo.
 oo..oo.
 .oooo..''',
 '''
 oooooo.
 o...oo.
 ...oo..
 ..oo...
 .oo....''',
 '''
 .ooooo.
 oo..oo.
 .oooo..
 oo..oo.
 .oooo..''',
 '''
 .ooooo.
 oo...o.
 oooooo.
 ....oo.
 ooooo..''',
 ]

def display_graph_number(number):   # In='str' / Out='str'
    """ show 2-byte Box Letter """
    str_number = RUN_IMAGE[number].replace('.','∵').replace('o','■')
    return str_number           # <class 'str'>

def display_text_number(number):   # In='str' / Out='str'
    """ show 1-byte ASC Letter """
    str_number = RUN_IMAGE[number]
    return str_number           # <class 'str'>

def display_mode_number(mode, number):   # In = 'int', 'int' / Out = 'str'
    """  """
    if mode == 1:
        str_number = display_graph_number(number)
    elif mode == 2:
        str_number = display_text_number(number)
    elif mode == 3:
        str_number = display_graph_number(number) + display_text_number(number)
    else:
        raise KeyboardInterrupt
    return str_number           # <class 'str'>

def mix_2digits(mode=1, num_1=0, num_2=0):
    digit_2t = digit_2g = ""

    num_1g_arr = display_graph_number(num_1).split('\n')
    num_2g_arr = display_graph_number(num_2).split('\n')

    num_1t_arr = display_text_number(num_1).split('\n')
    num_2t_arr = display_text_number(num_2).split('\n')


    for n in range(len(num_1g_arr)):
        digit_2t = digit_2t + (num_1t_arr[n].strip() + num_2t_arr[n].strip() +"\n")
        digit_2g = digit_2g + (num_1g_arr[n].strip() + num_2g_arr[n].strip() +"\n")


    if mode == 1:
        return digit_2g

    elif mode == 2:
        return digit_2t

    elif mode == 3:
        return (digit_2g + digit_2t)

    else:
        print(" \n\n")
        print(" MODE 1=TEXT, 2=BOX 3=BOTH")
        print(" Please, chose one out of three.")

        raise KeyError

def countdown(mode=1, from_n=9):
    """ mode : 1= graph, 2= text, 3= both """
    number = 0
    for n in range(from_n,-1,-1):
        print('\n\n'*3)

        if n > 9:
            str_n = str(n)
            # print(mode, str_n[0], str_n[1])
            str_number = mix_2digits(mode, int(str_n[0]), int(str_n[1]))
        else:
            str_number = display_mode_number(mode, n)

        print(str_number)
        time.sleep(0.01)
        os.system('cls')


if __name__ == '__main__':
    countdown(2,50)
    countdown(1,50)
    countdown(3,50)

    print(mix_2digits(mode=1,num_1=7,num_2=5))
    print(mix_2digits(mode=2,num_1=7,num_2=5))
    print(mix_2digits(mode=3,num_1=7,num_2=5))
