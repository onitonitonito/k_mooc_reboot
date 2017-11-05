""" -------- LESSON.01 -- Book KUJIRA :: Machine learning.
"""
import urllib.request as req

def simple_text_scraping():
    # READOUT DATA
    URL = 'http://api.aoikujira.com/ip/ini'
    RES = req.urlopen(url=URL)
    DATA = RES.read()

    # SHOW DATA Decoded
    TEXT = DATA.decode('UTF-8')
    print('\n(1) DATA = ', DATA)      # byte type 'str'
    print('\n(2) TEXT = ', TEXT)      # decoded 'str' with 'CODEC=UTF-8'
# simple_text_scraping()

""" -------- LESSON.01 -- Naver finance USD to KRW
"""
import os, time
from bs4 import BeautifulSoup

def get_USD2KRW_in_naver():
    # To bring HTML
    URL = 'http://info.finance.naver.com/marketindex/'
    RES = req.urlopen(URL)
    RELOAD = 0
    #
    SOUP = BeautifulSoup(RES, 'html.parser')

    while True:
        #
        krw = SOUP.select_one('div.head_info > span.value').string    # 1,133.80
        differ = SOUP.select_one('div.head_info > span.change').string  # 1.20
        change = SOUP.select_one('div.head_info > span.blind').string   # down

        flt_krw = float(krw.replace(',',''))
        flt_differ = float(differ)

        RELOAD += 1
        print('\tRELOAD : %s times'%RELOAD)
        print('__'*40)
        print('\tUSD/KRW    =  %5.2f '%flt_krw)
        print('\tDifference = %5.2f'%flt_differ)
        print('\tChanges    = ', change.encode().decode('CP949'))
        # b'\xc3\x87\xc3\x8f\xc2\xb6\xc3\xb4'
        time.sleep(10)
        os.system('cls')

    """ change.encode().encode('CP949')
    USD/KRW =  1,133.20
    Difference =   1.80
    Changes =  ÇÏ¶ô             # .decode('CP949').decode('UTF-8') in script_run
    """
get_USD2KRW_in_naver()
