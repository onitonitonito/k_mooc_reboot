#!/bin/user/python3
''' add parent dir in system path
'''
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
PARENT_DIR = sys.path[len(sys.path)-1]+"/"
# bg = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_sq060.png")
# -----------------------------------------

# TKinter Module Test
from tkinter import *               # Use TKinter Module (from)
from tkinter import messagebox      # Use messagebox
import random; import time          # Use random & Time Module

def helloCallBack():                # POP-UP messagebox option in Button function
    head = "HEAD : Hello Python 3.6 World"
    cntx = "CONTEXT : This is Practice for Message Box \n \
                            You will never be satisfied with this \n \
                            This is a only a example"
    msg = messagebox.showinfo(head, cntx)

tk = Tk()       # Declair Var.tk = Class.Tk()
canvas = Canvas(tk, width=600, height=800, highlightthickness=0)

tk.title("This is Tkinter module TEST_r01 (600x800)")
tk.resizable(1,1)           # resizable = 1, Not = 0
tk.wm_attributes("-topmost",1)

fname_bgrnd = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_105sq.png")  # Use filename(image)
fname_door = PhotoImage(file=PARENT_DIR+"static/img_stickman/door_01.png")         # Use filename(image)

for y in range(8):
    for x in range(6):
        canvas.create_image(x*105, y*105, image=fname_bgrnd, anchor='nw')
canvas.create_image(10,10, image=fname_door, anchor='nw')

images_left=[PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_01.png"),
    PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_02.png"),
    PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_03.png")]
images_right=[PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_04.png"),
    PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_05.png"),
    PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_06.png")]

for k in range(3):
    canvas.create_image(130,645, image=images_right[2], anchor='nw')


#fname_stick = PhotoImage(file=PARENT_DIR+"static/img_stickman/sman_04.png")
#canvas.create_image(130,645, image=fname_stick, anchor='nw')
# cannot USE Direct filename on Parameter.
# canvas.create_image(10,10, image=PhotoImage(file=PARENT_DIR+"static/img_stickman/door_01.png"), anchor='nw')

# refer canvas.syntax= https://www.tutorialspoint.com/python/tk_canvas.htm
canvas.pack()       # Create OBJECT --> Object Name = canvas.create_AAA ( )
points = [110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
ball = canvas.create_oval(0,0,25,25,fill='red')
bbox = canvas.create_rectangle(0,0,80,25,fill='blue')
poly = canvas.create_polygon(100, 140, points , fill='yellow', outline='black', width='3')

canvas.move(ball, 345, 100) # Object Move
canvas.move(bbox, 100, 700)
canvas.move(poly, 200, 300) # draw POLY: see this = https://goo.gl/x1qck2

# tk.geometry("100x100")      # Adjust TKinter Window geometry to 100 x 100
B = Button(tk, text="Comm'n Get in the door!", command = helloCallBack )   # TK_window Button(Text)
B.place (x = 50, y = 30)                # Slight difference btw helloCallBack and + ..Back()


# it causes Error msg when it terminates.
# so, use tk.mainloop(), if sprite doesn't move
while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# keep screen turn on. -- makeing a loop. '''
# tk.mainloop()
