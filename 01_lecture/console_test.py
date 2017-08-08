
def testInput():
    print ("Enter Your name: ")
    input_name = input()

    print("H1~!! %s"%input_name)


    print ("Enter Temperature: ")
    # input_temp = float(input())
    input_temp = int(input())

    print("The Temperature is ", input_temp)
    print("input type =", type(input_temp))
    print()
testInput()

def thisSimple():
    """ Python is so simple """
    languages = ['python', 'perl', 'c', 'java']
    for lang in languages:
        if lang in ['python', 'perl']:
            print("%6s need interpreter" % lang)
        elif lang in ['c', 'java']:
            print("%6s need compiler" % lang)
        else:
            print("should not reach here")
thisSimple()
