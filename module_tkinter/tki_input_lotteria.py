import sys, datetime
import tkinter as tki

CHEIF = ['Gordon Ramsay','jamie oliver','Dirty Hand','BAEK JW',]
MENU = {
    'Hamberger'         : (3000,'ECH'),
    'Pizza'             : (5000,'PCS'),
    'Chicken Frie'      : (7000,'BAS'),
    'Cold Noodle'       : (1500,'DSH'),
    'Lunch Box'         : (2500,'BOX'),
    'Buritto-chicken'   : (3000,'ECH'),
    'Ice Cream'         : ( 500,'CON'),
    'Coca Cola'         : ( 500,'BOT'),
}
MENU_IDX = [ item for item in MENU.keys()]
print(MENU_IDX)
print(MENU_IDX[0])

DESTIN_DIR = './static/img/'
WINDOW_WIDTH= 300
WINDOW_HEIGHT= 80

def calc_total():
    # print(e.get())
    pass

tk = tki.Tk()       # tk is Toolkit class
tk.title('Receit Maker (%sx%s)'%(WINDOW_WIDTH, WINDOW_HEIGHT))

# [TOP BANNER] ------------------------------------------------
c = tki.Canvas(tk, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bd=1, bg='white')
fname = tki.PhotoImage(file=DESTIN_DIR+'lotteria_banner.png')
p01 = c.create_image(5,5, anchor='nw', image=fname, )
c.grid(row=0, column=0, columnspan=4, sticky=tki.W, padx=4)

# [MENU LIST] ------------------------------------------------
for n in range(len(MENU_IDX)):
    tki.Label(tk, text='%-20s (%5s \\): '%(MENU_IDX[n],MENU[MENU_IDX[n]][0])).grid(  row=n+1, column=0, sticky=tki.E, padx=4)
    tki.Entry(tk, width=10, bd=3).grid(                                             row=n+1, column=1, sticky=tki.W, padx=4)
    tki.Label(tk, text=MENU[MENU_IDX[n]][1]).grid(                                  row=n+1, column=2, sticky=tki.W, padx=4)
tki.Label(tk,text="").grid(row=9, column=0, sticky=tki.W)
tki.Button(tk, width=12, text='SUBMIT', bd=3, command=calc_total, ).grid(row=10, column=0, sticky=tki.E, padx=4)
tki.Button(tk, width=8, text='CANCEL', bd=3, fg="red", command=lambda:sys.exit()).grid(row=10, column=1, columnspan=2, sticky=tki.W, padx=4)


tk.mainloop()

# def sort_line_menues():
#     idx_list = list(MENU.keys())    #print(idx_list)
#
#     for n in idx_list:
#         line_menu(str(n+' (%s\\)')%MENU[n][0],str(MENU[n][1])) # args=Lable, unit
#
# def line_menu(label='None',unit='None'):
#     global e
#     f = tki.Frame(tk)      # f = Frame(tk)
#     l1 = tki.Label(f, text=label+" :")
#     e= tki.Entry(f, width=5, bd=3)
#     l2= tki.Label(f, text=" "+unit)
#
#     f.pack(side=tki.TOP)               # same as tk.pack() = Place tk
#     l1.pack(side=tki.LEFT),
#     e.pack(side=tki.LEFT),
#     l2.pack(side=tki.LEFT)
#
# def set_buttons():
#     f = tki.Frame(tk)
#     c1 = tki.Canvas(tk,width=WINDOW_WIDTH, height=15,)
#     b1 = tki.Button(f, width=12, text='SUBMIT', bd=3, command=calc_total, )
#     b2 = tki.Button(f, width=8, text='CANCEL', bd=3, fg="red", command=lambda:sys.exit())
#
#     c1.pack()
#     f.pack(side=tki.BOTTOM), b1.pack(side=tki.LEFT), b2.pack(side=tki.LEFT)
#
# def calc_total():
#     print(e.get())
#     pass
#
# if __name__ == '__main__':
#     sort_line_menues()
#     set_buttons()
#
#     tk.mainloop()
