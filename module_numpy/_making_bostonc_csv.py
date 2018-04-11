import os
import sys
import csv

import numpy as np
import pandas as pd

# '루트'와 '작업'디렉토리 설정 - for 스크립트런
DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1]
sys.path.append(ROOT)

CSV_DIR = os.path.join(ROOT, "_static", "")
WORK_DIR = os.path.join(ROOT, "_static", "_made_static", "")
print("워킹디렉토리 = %s \n"% WORK_DIR)

# 스크립트런 '한글' 표시를 위한 커스텀 모듈 실행
import _script_run_utf8
_script_run_utf8.main()




# 워킹 디렉토리가 없을 경우, 워킹 디렉토리를 만든다.
if not os.path.isdir(WORK_DIR):
    os.mkdir(WORK_DIR)
    print("... 워킹 디렉토리(%s)를 만들었습니다."% WORK_DIR)


# boston.csv 화일에서 읽어서 data 리스트 화일에 담는다.
with open(CSV_DIR + "bostonc.csv", mode='r') as f:
        data = f.readlines()


# print(len(data))        # 자료의 갯수 = 518개 / 1~10까지는 자료설명
descript = ""
for n in range(10):
    one_line = data[n].split(",")[1]
    one_line = one_line.replace("\"", "")    #
    descript += one_line
print(descript)


# 자료 2+1줄을 뽑아낸다

columns = data[10].split(",")[1].replace("\"", "").split()
df = pd.DataFrame(columns=columns)

for n in range(518-11-1):                      # 518개 - 10개 만큼 반복한다.
    one_line = data[11+n].split(",")[1]      # 앞 번호를 빼고, 뒷 자료만 이용한다
    one_line = one_line.replace("\"", "")    # 데이터안의 '"'를 제거한다.
    one_line_list = one_line.strip().split() # 21개 맴버의 리스트로 분리.
    feed_dict = {
        col : val for col, val in zip(columns, one_line_list)}
    df = df.append(feed_dict, ignore_index=True)

print(df.shape)
# print(df[1])
# print(df[2])


# http://pythonstudy.xyz/python/article/207-CSV-파일-사용하기
# 자료 리스트를 한줄 한줄 저장할 경우, import csv
# 판다스 df 를 한꺼번에 csv 화일로 저장할 경우, 아래 참조
# 판다스 DataFrame을 csv로 저장하고 로드하기 = http://buttercoconut.xyz/74

df.to_csv(WORK_DIR+"bostonc_new.csv")
