"""
# tk_post_query=https://www.facebook.com/groups/TensorFlowKR/
# permalink/1143451979329192/
"""
import assets.script_run
from assets.config import dir_ini
from pyprnt import prnt


# MAKE ARRAY
with open(file=dir_ini + 'fb_comments.ini', mode='r', encoding='utf8') as f:
    fb_comments = [item.strip()
                            for item in f.read().split('\n')
                            if item is not '']

# print(fb_comments.count(''))  # 0

array_temp = []
comments_2d = []
count = 0
splitter = '좋아요'            # splitter = 'likes'

for item in fb_comments:
    if splitter in item:
        array_temp.append(item)
        comments_2d.append(array_temp)

        if count > 2:
            print(f"COUNT = {count} --> ", end="")
            array_wrong = comments_2d[-1]

            # REMOVE DUPLICATE from ARRAY
            array_correct = list(dict.fromkeys(array_wrong))

            # MERGE MIDDLE ARRAY
            array_correct[1 : -1] = [''.join(array_correct[1 : -1])]
            print(f"{len(array_correct)-1}")

            [print(item) for item in array_correct]
            print()

            comments_2d.pop()
            comments_2d.append(array_correct)

        array_temp = []
        count = 0

    else:
        count += 1
        array_temp.append(item)

# [print(comment) for comment in comments_2d]         # FOR TEST!

comment_dic = {}
temp_dic = {}
for idx, comment in enumerate(comments_2d):
    temp_dic['name'] = comment[0]
    temp_dic['comment'] = comment[1].replace(comment[0], '')
    temp_dic['likes'] = comment[2]
    comment_dic[idx] = temp_dic
    temp_dic = {}


def check_last_column_likes():
    # 첫번째 = name / 마지막=likes, but comment[2]가 likes 가 아닐수도 있음.
    # WRONG_ARRAY -> CORRECT, & CHECK DICT['LIKES']
    for i in range(len(comment_dic)):
        print(comment_dic[i]['likes'])


check_last_column_likes()
