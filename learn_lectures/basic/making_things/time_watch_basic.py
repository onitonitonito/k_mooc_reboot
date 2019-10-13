"""
# Refer : DATETIME module Documentation
# - format here : https://docs.python.org/2/library/datetime.html
"""

import os
import time
import datetime
# print(__doc__)


while True:
    a = datetime.datetime.now()

    ampm = a.strftime('%p')     # AM, PM
    hour = a.strftime('%H')     # %H = 24, %I = 12 format.
    minute = a.strftime('%M')   # 01
    second = a.strftime('%S')   # 01
    weekday = a.strftime('%A')  # MONDAY

    _combined_format = a.strftime('%p %I:%M:%S - %B %d, %A')

    print('%s  --> %s' % (a, _combined_format), end='\n\n')
    print('ampm =', type(ampm))
    print('hour =', type(hour))
    print('minute =', type(minute))
    print('second =', type(second))
    print('\n\n\n', "%s %s : %s : %s - %s" %
          (ampm, hour, minute, second, weekday))
    print()

    time.sleep(1)
    os.system('cls')
