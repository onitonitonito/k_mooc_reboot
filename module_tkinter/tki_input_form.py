from tkinter import Tk, Frame, Button, Entry, LEFT, RIGHT, TOP, BOTTOM

class App(object):
    def __init__(self, master):     # master = tk
        frame = Frame(master)       # frame = Frame(tk)
        frame.pack()                # same as tk.pack() = Place tk

        self.input = Entry(frame)
        self.input.pack(side=LEFT)  # place input frame,LEFT

        self.button = Button(frame, text="INPUT", command = self.output)
        self.button.pack(side=LEFT) # Place button, LEFT

    def output(self):               # function for Button click event
        print(self.input.get())



def main():
    tk = Tk()
    app = App(tk)

    tk.mainloop()


if __name__ == '__main__':
    main()
