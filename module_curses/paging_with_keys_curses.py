# Python Curses Scropp Example - by mingramer
# 파이썬 curses에서 스크롤 및 페이징 기능 구현하기
# https://mingrammer.com/how-to-implement-the-scroll-and-paging-in-python-curses/
# 소스코드 및 실행 방법은 Python Curses Scroll Example을 참고
# ==============================================================================

import curses
import curses.textpad       # getch()을 위해서 필요.


class Screen(object):
    UP = -1
    DOWN = 1

    def __init__(self, items):
        self.items = items
        self.window = None
        self.width = 0
        self.height = 0
        self.init_curses()
        self.max_lines = curses.LINES
        self.top = 0
        self.bottom = len(self.items)
        self.current = 0
        self.page = self.bottom // self.max_lines
        self.run()

    def init_curses(self):
        """Setup the curses"""
        self.window = curses.initscr()
        self.window.keypad(True)

        curses.noecho()
        curses.cbreak()

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.current = curses.color_pair(2)
        self.height, self.width = self.window.getmaxyx()

    def run(self):
        """인터럽트 전까지 TUI(Text User Interface) 유지한다 """
        try:
            self.get_key_callback()
        except KeyboardInterrupt:
            pass
        finally:
            curses.endwin()

    def get_key_callback(self):
        """ 채널(값)을 받아, 키에 맞는 매서드를 수행(curses.textpad 필요) """
        while True:
            self.display()
            ch = self.window.getch()
            if ch == curses.KEY_UP:
                self.scroll(self.UP)
            elif ch == curses.KEY_DOWN:
                self.scroll(self.DOWN)
            elif ch == curses.KEY_PPAGE:
                self.paging(self.UP)
            elif ch == curses.KEY_NPAGE:
                self.paging(self.DOWN)
            elif ch == curses.ascii.ESC:
                break

    def scroll(self, direction):
        """ 페이지 업(-1)/다운(+1) 키로 페이징을 수행 """
        # 방향에 따른 다음 라인 커서 위치 계산
        # direction UP= -1 / DOWN = +1
        next_line = self.current + direction

        """ 윈도우 스크롤 업 """
        # 현재 커서가 윈도우의 상단에 위치하나, 윈도우의 상단 라인이 최상단에 닿지
        # 않았으므로 윈도우 스크롤 업이 가능하다
        if (direction == self.UP) and (self.top > 0 and self.current == 0):
            self.top += direction
            return

        """ 윈도우 스크롤 다운 """
        # 다음 커서가 현재 윈도우의 하단에 위치하나, 커서의 절대 위치가 아직 최하단
        # 까지 도달하진 않았으므로 윈도우 스크롤 다운이 가능하다
        if (direction == self.DOWN) and (next_line == self.max_lines) and \
            (self.top + self.max_lines < self.bottom):
            self.top += direction
            return

        """ 스크롤 업 """
        # 현재 커서가 최상단보다 아래에 있으므로 스크롤 업이 가능하다
        if (direction == self.UP) and (self.top > 0 or self.current > 0):
            self.current = next_line
            return

        """ 스크롤 다운 """
        # 다음 커서가 현재 윈도우의 하단보다 위에 있으며, 커서의 절대 위치가 아직
        # 최하단까지 도달하진 않았으므로 스크롤 다운이 가능하다
        if (direction == self.DOWN) and (next_line < self.max_lines) and \
            (self.top + next_line < self.bottom):
            self.current = next_line

    def paging(self, direction):
        """페이징 윈도우는 PGUN/PGDN 키 이용, direction, UP/DN=-/+1"""
        current_page = (self.top + self.current) // self.max_lines
        next_page = current_page + direction

        # The last page may have fewer items than max lines,
        # so we should adjust the current cursor position as maximum item count on last page
        if next_page == self.page:
            self.current = min(self.current, self.bottom % self.max_lines - 1)

        """ 페이지업 : Page up """
        # if current page is not a first page, page up is possible
        # top position can not be negative, so if top position is going to be negative, we should set it as 0
        if (direction == self.UP) and (current_page > 0):
            self.top = max(0, self.top - self.max_lines)
            return

        """ 페이지다운 : Page down"""
        # if current page is not a last page, page down is possible
        if (direction == self.DOWN) and (current_page < self.page):
            self.top += self.max_lines
            return

    def display(self):
        """ 아이템(리스트)에서 Addstr()으로 오브젝트를 기록한다. """
        self.window.erase()
        for idx, item in enumerate(self.items[self.top:self.top + self.max_lines]):
            # 현재의 커서 라인을 하일라이트(par(2)=반전) 시킨다.
            if idx == self.current:
                self.window.addstr(idx, 0, item, curses.color_pair(2))
            else:
                self.window.addstr(idx, 0, item, curses.color_pair(1))
        self.window.refresh()


def main():
    making_lines = 100
    items = ['{number:0>3}.Item'.format(number=num + 1) for num in range(making_lines)]
    Screen(items)


if __name__ == '__main__':
    main()
