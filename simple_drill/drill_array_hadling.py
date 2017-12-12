import random
import keyword

def show_keyword_list_python():
    """ print(key for key in keyword.kwlist)
    #<generator obj. show_keyword_list_python.<locals>.<genexpr> at.. >
    print((keyword.kwlist).sort())        # 'list' but return 'None' """

    for key in keyword.kwlist:
        print(key)
# show_keyword_list_python()

sample_list = [1, 2, 3,]          # array
sample_tuple = (1, 2, 3,)
sample_dict = {'a':1, 'b':2, 'c':3}

def tes1t_add_list():
    for x in range(5):              # [1,2,3] append[4,5,6,7,8]
        sample_list.append(x+4)
    print(sample_list)
# tes1t_add_list()

def test1_add_tuple_error():
    for x in range(5):             # ERROR !!!!... Tuple can't be appended
       sample_tuple.append(x+4)
    print(sample_list)
# tes1t_add_list()

def test1_add_dict():
    """
    is_true? in dict -- lambda expression 
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    is in 'a'? ...  True
    is in 'b'? ...  True
    """
    sample_dict['d'] = 4
    print(sample_dict)

    is_in = 'a' in sample_dict
    print("is in 'a'? ... ", is_in)
    print("is in 'b'? ... ", (lambda key_str: key_str in sample_dict)('b'))
test1_add_dict()

def test2_append_new_list():
    """ The Same with the one-line comprehension list below
    sample_list = [random.randint(0,10) for n in range(10)]
    print(sample_list)
    """
    sample_list = []
    for n in range(10):
        sample_list.append(random.randint(0,10))
    print(sample_list)
# test2_append_new_list()

def test2_same_comp_list():
    sample_list = [ random.randint(0,10) for n in range(10)]
    print(sample_list)
    print(sample_list[0])
    print(sample_list[9])
# test2_same_comp_list()

def test3_matics_list():
    matrics_list = [
            [1,2,3,4,5],
            [3,4,5,6,7],
            [4,5,6,8,9],]

    print(matrics_list[0])         # [1, 2, 3, 4, 5]
    print(matrics_list[1][0])      # 3
# test3_matics_list()

def test4_dict_in_zip():
    """ Dictionary use in - ZIP function """
    name = ['Park', 'Choi', 'Kim',]
    position = ['FW','MD','DF',]
    number = [18,15,4,]

    team_dict = { number: [name, position] for name, position, number in zip(
                    number, name, position) }
    print (team_dict)

    print( 'PARK =' , team_dict['Park'] )
    print( team_dict['Park'][1] )
# test4_dict_in_zip()
