import time, os
import datetime

while True:
    a = datetime.datetime.now()

    ampm = a.strftime('%p')     # AM, PM
    hour = a.strftime('%H')     # 07
    minute = a.strftime('%M')   # 01
    second = a.strftime('%S')   # 01

    weekday = a.strftime('%A')  # MONDAY

    print(a)
    print()
    print('ampm =',type(ampm))
    print('hour =',type(hour))
    print('minute =',type(minute))
    print('second =',type(second))
    print('\n\n\n',"%s %s : %s : %s - %s" %(ampm, hour, minute, second, weekday))
    print()
    
    time.sleep(1)
    os.system('cls')
