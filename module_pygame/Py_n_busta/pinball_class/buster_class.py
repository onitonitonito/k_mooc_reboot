"""
* Ball 오브젝트
* Paddle 오브젝트
"""
import random
from .config import *


class Paddle(object):
    def __init__(self, canvas):
        self.x = 0

        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()

        self.id = canvas.create_rectangle(
            0, 0, PAD_WIDTH, PAD_HEIGHT, fill=PAD_COLOR)

        self.canvas.move(self.id, (SCREEN_WIDTH - PAD_WIDTH) /
                         2, SCREEN_HEIGHT - 3 * PAD_HEIGHT)

        # 키 바인딩 함수 : Call-Back()
        self.canvas.bind_all("<Button-1>", self.start_game)
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
        self.canvas.bind_all("<KeyRelease>", self.stop)

    def is_x_min(self, pos):
        if pos[0] <= 0:
            return True

    def is_x_max(self, pos):
        if pos[2] >= self.canvas_width:
            return True

    def draw(self):
        pos = self.canvas.coords(self.id)
        if self.is_x_max(pos) or self.is_x_min(pos):
            self.x = 0
        else:
            self.canvas.move(self.id, self.x, 0)

    def start_game(self, evt):
        pass

    def move_left(self, evt):
        pos = self.canvas.coords(self.id)
        if self.is_x_min(pos):
            self.x = 2 * PAD_SPEED
        else:
            self.x = -1 * PAD_SPEED

    def move_right(self, evt):
        pos = self.canvas.coords(self.id)
        if self.is_x_max(pos):
            self.x = -2 * PAD_SPEED
        else:
            self.x = 1 * PAD_SPEED

    def stop(self, evt):
        self.x = 0


class Ball(object):
    def __init__(self, canvas, paddle):
        self.hit_bottom = False

        self.canvas = canvas
        self.paddle = paddle

        self.id = canvas.create_oval(0, 0, BALL_DIA, BALL_DIA, fill=BALL_COLOR)
        self.canvas.move(self.id, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 5 / 6)

        self.x = int(random.randint(-1 * BALL_SPEED, 1 * BALL_SPEED))
        if self.x == 0:
            self.x = BALL_SPEED
        self.y = -1 * BALL_SPEED

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def is_collide(self, ball_pos):
        pad_pos = self.canvas.coords(self.paddle.id)
        if ball_pos[2] >= pad_pos[0] and ball_pos[0] <= pad_pos[2]:
            if ball_pos[3] >= pad_pos[1] and ball_pos[3] <= pad_pos[3]:
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # 수평으로 장애물(좌/우 벽체)에 부딧히는지 판단
        if pos[0] <= 0:
            self.x = int(random.randint(1, BALL_SPEED))

        if pos[2] >= self.canvas_width:
            self.x = int(random.randint(-1 * BALL_SPEED, -1))

        # 수직으로 장애물(천정/패들/바닥) 부딧히는지 판단
        if pos[1] <= 0:
            self.y = int(random.randint(1, BALL_SPEED))

        if pos[3] >= self.canvas_height:
            self.y = -1 * BALL_SPEED
            # self.hit_bottom == True

        if self.is_collide(pos) == True:
            self.y = int(random.randint(-1 * BALL_SPEED, -1))
            
