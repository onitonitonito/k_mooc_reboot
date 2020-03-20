"""
# tk_post_query=https://www.facebook.com/groups/TensorFlowKR/
# permalink/1143451979329192/
"""
import json

import assets.script_run
from assets.config import dir_ini

# MAKE ARRAY
filename = 'fb_comments_00raw_20200318.ini'
with open(file=dir_ini + filename, mode='r', encoding='utf8') as f:
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

# [print(comment) for comment in comments_2d]                # FOR TEST! - array
name_array = list(set([array[0] for array in comments_2d]))  # REMOVE DUPLICATE

# REMOVE NAME FROM COMMENT for REPLAYING!
count = 0
for name in name_array:
    for comment in comments_2d:
        if name in comment[1]:
            count += 1
            comment[1] = comment[1].replace(name, '')

print(f"*** TOTLA REMOVE '{count}' NAMES IN COMMENTS for REPLAYING! ***")

# MAEK COMMENT_DICT WITH INDEX
comment_dic = {}
temp_dic = {}
for i, comment in enumerate(comments_2d):
    temp_dic['name'] = comment[0]
    temp_dic['comment'] = comment[1].replace(comment[0], '').strip()
    temp_dic['likes'] = comment[2]
    comment_dic[i] = temp_dic
    temp_dic = {}


def check_llkes_shortened_result():          # FOR TEST!
    # 첫번째 = name / 마지막=likes, but comment[2]가 likes 가 아닐수도 있음.
    # WRONG_ARRAY -> CORRECT, & CHECK DICT['LIKES']
    for i in range(len(comment_dic)):
        print(
                f"[{i:03}] ",
                f"{comment_dic[i]['likes']:6}",
                f"{comment_dic[i]['comment']:30.30}...",
            )

# check_llkes_shortened_result()


# [blog] json.dumps() 한글 유니코드로 저장되는 현상해결 http://bit.ly/2xazD4x
filename = 'fb_comments_01refine_20200318.json'
with open(file=dir_ini + filename, mode='w', encoding='utf8') as f:
    file = json.dumps(comment_dic, ensure_ascii=False)
    f.write(file)

filename = 'fb_comments_01refine_to_text_commentOnly.txt'
with open(file=dir_ini + filename, mode='w', encoding='utf8') as f:
    coments_array = [ f.writelines(array[1]+"\n") for array in comments_2d]
