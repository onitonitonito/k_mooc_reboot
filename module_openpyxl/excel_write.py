
import os
import datetime
from openpyxl import Workbook

# WORKING DIR. SET
DIRS = os.path.dirname(__file__).partition("k_mooc_reboot")
ROOT = DIRS[0] + DIRS[1] + '\\'

wb = Workbook()

# grab the active worksheet
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 'Python OpenPyXL module TEST'

# Python types will automatically be converted
ws['B1'] = datetime.datetime.now()

# Rows can also be appended
ws.append([1, 2, 3, 4, 5])
ws.append(['Hello!', 'This','is the','OpenPyXL','World!'])


for content in ws['A1'].__dir__():
    print(content)

print(ws['A1'].value)       # Python OpenPyXL module TEST
print(ws['B1'].value)       # datetime.now()

# Save the file
wb.save(ROOT + "_static/_sample.xlsx")
