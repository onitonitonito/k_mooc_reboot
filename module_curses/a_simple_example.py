"""  -------------- LESSON.01 - Simple TEXT string
"""
import curses

def simple_text():
    SCREEN = curses.initscr()       # initialize

    HEIGHT, WIDTH = SCREEN.getmaxyx()   # set HEIGHT, WIDTH
    STRING = 'PYTHON CURSES in Action!'

    SCREEN.border(0)
    SCREEN.addstr((HEIGHT//2-1), (WIDTH-(len(STRING)))//2, STRING)

    SCREEN.refresh()                # (draw) neccessity!
    SCREEN.getch()                  # keybindings

    curses.endwin()
# simple_text()


"""  -------------- LESSON.02 - BOXED New Window TEXT string
  refer to : https://stackoverflow.com/
  URL= https://goo.gl/TPFYXM
"""
def boxed_new_window_text():
    """ try: execute part / finally: curses.endwin() """
    SCREEN = curses.initscr()
    SCREEN.border(0)
    nw_string = 'im a new window box, you can try this at home!...'
    sc_string = 'this will be on the background screen'

    try:
        new_win = curses.newwin(10, 50, 10, 20)   #(size_Y, size_X, pos_Y, pos_X)
        new_win.box()

        SCREEN.addstr(2,3,sc_string)
        new_win.addstr(1,1,nw_string)   # del [:len(nw_string)-1]

        SCREEN.refresh()
        new_win.refresh()

        SCREEN.getch()                  # keybindings

    finally:
        curses.endwin()
boxed_new_window_text()
