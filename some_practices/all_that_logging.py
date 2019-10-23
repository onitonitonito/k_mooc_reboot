"""
# 파이썬 로깅의 모든것 - [하마] 이승현 (wowlsh93@gmail.com) 2017.08/07 11:09
# 출처: https://hamait.tistory.com/880 [HAMA 블로그]
"""
# ------ root path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
import os, sys                                                      # 1
top = "k_mooc_reboot"                                               # 2
root = "".join(os.path.dirname(__file__).partition(top)[:2])+"\\"   # 3
sys.path.insert(0, root)                                            # 4
# ---------------------------------------------------------------------
# 파이썬 로깅의 기본 설정은 WARNING 입니다.
# DEBUG < INFO < WARNING < ERROR < CRITICAL

import os
import json
import logging
import logging.config

from _assets import script_run      # 한글출력 utf-8
from _assets.config_global import dir_logging

print(__doc__)

filename_log = dir_logging + "log\\my.log"
filename_json = dir_logging + "log\\logging.json"

# 2019-11-08 12:55:27,488-my-INFO-hello world!
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

def main():
    run_01()
    # run_02()
    pass

def run_01():
    """간단한 로깅의 BASIC!"""
    # Call Object & setLevel()
    my_logger = logging.getLogger(name="my")
    my_logger.setLevel(logging.INFO)

    # StramHandler() :
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    my_logger.addHandler(stream_hander)

    # FileHandler() :
    file_handler = logging.FileHandler(filename_log)
    my_logger.addHandler(file_handler)

    # logging
    my_logger.info("hello world!")

def run_02():
    """logging_json 화일의 설정을 읽어온다."""
    with open(filename_json, 'rt') as f:
        config_json = json.load(f)

    logging.config.dictConfig(config_json)

    logger = logging.getLogger()
    logger.info("run_02() test!!!")



if __name__ == '__main__':
    main()
