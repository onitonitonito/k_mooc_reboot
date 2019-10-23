"""
* Ball / Paddle 오브젝트 클래스
* Config 외부변수 설정
"""
import time

from tkinter import Tk
from tkinter import Canvas
from pinball_class.config import *
from pinball_class.buster_class import Ball
from pinball_class.buster_class import Paddle


tk = Tk()
tk.title(WINDOW_TITLE)
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk,width=SCREEN_WIDTH,height=SCREEN_HEIGHT,
                bd=0, highlightthickness=0)

paddle = Paddle(canvas)
ball = Ball(canvas, paddle)

canvas.pack()
tk.update()

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
