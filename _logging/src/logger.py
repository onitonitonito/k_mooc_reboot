"""
# logging example -
#
"""


import os
from datetime import datetime

print(__doc__)

class Logger(object):
    def __init__(self, filename):
        # self._format = '%m/%d %H:%M:%S.%f'
        self._format = '%Y %m/%d %H:%M:%S.%f'
        self._filename = filename
        self._time_now = datetime.now().strftime(self._format)

    def _timestamp(self):
        return f"{self._time_now}"

    def _log(self, *args):
        """메시지를 지정 로그화일에 기록(append)하고, echo 시킴"""
        message = f"* {self._timestamp()} - {' '.join(args)}"
        open(self._filename, 'a', encoding='utf8').write(message.strip()+"\n")
        print(message)       # 화면에 표시

    def info(self, *args):
        self._log('[INFO]', *args)

    def warning(self, *args):
        self._log('[WARNING]', *args)

    def error(self, *args):
        self._log('[ERROR]', *args)



if __name__ == '__main__':
    # ------ root path 를 sys.path.insert 시키는 코드 ... 최소 4줄 필요------
    import os, sys                                                      # 1
    top = "_logging"                                                    # 2
    root = "".join(os.path.dirname(__file__).partition(top)[:2])+"\\"   # 3
    sys.path.insert(0, root)                                            # 4
    # ---------------------------------------------------------------------

    import assets.script_run

    log = Logger(root + "log/test.log")
    # print(log._timestamp())
    log._log('logger.py에서 테스트하는 기록입니다...')
    log.info('logger.py에서 테스트하는 기록입니다...')
    log.error('logger.py에서 테스트하는 기록입니다...')
