""" PYTHON SNIPPETS!
  refer to : https://www.programcreek.com/python/index/164/curses
"""
import curses

def display_init():
    stdscr = curses.initscr()
    curses.echo()
    stdscr.keypad(1)
    return stdscr
# display_init()

""" quick example for ncurses : Gist.github/myano
  refer to : https://gist.github.com/myano/1055442
"""

#!/usr/bin/env python
import curses.textpad
import time

stdscr = curses.initscr()

curses.noecho()
#curses.echo()

begin_x = 20
begin_y = 7

height = 5
width = 40

win = curses.newwin(height, width, begin_y, begin_x)
tb = curses.textpad.Textbox(win)
text = tb.edit()
curses.addstr(0,0,text)

# hw = "Hello world!"
# while 1:
#    c = stdscr.getch()
#    if c == ord('p'):
#        pass
#    elif c == ord('q'):
#        break # Exit the while()
#    elif c == curses.KEY_HOME:
#         x = y = 0

curses.endwin()
