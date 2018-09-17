"""
* 엑셀 설치없이 엑셀시트 만들기
* 임의의 시트를 활성화해서 내용을 기록하고 새로운 액셀화일을 만듬
"""
# script run 에서는 실행이 안됨.

import datetime
import openpyxl as opx

wb = opx.Workbook()

# sheet = wb["Sheet1"]      # or
# grab the active worksheet
sheet = wb.active

# Data can be assigned directly to cells
# Python types will automatically be converted
sheet['A1'] = 'Python OpenPyXL module test'
sheet['F1'] = datetime.datetime.now()

# Rows can also be appended
sheet.append([1, 2, 3, 4, 5])
sheet.append(['Hello!', 'This', 'is the', 'OpenPyXL', 'World!'])

command_list = sheet['A1'].__dir__()
for content in command_list:
    if content[:1] is "_":
        pass
    else:
        print(content)

print(sheet['A1'].value)       # Python OpenPyXL module TEST
print(sheet['F1'].value)       # datetime.now()

# Save the file
wb.save("./_static/_sample.xlsx")
