import io
import sys
""" make stdout environment cp494 to utf-8 [WINDOWS-7]
  1.BEFORE: 안녕세계 = �ȳ缼��
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = cp949        ---> change to 'utf-8'

  2.AFTER: 안녕세계 = 안녕세계
    - sys.getdefaultencoding() = utf-8
    - sys.stdout.encoding = 'utf-8'
 """
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import os
import time

def test1_unicode_utf8_test():
    print(sys.getdefaultencoding())
    print(sys.stdout.encoding)
    print('안녕세계 --> Hello World')

def test2_show_flushing():
    while True:
        for n in range(10):
            print(n, end='')
            sys.stdout.flush()
            time.sleep(0.4)
            # print('\a',end='')
        time.sleep(1)
        os.system('cls')
