import tkinter as tki

# def mouse_click(event):
#     global x1,y1
#     x1 = event.x
#     y1 = event.y

def mouse_drop(event):
    global x2,y2
    x2 = event.x
    y2 = event.y

    # cv.create_line(x1,y1,x2,y2, width=5, fill="red")

def mouse_drag(event):
    global x1,y1
    x1 = event.x
    y1 = event.y

    cv.create_oval(x1,y1,x1+10,y1+10, width=1, fill="blue")

def main():
    # cv.bind("<Button-1>", mouse_click)
    # cv.bind("<ButtonRelease-1>", mouse_drop)
    cv.bind("<B1-Motion>", mouse_drag)

    cv.pack()
    tk.mainloop()


if __name__ == '__main__':
    # tki, cv should be placed out side of [DEF]
    tk = tki.Tk()
    tk.title('Simple Paint Brush Tool')
    cv = tki.Canvas(master=tk, height=300, width=300)

    main()
