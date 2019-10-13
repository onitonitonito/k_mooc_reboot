import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """

import os
import time

def test1_unicode_utf8_test():
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
    print('안녕세계 --> Hello World')

def test2_show_flushing():
    count = 0
    while count < 3:
        count += 1
        for n in range(10):
            print(n, end='')
            sys.stdout.flush()
            time.sleep(0.4)
            # print('\a',end='')
        time.sleep(1)
        os.system('cls')

def test3_very_confused():
    byt_ = b'abcd'
    print(type(byt_))           # <class 'bytes'>
    print(byt_[0] == 'a')       # False : NEVER!
    print(byt_[0] == 97)        # True : 0x61
    print(byt_[0] == 0x61)      # True

    print(b'\x61')              # b'a' : b'\x61'
    print(b'a')                 # b'a' : b'a'
    print(byt_[0])              # 97   : byt_[0]

    print(byt_[0] == b'\x61')   # True : \x61


test1_unicode_utf8_test()
test2_show_flushing()
test3_very_confused()