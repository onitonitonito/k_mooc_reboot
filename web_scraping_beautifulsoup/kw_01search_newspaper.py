""" Keyword search in Donga-Ilbo :: Couldn't find : parser libraryError lxml
  (1) Can't performed with CMD - lxml parser libraryError, DLL errors.. etc.
  (2) Only run with Anaconda env = Ipython, Jupyter, Spyder etc..
"""
import sys
# import lxml               # can't find a tree builder : lxml. Install parser?
# from lxml import etree    # ImportError: DLL load failed:
from bs4 import BeautifulSoup
import urllib.request
from urllib import parse

TARGET_URL_BEFORE_PAGE_NUM = "http://news.donga.com/search?p="
TARGET_URL_BEFORE_KEWORD = '&query='
TARGET_URL_REST = '&check_news=1&more=1&sorting=3&search_date=1&v1=&v2=&range=3'

def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = 1 + i*15
        position = URL.index('=')       # 'int' = 1st position
        URL_with_page_num = URL[: position+1] + str(current_page_num) \
                            + URL[position+1 :]
        source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
        soup = BeautifulSoup(source_code_from_URL, 'lxml',
                            from_encoding='utf-8')
        for title in soup.find_all('p', 'tit'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)

def get_text(URL, output_file):
    source_code_from_url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_url, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.article_txt')

    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)

def main(argv):
    global output_file_name
    # if len(argv) != 4:
    #     return
    # keyword = argv[1]
    # page_num = int(argv[2])
    # output_file_name = argv[3]

    keyword = '사드'
    page_num = 2
    output_file_name = '_1_thadd_article.pdb'

    meta_string_on_top = 'KEY WORD = %s / PAGE NUMBER = %s / FILE_NAME = %s'%(
                keyword, page_num, output_file_name )+ '\n' + '^+^+^' + '\n'

    # ...com/search?p= | &query= |
    target_URL = TARGET_URL_BEFORE_PAGE_NUM \
               + TARGET_URL_BEFORE_KEWORD \
               + parse.quote(keyword) \
               + TARGET_URL_REST

    # print(type(parse.quote(keyword)))
    # print('----',parse.quote(keyword))

    output_file = open(output_file_name, 'w', encoding='utf-8')

    output_file.write(meta_string_on_top)      # write meta_string @TOP
    get_link_from_news_title(page_num, target_URL, output_file)
    output_file.close()

if __name__ == '__main__':
    main(sys.argv)
