"""
# Ex 3.09 display date & time
http://codetorial.net/pyqt5/basics/datetime.html
"""
# 날짜와 시간 표시하기
# QtCore 모듈의 QDate, QTime, QDateTime 클래스를 이용해서 어플리케이션에 날짜와
# 시간을 표시할 수 있습니다.각 클래스에 대한 자세한 설명은 아래 링크를 참고합니다.
#   - QDate 공식 문서
#   - QTime 공식 문서
#   - QDateTime 공식 문서

print(__doc__)

import sys
import _add_syspath_root

from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt)


def main():
    a = TestAll(quit=False)

    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

class TestAll():
    from PyQt5.QtCore import (
                        QDateTime,
                        QDate,
                        QTime,
                        Qt,
                    )

    def __init__(self, quit=True):
        self.quit = quit
        self.now = self.QDate.currentDate()
        self.timeNow = self.QTime.currentTime()
        self.dateTime = self.QDateTime.currentDateTime()
        self.run_test_all_and_quit()

    def run_test_all_and_quit(self):
        func_names = [func for func in vars(TestAll)
                        if func.startswith("test_")]

        for i, func_name in enumerate(func_names, 1):
            func = getattr(TestAll, func_name)

            print('\n\n{:_^50}'.format(f" {i:02}.{func.__doc__} "))
            func(self)

        if self.quit:
            quit()

    def test_01(self):
        """TEST QtPy current date now """
        print(self.now.toString())
        print()

    def test_02(self):
        """TEST QtPy date format """
        print(self.now.toString('d.M.yy'))                   # 10.3.20
        print(self.now.toString('dd.MM.yyyy'))               # 10.03.2020
        print(self.now.toString('ddd.MMMM.yyyy'))            # 화.3월.2020

        print(self.now.toString(self.Qt.ISODate))                 # 2020-03-10
        print(self.now.toString(self.Qt.DefaultLocaleLongDate))   # 2020년 3월 10일 화요일
        pass

    def test_03(self):
        """TEST QtPy current time """
        print(self.timeNow.toString())

    def test_04(self):
        """TEST QtPy time format"""
        print(self.timeNow.toString('h.m.s'))
        print(self.timeNow.toString('hh.mm.ss.'))
        print(self.timeNow.toString('hh.mm.ss.zzz'))
        print(self.timeNow.toString(self.Qt.DefaultLocaleLongDate))
        print(self.timeNow.toString(self.Qt.DefaultLocaleShortDate))

    def test_05(self):
        """TEST QtPy Date & Time together!"""
        print(self.dateTime.toString())              # 화 3 10 13:21:25 2020

    def test_06(self):
        """TEST QtPy Date & Time with format"""
        print(self.dateTime.toString('d.M.yy hh:mm:ss'))
        print(self.dateTime.toString('dd.MM.yyyy, hh:mm:ss'))
        print(self.dateTime.toString(self.Qt.DefaultLocaleLongDate))
        print(self.dateTime.toString(self.Qt.DefaultLocaleShortDate))

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.time = QTime.currentTime()
        # self.dateTime = QDateTime.currentDateTime()

        self.title = 'Ex3.09-Show Date in statusBar!'
        self.posXY = (300, 300)
        self.windowSize = (400, 200)

        string_format = Qt.DefaultLocaleLongDate
        # self.message = QDate.currentDate().toString(string_format)
        # self.message = QTime.currentTime().toString(string_format)
        self.message = QDateTime.currentDateTime().toString(string_format)

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.message)
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()





if __name__ == '__main__':
    main()
