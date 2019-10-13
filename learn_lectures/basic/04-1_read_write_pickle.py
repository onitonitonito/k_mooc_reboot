"""
    (1) pickle = write directly into a file as data-format
    (2) read =
    (3) write =
    (4) os.exists & remove
"""
import os
import sys
import time
import errno
import pickle

HOME_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(HOME_DIR)
# print('HOME_DIR = %s'% HOME_DIR)     # D:\My Documents\GitHub\k_mooc_reboot

FILE_NAME = 'data_for_pickle.pdb'

def test1_make_comprehensive_list_dict():
    _a = '가나다라마바사아자차카타파하'               # 14 letters
    _b = 'ga-na-da-ra-ma-ba-sa-ah-ja-cha-ka-ta-pa-ha'.strip().split('-')  # 14

    # _num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]     # 14 numbers
    _num = [n for n in range(1, 15)]               # comprehensive list

    # _num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    # _num = [n for n in range(1,29) if n%2 == 0]     # 14 numbers

    # _num = [1, '헐~!', 3, '헐~!', 5, '헐~!', 7, 8, 9, 10, 11, 12, 13, 14]
    # _num = [n if n not in [2, 4, 6] else '헐~!' for n in range(1,15) ]

    # _num = ['헐~!', '헐~!', '헐~!', 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    # _num = [n if n not in [2, 4, 6] else '헐~!' for n in range(1,29) if n%2 == 0]

    _c_list = list(zip(_a, _b))
    print(_c_list)
    """ make list from zip object
      [('가', 'ga'), ('나', 'na'),.... , ('파', 'pa'), ('하', 'ha')]
    """

    _d_dict = {key_num: [letter, sylable]
               for key_num, letter, sylable in zip(_num, _a, _b)}
    print(_d_dict)
    """ comprehension dict -- _d_dict
      {1: ['가', 'ga'], 2: ['나', 'na'], 3: ['다', 'da'], 4: ['라', 'ra'],
            .... 13: ['파', 'pa'], 14: ['하', 'ha']}
    """
# test1_make_comprehensive_list_dict()


_a = '가나다라마바사아자차카타파하'               # 14 letters
_b = 'ga-na-da-ra-ma-ba-sa-ah-ja-cha-ka-ta-pa-ha'.strip().split('-')  # 14
_num = [n for n in range(1, 15)]
_d_dict = {key_num: [letter, sylable]
           for key_num, letter, sylable
           in zip(_num, _a, _b)}


def write_file_to_pickle(file_name_with_dir, data):
    """ if data file is not exist, make dict and write on a new file
    """
    if not os.path.exists(file_name_with_dir):
        with open(file_name_with_dir, mode='wb') as f:
            pickle.dump(data, f)
        print('*** A NEW WRITE PROCESS HAS BEEN DONE ***', flush=True)
    else:
        print('O.K!! ... already exists ...', flush=True)


def get_read_file_from_pickle(file_name_with_dir):
    if os.path.exists(file_name_with_dir):
        with open(file_name_with_dir, mode='rb') as f:
            # IPORTANT(!) : f = _io.BufferReader, not "file_name_with_dir"
            loaded_data = pickle.load(f)
        return loaded_data
    else:
        print("SORRY!! ... pickle file doesn't exists ...", flush=True)


def remove_silently(file_name_with_dir):
    try:
        os.remove(file_name_with_dir)
        print('*** FILE IS DELETED~!!! ***', flush=True)
    except OSError as e:
        """
        # errno.ENOENT = no such file or directory
        # re-raise exception if a different error occurred
        """
        if e.errno != errno.ENOENT:
            raise


def waiting_delete(file_name_with_dir, second=3):
    """ USING remove_silently, after waiting (sec) & delete file
    """
    delay = 0.2            # the interval of each counting
    for n in range(int(second / delay)):
        print('.', flush=True)
        time.sleep(delay)
    remove_silently(file_name_with_dir)


write_file_to_pickle(
    HOME_DIR + '\\_statics\\_pickle\\' +
    FILE_NAME,
    _d_dict)

try:
    _new_dict = get_read_file_from_pickle(
        HOME_DIR + '\\_statics\\_pickle\\' +
        FILE_NAME)

    for _key in _new_dict:
        # print(_key, _new_dict[_key][0])
        print("{} = '{}'".format(_new_dict[_key][0], _new_dict[_key][1]))

    version = 0
    for n in range(20):
        if os.path.exists(
            HOME_DIR + '\\_statics\\_pickle\\' +
            FILE_NAME.strip().split('.')[0] +
            '_v' + '{:0>2}.'.format(version) +
                FILE_NAME.strip().split('.')[1]):

            version += 1
        else:
            break

    write_file_to_pickle(
        HOME_DIR + '\\_statics\\_pickle\\' +
        FILE_NAME.strip().split('.')[0] +
        '_v' + '{:0>2}.'.format(version) +
        FILE_NAME.strip().split('.')[1],
        _new_dict)

    waiting_delete(HOME_DIR + '\\_statics\\_pickle\\' + FILE_NAME, 6)

except TypeError as e:
    print('(!) Message : {}'.format(e))
    print("*** PROGRAM TERMINATED ***")
