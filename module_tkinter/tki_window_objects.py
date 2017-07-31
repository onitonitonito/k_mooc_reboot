#!/bin/user/python3
''' add parent dir in system path
'''
import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
PARENT_DIR = sys.path[len(sys.path)-1]+"/"
# bg = PhotoImage(file=PARENT_DIR+"static/img_stickman/bground_sq060.png")
# -----------------------------------------

import tkinter as tki               # module import as tki
import tkinter.messagebox as msg    # module import as msg
import sys

# declare --2 Objents (tk, canvas)
tk = tki.Tk()
tk.title("HELLO WORLD! 640x480 window")     # Header title (v)
tk.resizable(width=None,height=None)        # Not resozeable (v)
tk.wm_attributes("-topmost",1)              # always on top (f)

canvas = tki.Canvas(tk, width='640', height='480', bd=1, highlightthickness=0)

obj_bground = tki.PhotoImage(file=PARENT_DIR+'static/img_stickman/bground_sq060.png', name='tile_060px')
obj_photo = tki.PhotoImage(file=PARENT_DIR+'static/img/favicon_backpack.png', name='backpack')

def set_bground():
    w = tki.PhotoImage.width(obj_bground)              # width (f) .. return image size_w
    h = tki.PhotoImage.height(obj_bground)             # height (f).. return image size_h

    for x in range(0,17):
        for y in range(0,10):
            canvas.create_image(w*x, h*y, image=obj_bground, anchor='nw')    # set Image_photo

def set_inner_window():
    window_content='''\
    This is a label_content
    -----------------------
    Main Page               .
    Community portal        .
    Preferences             .
    Requested entries       .
    Recent changes          .
    Random entry            .
    Help                    .
    Donations               .
    Contact us              .
    Tools                   .
    What links here         .
    Related changes         .
    '''
    label_frame = tki.LabelFrame(canvas, text='This is a LabelFrame!')
    label_content = tki.Label(label_frame, text=window_content)
    obj_window = canvas.create_window(640,0,height=250,width=200,anchor='ne', window=label_frame )
    label_content.pack()

def button_close():         # close window
    sys.exit()

def button_callback():      # pop-up message box option
    head = 'head message'
    content = 'board message:\n   You\'ll be never satisfied!\n   with this message.\n   ha-ha'
    obj_message = msg.showinfo(title=head, message=content)  # showinfo (f)

set_bground()               # bground should be set at first of all
set_inner_window()

obj_oval = canvas.create_oval(0,0,60,40, fill='yellow')
obj_rect = canvas.create_rectangle(0,0,40,40, fill='orange')

# font *args= 100,180, text='HELLO', anchor='nw', font=['normal',10,'bold','underline'],
obj_text00 = canvas.create_text(100, 180, text='HELLO WORLD(Normal)', anchor='nw',)
obj_text01 = canvas.create_text(100, 160, text='HELLO WORLD(Pursia)',font=('Pursia',10,'bold','underline'),anchor='nw',)

obj_button00 = tki.Button(tk, text='[POP-UP]\ntake it easy!', command=button_callback )
obj_button01 = tki.Button(tk, text='EXIT\n(belive me!)', command=button_close )

canvas.create_image(0,480, image=obj_photo, anchor='sw')    # set Image_photo

obj_button00.place(x=200, y=430, anchor='nw') # cnf={} = x=200, y=100m ... format
obj_button01.place(x=290, y=430, anchor='nw') # cnf={} = x=200, y=100m ... format

canvas.move(obj_oval, 180, 200)         # Move option
canvas.move(obj_rect, 100, 200)         # Move option

canvas.pack()                           # show canvas OBJECT
tk.mainloop(n=0)                        # keep mainloop preventing console closed
