from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sys


DESTIN_DIR = './static/img/'

tk = Tk()
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

num1Entry = Entry(tk, width=5)
num1Entry.pack(side=LEFT)

Label(tk, text='x').pack(side=LEFT)

num2Entry = Entry(tk, width=5)
num2Entry.pack(side=LEFT)

equalButton = Button(tk, text='=')
equalButton.bind('<Button-1>', get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(tk)
sumEntry.pack(side=LEFT)



tk.mainloop()
