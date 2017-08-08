import tkinter as tki
import os, time

tk = tki.Tk()
canvas = tki.Canvas(tk, width=400, height=400)
canvas.pack()           # SHOW canvas

def get_filename(file_name):
    fname_with_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'static', 'img', file_name)
    return fname_with_dir

def move_icon(obj, dx, dy, time_sleep=0.05):
    canvas.move(obj, dx, dy)
    tk.update()
    time.sleep(time_sleep)

def move_around(obj, dx=5, dy=5, dx_times=10, dy_times=10, time_sleep=0.05):
    for n in range(dx_times):
        move_icon(obj, dx, 0, time_sleep)

    for n in range(dy_times):
        move_icon(obj, 0, dy, time_sleep)

    for n in range(dx_times):
        move_icon(obj, -dx, 0, time_sleep)

    for n in range(dy_times):
        move_icon(obj, 0, -dy, time_sleep)

fname1 = get_filename('icon_face32.png')
fname2 = get_filename('lotteria.png')

face1 = tki.PhotoImage(file=fname1)

_a = canvas.create_image(10, 10, anchor='nw', image=face1)
_b = canvas.create_image(0, 0, anchor='se', image=face1)

canvas.move(_b, 150, 150)

while True:
    move_around(_a, 5, 5, 70, 70, 0.005)
    move_around(_b, 5, 5, 30, 30, 0.01)

tk.mainloop()           # STOP Screen
