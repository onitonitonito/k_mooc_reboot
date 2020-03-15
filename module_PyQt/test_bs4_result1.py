"""
# for Ex519a BBC webCrawling result for PyQt5 QTextBrowser
"""
print(__doc__)

import requests

from assets import script_run
from bs4 import BeautifulSoup
from urllib.parse import urlencode

URL_TARGET = 'https://search.naver.com/search.naver?query='
KEYWORD = '날씨'

def main():
    print(f"NAVER Search Results for ULTRA FINE DUST in '{KEYWORD}' ")
    url = URL_TARGET + KEYWORD

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    locations = soup.find('span', {'class': 'btn_select'}).findAll('em')
    data = soup.find('div', {'class': 'detail_box'}).findAll('dd')


    location = locations[0].text
    chemicals = [dat.find('span', {'class':'num'}).text for dat in data]
    echo_messages = [
                    f" WEB CRAWLING : NAVER WEATHER",
                    f"-------------------------------",
                    f" {location}",
                    f"-------------------------------",
                    f"  (1) PM 10   =  {chemicals[0]}",
                    f"  (2) PM 2.5  =  {chemicals[1]}",
                    f"  (3) O3 (Oz) =  {chemicals[2]}",
                    f"-------------------------------",
                ]

    [print(line) for line in echo_messages]



if __name__ == '__main__':
    main()
