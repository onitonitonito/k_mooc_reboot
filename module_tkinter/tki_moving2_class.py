import tkinter as tki
import os, time

tk = tki.Tk()
canvas = tki.Canvas(tk, width=500, height=500)

class FaceIcon(object):
    """
    """
    def __init__(self, fname, pos_x=100, pos_y=100):
        """ fname = file_name with os.dir
        """
        self.fname = fname
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image_obj = tki.PhotoImage(file=fname)
        self.obj = canvas.create_image(0, 0, anchor='nw', image=self.image_obj)
        canvas.move(self.obj, self.pos_x, self.pos_y)
        canvas.pack()

    def move_icon(self, dx, dy, time_sleep=0.05):
        canvas.move(self.obj, dx, dy)
        tk.update()
        time.sleep(time_sleep)

    def move_around(self, dx=5, dy=5, dx_times=10, dy_times=10, time_sleep=0.05):
        for n in range(dx_times):
            self.move_icon(dx, 0, time_sleep)

        for n in range(dy_times):
            self.move_icon( 0, dy, time_sleep)

        for n in range(dx_times):
            self.move_icon(-dx, 0, time_sleep)

        for n in range(dy_times):
            self.move_icon(0, -dy, time_sleep)


def get_filename(file_name):
    fname_with_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'static', 'img', file_name)
    print(fname_with_dir)
    return fname_with_dir

f_name1 = get_filename('icon_face32.png')
f_name2 = get_filename('lotteria.png')

pack1 = FaceIcon(f_name1, 50, 50)
pack2 = FaceIcon(f_name2, 0, 0)

while True:
    for n in range(150):
        pack1.move_icon(dx=2, dy=2, time_sleep=0.01)

    for n in range(90):
        pack2.move_icon(dx=3, dy=3, time_sleep=0.007)

    time.sleep(0.5)

    for n in range(150):
        pack1.move_icon(dx=-2, dy=-2, time_sleep=0.01)

    for n in range(90):
        pack2.move_icon(dx=-3, dy=-3, time_sleep=0.007)

    time.sleep(0.5)

tk.mainloop()           # STOP Screen
