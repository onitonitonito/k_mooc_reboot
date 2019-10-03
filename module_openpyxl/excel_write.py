"""
* 엑셀 설치없이 엑셀시트 만들기
* 임의의 시트를 활성화해서 내용을 기록하고 새로운 액셀화일을 만듬
"""
# script run 에서는 실행이 안됨.

import datetime
import openpyxl as opx
import _assets.script_run

from _assets.configs import *
from _assets.classes import *

filename_write = join_dir(
                get_dir(dir_top, dir_dict, "_results"),
                '_sample.xlsx',
                )

WB = opx.Workbook()
WS = WB.active

# Data can be assigned directly to cells
# Python types will automatically be converted
WS['A1'] = 'Python OpenPyXL module test'
WS['F1'] = datetime.datetime.now()

# Rows can also be appended
WS.append([1, 2, 3, 4, 5])
WS.append(['Hello!', 'This', 'is the', 'OpenPyXL', 'World!'])

command_list = WS['A1'].__dir__()
for content in command_list:
    if content[:1] is "_":
        pass
    else:
        print(content)

print(WS['A1'].value)       # Python OpenPyXL module TEST
print(WS['F1'].value)       # datetime.now()

# Save the file
WB.save(filename_write)
