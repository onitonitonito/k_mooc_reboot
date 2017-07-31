#!/bin/user/python3
import tkinter as tki

''' add parent dir in system path
'''
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
PARENT_DIR = sys.path[len(sys.path)-1]+"/"
# bg = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_sq060.png")
# -----------------------------------------

DESTIN_DIR = PARENT_DIR+'static/img/'

tk = tki.Tk()
tk.wm_geometry(newGeometry='300x300+800+100')
tk.wm_attributes("-topmost",1)
#-----------------------------------------------------
def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 * num2

    sumEntry.delete(0,'end')
    sumEntry.insert(0, sum)

def widow_close():
    sys.exit()

def clear_all():
    num1Entry.delete(0,'end')
    num2Entry.delete(0,'end')
    sumEntry.delete(0,'end')

num1Entry = tki.Entry(tk, width=5)
num1Entry.pack(side=tki.LEFT)

tki.Label(tk, text='x').pack(side=tki.LEFT)

num2Entry = tki.Entry(tk, width=5)
num2Entry.pack(side=tki.LEFT)

equalButton = tki.Button(tk, text='=')
equalButton.bind('<Button-1>', get_sum)
equalButton.pack(side=tki.LEFT)

sumEntry = tki.Entry(tk)
sumEntry.pack(side=tki.LEFT)

clearButton = tki.Button(tk, text='CL')
clearButton.bind('<Button-1>', clear_all)
clearButton.pack(side=tki.LEFT)



tk.mainloop()
