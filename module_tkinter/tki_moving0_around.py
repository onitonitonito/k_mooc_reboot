import tkinter as tki
import os, time

def get_filename(file_name):
    fname_with_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'static', 'img', file_name)
    return fname_with_dir

def move_icon(obj, dx, dy, time_sleep=0.05):
    canvas.move(obj, dx, dy)
    tk.update()
    time.sleep(time_sleep)

fname1 = get_filename('icon_face32.png')
fname2 = get_filename('lotteria.png')

tk = tki.Tk()
canvas = tki.Canvas(tk, width=400, height=400)
canvas.pack()           # SHOW canvas

face1 = tki.PhotoImage(file=fname1)

canvas.create_image(10, 10, anchor='nw', image=face1)
canvas.create_image(0, 0, anchor='nw', image=face1)

canvas.move(2, 200, 200)


while True:

    for n in range(70):
        move_icon(1, 5, 0, 0.02)

    for n in range(70):
        move_icon(1, 0, 5, 0.02)

    for n in range(70):
        move_icon(1, -5, 0, 0.02)

    for n in range(70):
        move_icon(1, 0, -5, 0.02)

tk.mainloop()           # STOP Screen
