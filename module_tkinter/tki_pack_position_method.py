from tkinter import Tk, Canvas, Frame, Button, Label, Entry
from tkinter import LEFT, RIGHT, BOTTOM, TOP

tk = Tk()

canvas = Canvas(tk,width=300, height=200, bd=1, highlightthickness=0)
canvas.pack()

frame01 = Frame(tk)
frame01.pack()

frame02 = Frame(tk)
frame02.pack()

bottomframe = Frame(tk)
bottomframe.pack( side = BOTTOM )

label = Label(frame01, text="USER NAME: ")
label.pack(side=LEFT)

entry = Entry(frame01, bd=3)
entry.pack(side = LEFT)

redbutton = Button(frame01, text="Red", fg="red")
redbutton.pack( side = RIGHT)

greenbutton = Button(frame02, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame02, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

tk.mainloop()

# https://www.tutorialspoint.com
# https://www.tutorialspoint.com/python/python_gui_programming.htm
# Python Tkinter pack() : https://www.tutorialspoint.com/python/tk_pack.htm
