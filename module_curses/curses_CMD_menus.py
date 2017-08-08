#!/usr/bin/env python
""" ----------------------- Code Project: Build an Ncurses UI with Python
  refer to : http://www.tuxradar.com/(home) URL= https://goo.gl/XT9f
"""
import os
import curses

screen = curses.initscr()

def get_param(prompt_string):       # In='str' / OUT= value 'str'
     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, prompt_string)
     screen.refresh()
     _input = screen.getstr(5, 5, 60)
     return _input

def execute_cmd(cmd_string):
     os.system('cls')
     a = os.system(cmd_string)
     print()
     if a == 0:
          print("Command executed correctly")
     else:
          print("Command terminated with error")
     input("Press enter")
     print()

def do_menu01():
    username = get_param("Enter the username")
    homedir = get_param("Enter the home directory, eg /home/nate")
    groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
    shell = get_param("Enter the shell, eg /bin/bash:")
    curses.endwin()
    execute_cmd("useradd -d " + \
        homedir + " -g 1000 -G " + \
        groups + " -m -s " + \
        shell + " " + username)

def do_menu02():
    curses.endwin()
    execute_cmd("apachectl restart")

def do_menu03():
    curses.endwin()
    execute_cmd("dir")
    # execute_cmd("df -h")

def do_menu04():
    curses.endwin()
    raise SystemExit

def do_keybinds():
    x = screen.getch()      # get keybind = 'int'

    if x == ord('1'):
        do_menu01()
    elif x == ord('2'):
        do_menu02()
    elif x == ord('3'):
        do_menu03()
    elif x == ord('4'):
        do_menu04()

def set_addstr(y, x, num_color_set, string):
    _arg = curses.color_pair(num_color_set)
    if num_color_set:
        screen.attron(_arg)
    screen.addstr(y, x, string)
    if num_color_set:
        screen.attroff(_arg)

def set_screen(screen):
    screen.clear()
    screen.border(0)

    set_addstr(2, 2, 1, "Please enter a number...")
    set_addstr(4, 4, 0, "1 - Add a user")
    set_addstr(5, 4, 0, "2 - Restart Apache")
    set_addstr(6, 4, 0, "3 - Show disk space")
    set_addstr(7, 4, 0, "4 - Exit")
    set_addstr(7, 8, 2, "Exit")
    # screen.refresh()

def set_color():
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

while True:
    set_color()
    set_screen(screen)

    do_keybinds()
