"""
# [python] 파이썬으로 주식 상장기업 크롤링? .. 이상한 진행?
# http://bit.ly/2FAGntD
"""
# 상장목록을 엑셀로 다운로드하는 URL에서
# 굳이, DF로 한번 바꿔서 엑셀로 저장하는 건 뭔가?

import pandas as pd

print(__doc__)

# 상장목록을 엑셀로 다운로드 하는 URL
URL = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'

# 어짜피, DF객체를...
code_df = pd.read_html(URL, header=0)[0]


# DF객체로 한번 더 바꿔서 엑셀로 저장한다. csv형식
df = pd.DataFrame(code_df)
df.to_csv('excel_test.csv', mode='w', encoding='EUC-KR')


# 똑같은 DF객체인데 뭐하러, 한번 더 바꾸나??
print(type(df.head()))
print(df.head())

print(type(code_df.head()))
print(code_df.head())
