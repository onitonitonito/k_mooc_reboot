#!/bin/user/python3
''' add parent dir in system path
'''
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
PARENT_DIR = sys.path[len(sys.path)-1]+"/"
# bg = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_sq060.png")
# -----------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sys

DESTIN_DIR = PARENT_DIR+'static/img/'

# -------------------------------------------------------
# tk = Tk()
# tk.title('First GUI')
# tk.wm_geometry(newGeometry='200x200+800+100')
# # ttk.Button(tk, text='HELLO WORLD', command=lambda: sys.exit()).grid()
# ttk.Button(tk, text='HELLO WORLD', command=lambda: sys.exit()).pack()
# tkinter.Button(tk, text='HELLO WORLD',bd=5, command=lambda: tkinter.messagebox.showinfo('TITLE','CONTENT')).pack()
#
# tk.mainloop()

# -------------------------------------------------------
# tk = Tk()
# tk.wm_geometry(newGeometry='200x200+800+100')
# f = Frame(tk)
# labelText = "I'm a label"
# l = Label(f, text=labelText)
# b = Button(f, text="ClickMe")
# l.pack(), b.pack(), f.pack()
# tk.mainloop()

# -------------------------------------------------------
# tk = Tk()
# tk.wm_geometry(newGeometry='300x300+800+100')
# tk.wm_attributes("-topmost",1)
#
# Label(tk, text='First Name').grid(row=0, sticky=W, padx=4)
# Entry(tk).grid(row=0, column=1, sticky=E, padx=4)
#
# Label(tk, text='Last Name').grid(row=1, sticky=W, padx=4)
# Entry(tk).grid(row=1, column=1, sticky=E, padx=4)
#
# Button(tk, text='SUBMIT').grid(row=3)
#
# tk.mainloop()

#-------------------------------------------------------
# tk = Tk()
# tk.wm_geometry(newGeometry='300x350+800+100')
# tk.wm_attributes("-topmost",1)
# tk.configure(bg='white')
#
# Label(tk, text='Description').grid( row=0, column=0, sticky=W )
# Entry(tk, width=40, bd=4).grid(     row=0, column=1, padx=10,)
# Button(tk, text='SUBMIT').grid(     row=5, column=1, sticky=W, padx=15)
#
# Label(tk, text='Quality (Condition)').grid(     row=1, column=0, sticky=W)
# Radiobutton(tk, text='New', value=1).grid(      row=2, column=0, sticky=W, padx=15,)
# Radiobutton(tk, text='Good', value=2).grid(     row=3, column=0, sticky=W, padx=15,)
# Radiobutton(tk, text='Poor', value=3).grid(     row=4, column=0, sticky=W, padx=15,)
# Radiobutton(tk, text='Damaged', value=4).grid(  row=5, column=0, sticky=W, padx=15,)
#
# Label(tk, text='Benefits').grid(            row=1, column=1, sticky=W,)
# Checkbutton(tk, text='Free Shipping').grid( row=2, column=1, sticky=W, padx=15,)
# Checkbutton(tk, text='Bonus Gift').grid(    row=3, column=1, sticky=W, padx=15,)
#
# c = Canvas(tk,width=210, height=190, bd=4, bg='white')
# fname = PhotoImage(file=DESTIN_DIR+'lotteria.png')
# ph = c.create_image(0,0, anchor='nw', image=fname)
#
# c.grid(    row=6, column=0, columnspan=2, sticky=W, padx=1,)
#
# tk.mainloop()
# -------------------------------------------------------

tk = Tk()
tk.wm_geometry(newGeometry='300x300+800+100')
tk.wm_attributes("-topmost",1)

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 * num2

    sumEntry.delete(0,'end')
    sumEntry.insert(0, sum)

def window_close():
    sys.exit()

def clear_all():
    num1Entry.delete(0,'end')
    num2Entry.delete(0,'end')
    sumEntry.delete(0,'end')

f1 = Frame(tk)
f2 = Frame(tk)
f3 = Frame(tk)
f4 = Frame(tk)
f5 = Frame(tk)

num1Entry = Entry(f1, width=8)
num1Entry.pack(side=LEFT)

Label(f1, text='x').pack(side=LEFT)

num2Entry = Entry(f1, width=8)
num2Entry.pack(side=LEFT)

equalButton = Button(f1, text='=')
equalButton.bind('<Button-1>', get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(f1, width=18)
sumEntry.pack(side=LEFT)

f1.pack(side=TOP)

#-------------------------------------------
b1 = Button(f2, text='1', width=8, pady=8)
b1.pack(side=LEFT)

b2 = Button(f2, text='2', width=8, pady=8)
b2.pack(side=LEFT)

b3 = Button(f2, text='3', width=8, pady=8)
b3.pack()

f2.pack(side=TOP)

#-------------------------------------------
b4 = Button(f3, text='4', width=8, pady=8)
b4.pack(side=LEFT)

b5 = Button(f3, text='5', width=8, pady=8)
b5.pack(side=LEFT)

b6 = Button(f3, text='6', width=8, pady=8)
b6.pack()

f3.pack(side=TOP)

#-------------------------------------------
b4 = Button(f4, text='7', width=8, pady=8)
b4.pack(side=LEFT)

b5 = Button(f4, text='8', width=8, pady=8)
b5.pack(side=LEFT)

b6 = Button(f4, text='9', width=8, pady=8)
b6.pack()

f4.pack(side=TOP)
#------------------------------------------
ac = Button(f5, text='AC',
                width=8, pady=8, fg='red',
                command=clear_all )
ac.pack(side=LEFT)

b5 = Button(f5, text='0', width=8, pady=8)
b5.pack(side=LEFT)

cl = Button(f5, text='CLOSE',
                width=8, pady=8, fg='red',
                command=window_close )
cl.pack()

f5.pack(side=TOP)

#------------------------------------------
tk.mainloop()



# -------------------------------------------------------
# Learn to Program 20 : TkInter Tutorial  - Derek Banas
# date: 2016. 8. 24.
# Code & Transcript : http://goo.gl/2cmB2V
# Best Python Book : http://amzn.to/2aapV6S
# https://www.youtube.com/watch?v=-tbWoZSi3LU
