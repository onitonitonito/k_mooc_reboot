"""
# Deco-Logger : Logging file is written in display_info.log file
#  - INFO:root:[2017-10-05 16:27] achieved result args
#  -('Hello World!!',), kwargs= {}
# display_info(Jung-Eun, 24) function is activated...
"""
# ------ root path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
import os, sys                                                      # 1
top = "k_mooc_reboot"                                               # 2
root = "".join(os.path.dirname(__file__).partition(top)[:2])+"\\"   # 3
sys.path.insert(0, root)                                            # 4
# ---------------------------------------------------------------------

import time
import datetime
import logging

from _assets import script_run
from _assets.config_global import dir_pickle

print(__doc__)

_time_format = '%Y-%m-%d %H:%M:%S'

def my_logger(func):
    """
    # 2차함수() 내용은 항상 맨위에 실행 됨 (공통으로 가장 먼저 반복 실행 됨)
    # 중복 데코레이터의 경우 역순으로 실행 됨 / 제일 먼저, 한꺼번에 실행 됨
    """
    filename = f"{func.__name__}.log"
    filename_with_dir = dir_pickle + filename

    logging.basicConfig(filename=filename_with_dir, level=logging.INFO)
    print(f"... 베이직 콘피그 : 초기화/준비 작업완료 ... {func.__name__}")

    def wrapper(*args, **kwargs):
        # 래퍼함수()에 있어야, 실시간 로깅이 재현 됨,
        timestamp = datetime.datetime.now().strftime(_time_format)
        # logging.info(message, *args, **kwargs)
        logging.info(f"[{timestamp}]-args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@my_logger
def show_logger_00(name, age):        # 저장할 화일명 = func.name
    time.sleep(1)
    print(f"logger_00('{name}', {age})함수가 실행되었습니다...")

@my_logger
def show_logger_01(message):
    time.sleep(2)
    print(f"logger_01('{message}')함수가 실행되었습니다...")





_="""데코레이터를 사용한 프로젝트 (로그화일 남기기 : import logging)
------------------------
 - 데코레이터는 로그를 기록한다.
 - 일반함수는 기록한 내용을 프린트 해준다.
"""
print('\n\n'+_+'\n\n\n')

# -args=('제이콥', 24), kwargs={}
show_logger_00('제이콥', 24)
show_logger_01('안녕 세상!!')
show_logger_01('잘가, 바이바이~')

# -args=(), kwargs={'name':'Kay', 'age':24}
show_logger_00(name='Kay', age=24)
show_logger_01(message='HELLO WORLD!!')
show_logger_01(message='SEE-YOU, ByeBye~')
