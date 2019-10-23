import os
import time
import random
from tkinter import *

DIRS = os.path.dirname(__file__).partition("Hello-Python3.6\\")
ROOT = DIRS[0] + DIRS[1]
FILE_DIR = ROOT + "\\_statics\\img_bounce\\"


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Bounce Ball(480 x 640) -ver.1.00,Add Game Class")# Header
        self.tk.resizable(0,0)                   # resize's not allowed (=0)
        self.tk.wm_attributes("-topmost",1)      # Always on top

        self.canvas_height = 640; self.canvas_width = 480   # ....N0 NEED.
        self.canvas = Canvas(self.tk, width=self.canvas_width, \
                    height=self.canvas_height, bd=1, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

    def set_bground(self):
        self.bg = PhotoImage(file=FILE_DIR + "Wallpaper_00.png")
        w = self.bg.width()     # What's this ?
        h = self.bg.height()
        for x in range(0,9):
            for y in range(0,12):
                self.canvas.create_image(x*w,y*h,image=self.bg, anchor='nw')
                self.sprites =[]
                self.running = True

        self.paddle = Paddle(self.canvas,"blue")      # declair Paddle is Paddle Class
        self.ball = Ball(self.canvas,self.paddle,"red")    # Declair ball is Ball Class, afterward.

        self.block_01 = Block(self.canvas, 20+(0*90),100, "orange")  # Declair Block is
        self.block_02 = Block(self.canvas, 20+(1*90),100, "orange")  # Declair Block is
        self.block_03 = Block(self.canvas, 20+(2*90),100, "orange")  # Declair Block is
        self.block_04 = Block(self.canvas, 20+(3*90),100, "orange")  # Declair Block is
        self.block_05 = Block(self.canvas, 20+(4*90),100, "orange")  # Declair Block is

        self.block_11 = Block(self.canvas, 20+(0*90),125, "yellow")  # Declair Block is
        self.block_12 = Block(self.canvas, 20+(1*90),125, "yellow")  # Declair Block is
        self.block_13 = Block(self.canvas, 20+(2*90),125, "yellow")  # Declair Block is
        self.block_14 = Block(self.canvas, 20+(3*90),125, "yellow")  # Declair Block is
        self.block_15 = Block(self.canvas, 20+(4*90),125, "yellow")  # Declair Block is

        self.block_21 = Block(self.canvas, 20+(0*90),150, "orange")  # Declair Block is
        self.block_22 = Block(self.canvas, 20+(1*90),150, "orange")  # Declair Block is
        self.block_23 = Block(self.canvas, 20+(2*90),150, "orange")  # Declair Block is
        self.block_24 = Block(self.canvas, 20+(3*90),150, "orange")  # Declair Block is
        self.block_25 = Block(self.canvas, 20+(4*90),150, "orange")  # Declair Block is

        self.block_31 = Block(self.canvas, 20+(0*90),175, "yellow")  # Declair Block is
        self.block_32 = Block(self.canvas, 20+(1*90),175, "yellow")  # Declair Block is
        self.block_33 = Block(self.canvas, 20+(2*90),175, "yellow")  # Declair Block is
        self.block_34 = Block(self.canvas, 20+(3*90),175, "yellow")  # Declair Block is
        self.block_35 = Block(self.canvas, 20+(4*90),175, "yellow")  # Declair Block is

    def mainloop(self):
        while True:
            if self.ball.hit_bottom == False:
                self.ball.draw()
                self.paddle.draw()

                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)    # make Ball.object
        self.canvas.move(self.id,245,300)     	  		# move to canvas_center

        self.x = 0          # stop
        self.y = 0          # Stop

        self.canvas_height = self.canvas.winfo_height() # window height info.
        self.canvas_width = self.canvas.winfo_width()   # window width info.
        self.hit_bottom = False
        # self.stopBall = True

        self.canvas.bind_all("<KeyPress-space>",self.toggleBALL)
        self.canvas.bind_all("<KeyPress-z>",self.stopBALL)

        '''
        self.canvas.bind_all("<Button-1>",self.start_game)  Mouse Button-1
        '''

    def stopBALL(self,event):
        self.x = 0
        self.y = 0

    def toggleBALL(self,event):
        self.x = int(random.randint(-3,3))
        if self.x == 0:  self.x = 3
        self.y = -3

        '''
        if self.stopBall == False:
            self.x = int(random.randint(-3,3))
            if self.x == 0:  self.x = 3
            self.y = -3
            self.stopBall == True
        else:
            self.x = 0
            self.y = 0
            self.stopBall == False
        '''

    def hit_paddle(self,pos):                           # POS [0,1,2,3] = [x1,y1,x2,y2]
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <=paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <=paddle_pos[3]:
                return True
        return False

    def draw(self):                                     # ball draw()
        self.canvas.move(self.id,self.x,self.y)         # move ball up -1
        pos = self.canvas.coords(self.id)				# WHY? NO-Self ?? 'cause Array ??

        if pos[0] <=0:                                  # POS [0,1,2,3] = [x1,y1,x2,y2]
            self.x = int(random.randint(1,3))

        if pos[1] <=0:
            self.y = int(random.randint(1,3))

        if pos[2] >= self.canvas_width:
            self.x = int(random.randint(-3,-1))

        if pos[3] >= self.canvas_height:
            self.hit_bottom == True

        if self.hit_paddle(pos) == True:
            self.y = int(random.randint(-3,-1))

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_Right)
        self.canvas.bind_all("<KeyRelease>",self.stop)

        '''
        canvas.bind_all('<KeyPress-Up>', movetriangle)
        canvas.bind_all('<KeyPress-Down>', movetriangle)
        canvas.bind_all('<KeyPress-w>', movetriangle)
        '''

    def draw(self):                                         # draw paddle()
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=0: self.x = 0
        if pos[2] >=self.canvas_width: self.x = 0

    def turn_left(self,event):
        self.x = -7         # Move -7

    def turn_Right(self,event):
        self.x = 7        # move +7

    def stop(self,event):
        self.x = 0              # move 0 (stop)

class Block:
    def __init__(self,canvas,x,y,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,80,20,fill=color)
        self.canvas.move(self.id, x ,y)

    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos = self.canvas.coords(self.id)


game = Game()
game.set_bground()
game.mainloop()
