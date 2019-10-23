"""
# Python Calculator – Create A Simple GUI Calculator Using Tkinter
# https://www.simplifiedpython.net/python-calculator/
#
#\n\n"""
print(__doc__)

# from tkinter import *
import tkinter as tk

"""# define function"""

# creating from for calculator
def icalc(source, side):
    store_obj = tk.Frame(source, borderwidth=4, bd=4, bg="powder blue")
    store_obj.pack(side=side, expand=tk.YES, fill=tk.BOTH)
    return store_obj

# creating a buttom
def button(source, side, text, command=None):
    store_obj = tk.Button(source, text=text, command=command)
    store_obj.pack(side=side, expand=tk.YES, fill=tk.BOTH)
    return store_obj


class app(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.master.title('Calculator')

        # add thick-display screen
        display = tk.StringVar()
        entry = tk.Entry(
            self, relief=tk.RIDGE,
            textvariable=display,
            justify=tk.RIGHT,
            bd=30,
            bg='powder blue'
            )

        # show entry by pack
        entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        # Add 'C' on the TOP
        for clear_button in (["C"]):
            erase = icalc(self, side=tk.TOP)

            for ichar in clear_button:
                button(
                    erase,
                    tk.LEFT,
                    ichar,
                    lambda store_obj=display, q=ichar: store_obj.set(''),
                    )

        # Add numeric & function keys by LEFT
        for num_button in ("789/", "456*", "123-", "0.+"):
            func_num = icalc(self, side=tk.TOP)

            for i_equals in num_button:
                button(
                    func_num,
                    tk.LEFT,
                    i_equals,
                    lambda store_obj=display, q=i_equals: store_obj.set(
                                                        store_obj.get() + q),
                )

        # Add EQUAL key
        equal_button = icalc(self, tk.TOP)

        for i_equals in (["="]):
            if i_equals == "=":
                button_i_equals = button(equal_button, tk.LEFT, i_equals)
                button_i_equals.bind(
                    '<ButtonRelease-1>',
                    lambda e, s=self, store_obj=display: s.calc(store_obj), '+')
            else:
                button_i_equals = button(
                    equal_button,
                    tk.LEFT,
                    i_equals,
                    lambda store_obj=display, s=' %s '% i_equals: store_obj.set(
                                                    store_obj.get() + s),
                    )

    # Applying Event Trigger On Widgets
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("...ERROR!...")



# Start the GUI
if __name__ == '__main__':
    tk = app()

    tk.mainloop()
