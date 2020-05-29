"""
# 워드 클라우드 만들기 (주피터노트북 _ 파이썬) = http://bit.ly/391No2P
"""
print(__doc__)

import nltk
import matplotlib.pyplot as plt

from konlpy.tag import Twitter
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords

import assets.script_run
from assets.config import dir_ini, dir_img

# 맷플롯 한글깨짐 방지 - 폰트 = 맑은고딕
import matplotlib
from IPython.display import set_matplotlib_formats
matplotlib.rc('font', family='Malgun Gothic')
matplotlib.rc('axes', unicode_minus=False)
set_matplotlib_formats('retina')

FILENAME = "fb_comments_01refine_to_text_commentOnly.txt.ini"
RESULT = 'fb_comments_word_cloud.png'
IMG_MASK = 'fb_mask_image_black.png'

with open(dir_ini + FILENAME, mode='r', encoding='utf8') as file:
    lists = file.readlines()

twitter = Twitter()
morphs = []

# 형태소 분석
for sentence in lists:
    morphs.append(twitter.pos(sentence))



# 클라우드 대상은 명사, 형용사, 부사만 골라내기
list_noun_adj_adv = []
for sentence in morphs:
    for word,  tag in sentence:
        if tag in ['Noun'] and \
            ("것" not in word) and \
            ("내" not in word) and \
            ("나" not in word) and \
            ("수" not in word) and \
            ("게" not in word) and \
            ("말" not in word):
            list_noun_adj_adv.append(word)
# print(list_noun_adj_adv)   # FOR TEST!


# 빈도수의 반대로 정렬하기
count = Counter(list_noun_adj_adv)
words = dict(count.most_common())
# print(words)              # FOR TEST FREQUENCY of APPEARANCE

file_text = ""
for line in list_noun_adj_adv:
    file_text += line + "\n"

filename = 'fb_comments_02refile_noun_adj_adv.txt'
with open(file=filename, mode='w', encoding='utf8') as f:
    f.write(file_text)


f = open(filename, encoding='utf8').read()


# 맷플롯 한글깨짐 방지 - 폰트 = 맑은고딕
from IPython.display import set_matplotlib_formats
matplotlib.rc('font', family='Malgun Gothic')
set_matplotlib_formats('retina')
matplotlib.rc('axes', unicode_minus=False)

word_cloud_basic = WordCloud(
                            font_path="c:/Windows/Fonts/malgun.ttf",
                            background_color='white',
                            colormap='Accent_r',
                            max_words=100,
                            width=1500,
                            height=1000,
                        # ).generate_from_frequencies(words)
                        ).generate(f)

plt.figure(figsize=(8,4))
plt.imshow(word_cloud_basic)
plt.axis('off')
plt.show()







def main():
    pass

if __name__ == '__main__':
    main()
