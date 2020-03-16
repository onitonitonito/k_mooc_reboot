"""
# for Ex519a BBC webCrawling result for PyQt5 QTextBrowser
"""
print(__doc__)

import _add_syspath_root
from assets import script_run

import requests
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlencode

URL = 'http://news.donga.com/search'
KEYWORD = '날씨'
QUERIES = {
    'query' : KEYWORD,
    'check_news' : '1',
    'more' : '1',
    'sorting' : '1',         # 정확도=3, 최신순=1
    'search_date' : '1',
    'range' : '3',
}

URL_TARGET = f"{URL}?{urlencode(QUERIES)}"

def main():
    html = requests.get(URL_TARGET)
    soup = BeautifulSoup(html.text, 'html.parser')

    findings = soup.find_all('p', 'tit')

    for i, find in enumerate(findings, 1):
        date_text = find.select('span')[-1].get_text()
        date_parsed = datetime.strptime(date_text, '%Y-%m-%d %H:%M')
        when = datetime.strftime(date_parsed, '%m/%d(%a)')

        title_text = find.get_text().\
                            replace('\n', '').\
                            replace('  ','').\
                            replace(date_text, '')
        line = f"{i:02}-{when} {title_text[:32]}.."
        print(line)



if __name__ == '__main__':
    main()
