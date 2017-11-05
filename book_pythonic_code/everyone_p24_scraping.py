# # THIS IS FOR test1_searching_speed
# big_list = [str(n) for n in range(10**7)]
# big_set = set(big_list) # [Finished in 10.182s]

def test1_check_speed():
    """ set is faster than list, see what happen """
    # _a = "abc" in big_list
    # print(_a)           # False [Finished in 12.721s]

    _b = "abc" in big_set
    print(_b)           # False [Finished in 12.222s]
# test1_check_speed()

def test2_how_to_dict():
    """ easy way to make 'dict' type data using enumerate(), zip() """
    v_seq = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', ]
    k_seq = 'abcdefghi'

    _dict_zip = dict(zip(k_seq, v_seq,))    # key, value_sequance
    print(_dict_zip)

    _dict_enu = dict(enumerate(v_seq))      # automatically indexed i_seq
    print(_dict_enu)
# test2_how_to_dict()

def test3_cnt_appear():
    """ using collections, count number of appear in array """
    from collections import Counter

    phrase = 'a man a plan a canal panama jumping rope'
    cntr = Counter(phrase.split())
    _a_arr = cntr.most_common()
    print(type(_a_arr))
    print(_a_arr)
    print(dict(_a_arr))
    print('a=', dict(_a_arr)['a'])
# test3_cnt_appear()


import os
from urllib.request import urlopen

DESTIN_DIR = os.path.join(os.path.dirname(__file__), 'pdb_temp', '')

URL_arr = [
        ('http://www.naver.com','naver_1home.pdb', 'utf8'),
        ('http://cafe.naver.com','naver_2cafe.pdb', 'utf8'),
        ('https://section.blog.naver.com/BlogHome.nhn','naver_3blog.pdb','utf8'),
        ('http://kin.naver.com', 'naver_4know.pdb', 'utf8'),
        ('http://shopping.naver.com', 'naver_5shopping.pdb', 'utf8'),
        ('http://movie.naver.com', 'naver_6movie.pdb', 'utf8'),
        ('http://finance.naver.com','naver_7finance.pdb', 'cp949'),
        ('http://www.networksciencelab.com', 'sciencelab_home.pdb', 'utf8'),
        ]

def write_URL_to_file(URL, DESTIN_DIR, FILE_NAME, CODEC):
    # read contents from URL
    with urlopen(URL) as doc:
        html = doc.read().decode(CODEC)

    # write to file(.pdb)
    with open(file=DESTIN_DIR + FILE_NAME, mode='w', encoding='UTF-8') as f:
        f.write(html)

# URL='http://www.naver.com'
# FILE_NAME = 'naver_home.pdb'
# CODEC = 'utf-8'
# write_URL_to_file(URL, DESTIN_DIR, FILE_NAME, CODEC)

for i, URL in enumerate(URL_arr):
    # print(i,'=',URL) /  print(URL[0],'------>',URL[1])
    write_URL_to_file(URL[0], DESTIN_DIR, URL[1], URL[2])
