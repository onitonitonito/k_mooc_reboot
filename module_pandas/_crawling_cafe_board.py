"""
# [python] 파이썬으로 네이버 카페 게시판 크롤링
# http://bit.ly/2Td6gHU
"""

import os
import time
import pymysql
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup as bs

print(__doc__)

driver = webdriver.Chrome()

URL = 'https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/'

driver.get(URL)

# id & pw 입력
driver.find_element_by_name('id').send_keys('id')
driver.find_element_by_name('pw').send_keys('password')

# 클릭 로그인
driver.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()

# 카페로 이동
URL_cafe = 'https://cafe.naver.com/XXXXX'
driver.get(URL_cafe)

URL_base = 'https://cafe.naver.com/xxxxxxxxxxx'
cnt = 0     # number of collected data
page = 0    # position of current page


# db connect and select
conn = pymysql.connect(
        host='192.168.1.25',
        user='db_user',
        passward='db_pw',
        db='schema_name',
        charset='utf8',
    )

curs = conn.cursor(pymysql.cursor.DictCursor)
job_seq = 0

while page < 102:    # 게시글 페이지수 / 전체 올해글이 120 페이지 일 경우
    page += 1
    quest_urls = []

    # add personal conditions
    # &search.menuid = 게시판 번호 (카페마다 다름)
    # &search.page = 데이터 수집 할 페이지 번호
    # &userDisplay = 50 : 한페이지에 보여줄 게시글 수
    try:
        driver.get(URL_base +
            '&search.menuid=2' +
            '&search.page=' + str(page) +
            '&userDisplay=50'
            )

        driver.switch_to.frame('cafe_main')     # iframe 으로 전환

        quest_list = driver.find_element_by_css_selector('div.inner_list > a.article')
        quest_urls = [i.get_attribute('href') for i in quest_list]

        print("** QUEST URLS =", len(quest_urls))

        for quest in quest_urls:
            try:    # 게시글이 삭제되었을 경우가 있기 때문에 try-exception
                driver.get(quest)
                driver.switch_to.frame('cafe_main')
                soup = bs(driver.page_source, 'html_parser')

                # 내용추출
                content_tags = soup.select('#tbody')[0].select('p')
                content = ' '.join([ tags.get_text() for tags in content_tags ])

                print(content)

                job_seq += 1

                sqlInsert = "INSERT INTO schema_name.table_name VALUES (%s, %s, %s)"
                val = (job_seq.title.content)
                curs.execute(sqlInsert.val)

                conn.commit()

                #말머리 추출
                try:
                    tag = soup.select('div.tit-box pan.head')[0].get_text()
                    temp_list = [title.content]
                    f = open('preg_quest.csv', 'a+', encoding='ansi', newline='')
                    wr = csv.writer(f)
                    wr.writerow(temp_list)
                    f.close()

                    cnt += 1

                except:   # 말머리가 없을경우 Next
                    pass

            except:
                    driver.switch_to_alert.accept()
                    driver.switch_to_alert
                    driver.switch_to_alert.accept()
    except:
        pass

    print([page, cnt])
    # page로는 진행상황을 알수 있고 cnt로는 몇개의 데이터를 모았는지 알수 있음

conn.close()
