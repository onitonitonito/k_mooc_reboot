"""
# Ex 5.19_QTextBrowser.py
http://codetorial.net/pyqt5/widget/qdatetimeedit.html
"""
# ...
#  - QCalendarWidget
#  - QSpinBox
#  - QDoubleSpinBox
#  - QDateEdit
#  - QTimeEdit
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced) *
#  - QTextEdit

print(__doc__)

import sys
import requests

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup

import _add_syspath_root
from assets.config import dir_icon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex5.19_QTextBrowser'
        self.posXY = (600, 45)
        self.windowSize = (400, 300)
        self.initUI()
        self.showBasic()

    def initUI(self):
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your search word')
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.crawl_news)

        self.lbl = QLabel('')

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lbl, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)

        self.setLayout(grid)

    def showBasic(self):
        """Basci Attribution & Geometry display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def crawl_news(self):
        search_word = self.le.text()

        if search_word:
            self.lbl.setText('BBC Search Results for "' + search_word + '"')
            self.tb.clear()
            url_search = 'https://www.bbc.co.uk/search?q='
            url = url_search + search_word
            r = requests.get(url)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            titles_html = soup.select('.search-results > li > article > div > h1 > a')

            for i in range(len(titles_html)):
                title = titles_html[i].text
                link = titles_html[i].get('href')
                self.tb.append(str(i + 1) + '. ' + title + ' (' + '<a href="' + link + '">Link</a>' + ')')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
