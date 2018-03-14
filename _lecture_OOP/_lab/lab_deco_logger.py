"""--------------------------------------- SESSION 07--PROJECT-
(1) Logging file is written in display_info.log file
 - INFO:root:[2017-10-05 16:27] achieved result args -('Hello World!!',), kwargs= {}
(2) display_info(Jung-Eun, 24) function is activated...
"""
import os
import time
import datetime
import logging

CURRENT = os.path.dirname(__file__)
DIRS = CURRENT.partition('k_mooc_reboot\\')     # ROOT_NAME
ROOT_DIR = DIRS[0] + DIRS[1]

def my_logger(func):
    # 2차함수() 내용은 항상 맨위에 실행 됨 (공통으로 가장 먼저 반복 실행 됨)
    # 중복 데코레이터의 경우 역순으로 실행 됨 / 제일 먼저, 한꺼번에 실행 됨
    filename_with_dir = os.path.join(
        ROOT_DIR, '_static', '_pickle', '%s.log'% func.__name__)

    logging.basicConfig(            # filename=display_info.log, level=INFO
        filename= filename_with_dir,
        level=logging.INFO)
    print("... 베이직 콘피그 : 초기화 / 준비 작업완료 ... %s"% func.__name__)

    def wrapper(*args, **kwargs):
        # 래퍼함수()에 있어야, 실시간 로깅이 재현 됨,
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # logging.info(message, *args, **kwargs)
        logging.info('[{}]-args={}, kwargs={}'.format(
                timestamp,
                args,
                kwargs))
        return func(*args, **kwargs)
    return wrapper

@my_logger
def show_logger_00(name, age):        # 저장할 화일명 = func.name
    time.sleep(1)
    print("logger_00('{}', {})함수가 실행되었습니다...".format(name, age))

@my_logger
def show_logger_01(message):
    time.sleep(2)
    print("logger_01('{}')항수가 실행되었습니다...".format(message))





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
