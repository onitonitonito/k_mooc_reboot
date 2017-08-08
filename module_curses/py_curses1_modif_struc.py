""" Curses Example @ Github.gist/claymcleod
refer to :  https://gist.github.com/claymcleod/b670285f334acd56ad1c
"""
import curses

k = 0           # Key valie 'int'
cursor_x = 0
cursor_y = 0

# Initialization
screen = curses.initscr()           # init screen
height, width = screen.getmaxyx()   # set HEIGHT, WIDTH
# curses.echo()
# screen.keypad(1)

# Declaration of strings
title = "Curses example"
subtitle = "Written by Clay McLeod"

def set_color():
    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

def get_keybindings_xy(cursor_x, cursor_y):
    screen.clear()

    if k == curses.KEY_DOWN:
        cursor_y = cursor_y + 1
    elif k == curses.KEY_UP:
        cursor_y = cursor_y - 1
    elif k == curses.KEY_RIGHT:
        cursor_x = cursor_x + 1
    elif k == curses.KEY_LEFT:
        cursor_x = cursor_x - 1

    cursor_x = max(0, cursor_x)
    cursor_x = min(width-1, cursor_x)

    cursor_y = max(0, cursor_y)
    cursor_y = min(height-1, cursor_y)

    return cursor_x, cursor_y

def get_coordinate():
    global keystr, statusbarstr, start_x_title, start_x_subtitle, start_x_keystr, start_y

    # changing continuously - string value.
    keystr = "Last key pressed: {}".format(k)
    statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
    if k == 0:
        keystr = "No key press detected..."

    # Centering calculations
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
    start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
    start_y = int((height // 2) - 2)

def draw_menu(screen):
    global k, cursor_x, cursor_y

    # Clear and refresh the screen for a blank canvas
    screen.clear()
    screen.refresh()

    set_color()

    # Loop where k is the last character pressed
    while (k != ord('q')):
        cursor_x, cursor_y = get_keybindings_xy(cursor_x, cursor_y)

        get_coordinate()


        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        screen.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        screen.attron(curses.color_pair(3))
        screen.addstr(height-1, 0, statusbarstr)
        screen.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        screen.attroff(curses.color_pair(3))

        # Turning on attributes for title
        screen.attron(curses.color_pair(2))
        screen.attron(curses.A_BOLD)

        # Rendering title
        screen.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        screen.attroff(curses.color_pair(2))
        screen.attroff(curses.A_BOLD)

        # Print rest of text  --- addstr(Y, X, STRING)
        screen.addstr(start_y + 1, start_x_subtitle, subtitle)
        screen.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
        screen.addstr(start_y + 5, start_x_keystr, keystr)
        screen.move(cursor_y, cursor_x)

        # Refresh the screen
        screen.refresh()

        # Wait for next input
        k = screen.getch()


if __name__ == '__main__':
    curses.wrapper(draw_menu)           # RECURSIVE CALL func=draw_menu
