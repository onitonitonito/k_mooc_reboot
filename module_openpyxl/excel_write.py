"""
* 엑셀 설치없이 엑셀시트 만들기
* 임의의 시트를 활성화해서 내용을 기록하고 새로운 액셀화일을 만듬
"""
# script run 에서는 실행이 안됨.

import datetime
import openpyxl as opx
import assets.script_run

from assets.configs import dir_home_works
from assets.classes import show_commands

filename_write = dir_home_works + '_sample.xlsx'

WB = opx.Workbook()
WS = WB.active

# Data can be assigned directly to cells
# Python types will automatically be converted
WS['A1'] = 'Python OpenPyXL module test'
WS['F1'] = datetime.datetime.now()

# Rows can also be appended
WS.append([1, 2, 3, 4, 5])
WS.append(['Hello!', 'This', 'is the', 'OpenPyXL', 'World!'])


print(WS['A1'].value)       # Python OpenPyXL module TEST
print(WS['F1'].value)       # datetime.now()

# Save the file
WB.save(filename_write)


def main():
    show_commands(WS['A1'])



if __name__ == '__main__':
    main()
