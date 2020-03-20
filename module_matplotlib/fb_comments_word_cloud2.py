"""
# WORD CLOUD from fb_comments_01refined_to_text_commentOnly
"""
print(__doc__)

from wordcloud import WordCloud

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from wordcloud import STOPWORDS

import assets.script_run
from assets.config import dir_ini, dir_img

filename = "fb_comments_02refile_noun_adj_adv.txt"
result = 'fb_comments_word_cloud_{}.png'
img_mask = 'fb_mask_image_black.png'

mask_array = np.array(Image.open(dir_img + img_mask))
f = open(dir_ini + filename, encoding='utf8').read()

def main(f):
    word_cloud_basic = get_wordcloud_basic(f)
    word_cloud_masked = get_wordcloud_masked(f)

    show_wc(word_cloud_basic, (15, 10))
    save_wc_image(word_cloud_basic, dir_img + result.format("01_basic"))

    show_wc(word_cloud_masked, (10, 8))
    save_wc_image(word_cloud_masked, dir_img + result.format("02_masked"))


def show_wc(image_array, figsize):
    """show wordcloud obj. or img_array using imshow()"""
    plt.figure(figsize=figsize)
    plt.imshow(image_array, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def get_wordcloud_basic(f):
    """
    # If you lower the maximum font size, you will get more words
    # wc = WordCloud(max_font_size=30).generate(f) .... Line.10
    """
    stopwords = set(STOPWORDS)
    wc = WordCloud(
                    background_color="white",
                    font_path="c:/Windows/Fonts/malgun.ttf",
                    max_words=1000,
                    width=1500,
                    height=1000,
                    stopwords=stopwords,
                ).generate(f)
    wc.words_
    return wc

def get_wordcloud_masked(f):
    """ MASKED WORD CLOUD
    Original Author's Page refer to HERE :
    https://amueller.github.io/word_cloud/auto_examples/masked.html
    """
    # read the mask image taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    stopwords = set(STOPWORDS)
    wc = WordCloud(
                    background_color="white",
                    font_path="c:/Windows/Fonts/malgun.ttf",
                    max_words=1000,
                    width=1500,
                    height=1000,
                    stopwords=stopwords,
                    mask=mask_array,
                ).generate(f)
    return wc

def save_wc_image(wordcloud_object, filename_with_dir):
    wordcloud_object.to_file(filename_with_dir)







if __name__ == '__main__':
    main(f)
