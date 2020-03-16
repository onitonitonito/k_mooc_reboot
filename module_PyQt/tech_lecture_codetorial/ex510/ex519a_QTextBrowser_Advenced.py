"""
# Ex 5.19_QTextBrowser.py - Keyword News Search by Scrapping
http://codetorial.net/pyqt5/widget/qdatetimeedit.html
"""
# ...
#  - QDateTimeEdit
#  - QTextBrowser
#  - QTextBrowser (Advanced) *
#  - QTextEdit

print(__doc__)

import sys
import requests

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlencode

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

import _add_syspath_root
from assets.config import dir_icon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = dir_icon + 'icon_qt.png'
        self.title = 'Ex5.19_QTextBrowser'
        self.posXY = (0, 45)
        self.windowSize = (650, 380)
        self.initUI()
        self.showBasic()

    def initUI(self):
        # SET LINE EDIT
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your search word')
        self.le.returnPressed.connect(self.crawl_news)

        # SET PUSH-BUTTON
        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.crawl_news)

        # SET LABEL
        self.lb1 = QLabel('DONGA-ILBO KEYWORD NEWS SEARCH :')
        self.lb2 = QLabel('')

        # SET TEXT BROWSER
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        # SET GRID LAY-OUT
        grid = QGridLayout()

        # SELECT POSITION    *POS_R/C *SIZE_R/C
        grid.addWidget(self.lb1, 0, 0, 1, 4)
        grid.addWidget(self.le , 1, 0, 1, 3)
        grid.addWidget(self.btn, 1, 3, 1, 1)
        grid.addWidget(self.lb2, 2, 0, 1, 4)
        grid.addWidget(self.tb , 3, 0, 1, 4)

        # SET INTO LAY-OUT
        self.setLayout(grid)

    def showBasic(self):
        """Basci Attribution & Geometry display"""
        self.setWindowIcon(QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(*self.posXY, *self.windowSize)
        self.show()

    def crawl_news(self):
        URL = 'http://news.donga.com/search'
        KEYWORD = self.le.text()
        QUERIES = {
            'query'         : KEYWORD,
            'check_news'    : '1',
            'more'          : '1',
            'sorting'       : '1',      # ACCURACY=3, NEWEST=1
            'search_date'   : '1',
            'range'         : '3',
        }
        URL_TARGET = f"{URL}?{urlencode(QUERIES)}"

        if KEYWORD:
            self.lb2.setText(
                f"'DONGA-ILBO KEYWORD NEWS SEARCH RESULTS for '{KEYWORD}'")
            self.tb.clear()

            html = requests.get(URL_TARGET)
            soup = BeautifulSoup(html.text, 'html.parser')

            findings = soup.find_all('p', 'tit')

            for i, find in enumerate(findings, 1):
                date_text = find.select('span')[-1].get_text()
                date_parsed = datetime.strptime(date_text, '%Y-%m-%d %H:%M')
                when = datetime.strftime(date_parsed, '%m/%d(%a)')

                title_text = find.get_text().\
                                    replace('\n', '').\
                                    replace('  ','').\
                                    replace(date_text, '')
                link = find.select('a')[0]['href']
                line = f"{i:02}-{when} <a href='{link}'>{title_text}</a>"

                self.tb.append(line)
        self.le.clear()
        self.le.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
