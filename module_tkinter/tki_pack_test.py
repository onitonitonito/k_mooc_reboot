import sys
import tkinter as tki
import tkinter.messagebox as tkm

WIDTH = 230; HEIGHT = 230
BASE_DIR='./static/img/'

tk = tki.Tk()
tk.title('pack()-TEST! :: %sx%s'%(WIDTH,HEIGHT))

# [1st. frame] : 2 BUTTONS --------------------------------------
f01 = tki.Frame(tk)
b01 = tki.Button(f01, text='BUTTON', command=lambda:tkm.showinfo('TITLE','HELLO TKI~!!'), bd=5, )
b02 = tki.Button(f01, text='OK', command=lambda:sys.exit(), bd=5,)

f01.pack(side=tki.BOTTOM),
b01.pack(side = tki.LEFT), b02.pack()

# [2nd. frame] : TEXT BOX ----------------------------------------
f02 = tki.Frame(tk)
t01 = tki.Text(f02, height=5, width=30, bd=3, )     # Text spacing.
t01.insert(tki.INSERT, "HELLO HELLO WORLD!! \n")
t01.insert(tki.END, "Bye Bye.....TKI")

t01.tag_add('first','1.0','1.5')        # HELLO- 1st.row 0~5
t01.tag_add('second','2.0','2.3')       # Bye -  2nd.row 0~3
t01.tag_config('first', background='darkorange', foreground='white')
t01.tag_config('second', background='aqua', foreground='red')

f02.pack(side = tki.BOTTOM),
t01.pack()

# [ Canvas ] UPPER : Photo ---------------------------------------------------
c= tki.Canvas(tk, width=WIDTH, height=HEIGHT,)
fname = tki.PhotoImage(file=BASE_DIR+'favicon_backpack.png')
p01 = c.create_image(30, 30, anchor='nw', image=fname)
t02 = c.create_text(10,5,text='HELLO WORLD(Pursia)',font=('Pursia',14,'bold','underline'),anchor='nw',)

c.pack()

tk.mainloop()
