from tkinter import *
import random, time

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)    # make Ball.object
        self.canvas.move(self.id,245,100)     	  		# move to canvas_center

        self.x = int(random.randint(-3,3))
        if self.x == 0: self.x = 3
        self.y = -3										# ball movement

        self.canvas_height = self.canvas.winfo_height() # window height info.
        self.canvas_width = self.canvas.winfo_width()   # window width info.
        self.hit_bottom = False

    def hit_paddle(self,pos):                           # POS [0,1,2,3] = [x1,y1,x2,y2]
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <=paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <=paddle_pos[3]:
                return True
        return False

    def draw(self):                                     # ball draw()
        self.canvas.move(self.id,self.x,self.y)         # move ball up -1
        pos = self.canvas.coords(self.id)				# WHY? NO-Self ?? 'cause Array ??

        if pos[0] <=10:                                  # POS [0,1,2,3] = [x1,y1,x2,y2]
            self.x = int(random.randint(1,3))

        if pos[1] <=60:
            self.y = int(random.randint(1,3))

        if pos[2] >= self.canvas_width-10:
            self.x = int(random.randint(-3,-1))

        if pos[3] >= self.canvas_height-10:
            #self.hit_bottom == True
            self.y = int(random.randint(-3,-1))

        if self.hit_paddle(pos) == True:
            self.y = int(random.randint(-3,-1))

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,600)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<Button-1>",self.start_game)
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_Right)
        self.canvas.bind_all("<KeyRelease>",self.stop)

    def draw(self):                                         # draw paddle()
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <=10: self.x+=1
        if pos[2] >=self.canvas_width-10: self.x-=1

    def start_game(self,evt):
        pass        # Button-1 is not defined

    def turn_left(self,evt):
        self.x = -7         # Move -7

    def turn_Right(self,evt):
        self.x = 7        # move +7

    def stop(self,evt):
        self.x = 0              # move 0 (stop)

tk = Tk()
tk.title("Bounce Ball - ver.01.00_comment's added")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)      # Always on top

canvas = Canvas(tk, width=480, height=640, bd=0, highlightthickness=0)
obj_bground = PhotoImage(file='../static/img_stickman/bground_sq060.png', name='bground')


def set_bground():
    tx = PhotoImage.width(obj_bground)   # 105px
    ty = PhotoImage.height(obj_bground)  # 105px

    for x in range(0,9):
        for y in range(0,14):
            canvas.create_image(x*tx, y*ty, image=obj_bground, anchor='nw')

def set_border():
    obj_rect_L = canvas.create_rectangle(0,0,10,680, fill='grey')
    obj_rect_R = canvas.create_rectangle(470,0,480,680, fill='grey')
    obj_rect_U = canvas.create_rectangle(0,0,500,60, fill='grey')
    obj_rect_D = canvas.create_rectangle(0,630,480,640, fill='grey')

    obj_text01 = canvas.create_text(50, 20, text='SCORE :',font=('Normal',15,'bold'), anchor='nw')
    obj_text02 = canvas.create_text(370, 20, text='BALL :',font=('Normal',15,'bold'), anchor='nw')


set_bground()
set_border()

canvas.pack()
tk.update()
#tk.mainloop()       # temporary stop screen

paddle = Paddle(canvas,"blue")      # declair Paddle is Paddle Class
ball = Ball(canvas,paddle,"red")    # Declair ball is Ball Class, afterward.

while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
