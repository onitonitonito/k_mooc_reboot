"""
# 로깅화일 샘플 테스트
#
"""
import assets.script_run            # 스크립트-런 한글출력

from assets.config_log import dir_root, dir_log
from src.logger import Logger

print(__doc__)


def main():
    log = Logger(dir_log + "test.log")
    print(log._timestamp())
    log._log('일반적인 설명문장을 로그에 기록 합니다.')

    log.info('정보에 관한 로그문장을 로그에 기록 합니다.')
    log.error('에러발생시 에러메시지를 로그에 기록 합니다.')
    log.warning('경고 발생시 메시지를 로그에 기록 합니다.')



if __name__ == '__main__':
    main()
