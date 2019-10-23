"""
# class_object.py - 클래수 함수정의
#    : Game, Coords, Sprite                           = Parents
#    : ExitDoorSprite, PlatformSprite, StickManSprite = children of Sprite
"""
print(__doc__)

import os
import time

from tkinter import *
from assets.config import *


class Game(object):
    """
    # tk윈도우 활성화, Game 루프실행 후, Sprites[] 등록 된 오브젝트 이동
    # sprites 에는 Sprite 오브젝트를 등록시킨다.
    #  : mainloop()
    """
    def __init__(self):
        self.sprites = []
        self.running = True
        self.canvas_width = WINDOW_WIDTH
        self.canvas_height = WINDOW_HEIGHT

        self.tk = Tk()
        self.tk.title("Stick Man Dash! - window [{} x {}]".format(
            self.canvas_width,
            self.canvas_height))
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk,
                             width=self.canvas_width,
                             height=self.canvas_height,
                             highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

        # 배경 타일을 그린다 ( 배경타일[105x105] .. 5x8 반복 = 배경[525x840])
        self.bg = PhotoImage(file=dir_img + "bground_105sq.png")
        w = self.bg.width()     # What's this ?
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 8):
                self.canvas.create_image(
                    x * w, y * h, image=self.bg, anchor='nw')

    def mainloop(self):
        while True:
            if self.running == True:
                # game.sprites = []에 등록된 스프라이트를 move()시킨다.
                for sprite in self.sprites:
                    sprite.move()
                time.sleep(FLIP_SECOND)           # 0.01 --> 테스트 x100 느리게
                self.tk.update_idletasks()
                self.tk.update()


class Sprite(object):
    """
    # Game Class를 상수로 받아서 처리. (상속 할 '모체'가 됨)
    #  : move(), coords()
    """
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        # 상속을 위한 공란 - Stickman에서 재정의
        # move()는 스틱맨만 정의할 것임.
        pass

    def coords(self):
        # coords()는 최신 좌표값 리턴 (움직이는 스틱맨 만 필요함.)
        # 고정된 물체는, Coords() 클래스로 정의 함
        return self.coordinates


class Coords(object):
    """
    # x1, y1, x2, y2 를 받는다.
    # Coords() 클래스는 실시간 오브젝트 좌표의 충돌여부를 판단한다.
    # 통상, 움직이는 오브젝트 = co1,  정지된 오브젝트 = co2 로 지정한다.
    """
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2


class PlatformSprite(Sprite):
    """
    # 플랫폼[대,중,소]은 다수이므로 특정불가 - 이미지123, 좌표xy, 넓이,높이)
    """
    def __init__(self, game, bar_number, x, y, width, height):
        super().__init__(game)
        if bar_number == 1:
            self.photo_image = PhotoImage(file=dir_img+'Platform_01.png')
        elif bar_number == 2:
            self.photo_image = PhotoImage(file=dir_img+'Platform_02.png')
        elif bar_number == 3:
            self.photo_image = PhotoImage(file=dir_img+'Platform_03.png')


        self.image = game.canvas.create_image(
            x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x+width, y+height)


class ExitDoorSprite(Sprite):
    """
    # 탈출문[40x35]은 1개이므로 한개 속성만 사용 - 좌표xy, 넓이,높이
    """
    def __init__(self, game, x, y, width, height):
        super().__init__(game)
        self.photo_image = PhotoImage(file=dir_img + "door_01.png")
        self.image = game.canvas. \
                create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (width / 2), y + height)
        self.endgame = True


class StickManSprite(Sprite):
    """
    # 스틱맨[27x30]은 1개이므로 한개 속성만 사용 - 좌표xy, 넓이,높이
    """
    def __init__(self, game, x, y, width, height):
        super().__init__(game)
        (self.width, self.height) = (width, height)        # 추가
        self.images_left = [PhotoImage(file=dir_img + "sman_01.png"),
                            PhotoImage(file=dir_img + "sman_02.png"),
                            PhotoImage(file=dir_img + "sman_03.png"),
                            ]

        self.images_right = [PhotoImage(file=dir_img + "sman_04.png"),
                             PhotoImage(file=dir_img + "sman_05.png"),
                             PhotoImage(file=dir_img + "sman_06.png"),
                             ]

        self.image = game.canvas. \
                create_image(x, y, image=self.images_left[0], anchor='nw')
        (self.x, self.y) = (0, 0)         # -2  .. x 방향 움직임 초기값
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def coords(self):
        # 스틱맨은 항상 움직이기 때문에 최신좌표가 필요함  ...  최신좌표값 리턴
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + self.width     # 27
        self.coordinates.y2 = xy[1] + self.height    # 30
        return self.coordinates

    def move(self):
        # 어떤 동작이던지, 가능하다 (초기화)
        falling = True
        left, right, top, bottom = True, True, True, True

        # 스틱맨 애니메이션 실행
        self.animate()

        # 첨프를 시작하면(-4) 점프카운트를 증가시킨다.
        if self.y < 0:
            self.jump_count += 1

            # 점프카운트가 20보다 크면 떨어지는 뱡향(+4)으로 전환된다.
            if self.jump_count > JUMP_DURATION:
                self.y = VERT_MOVE

        # 추락방향이면 점프카운트를 감소시킨다 (from 20)
        if self.y > 0:
            self.jump_count -= 1

        co = self.coords()  # 최신좌표값 co = self.coordinates(x1, y1, x2, y2)

        # 아래 방향으로 갈 수 없음 (y=0)
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False

        # 윗 방향으로 갈 수 없음 (y=0)
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        # 오른 쪽으로 갈 수 없음 (x=0)
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False

        # 왼 쪽으로 갈 수 없음 (x=0)
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False

        for sprite in self.game.sprites:
            # 스프라이트가 '스틱맨' 이면 'Skip' 한다
            if sprite == self:
                continue

            # 정지된 오브젝트의 '좌표'를 가져온다  ...  sprite_co
            sprite_co = sprite.coords()

            if top and self.y < 0 and self.collided_top(co, sprite_co):
                self.y = -self.y
                top = False

            if bottom and self.y > 0 and self.collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False

            # ??(y=0), y2가 바닥에 닿았고, 바닥에 충돌했다면 = 추락 STOP!
            if bottom and falling and self.y == 0 \
                    and co.y2 < self.game.canvas_height \
                    and self.collided_bottom(1, co, sprite_co):
                falling = False

            # 왼쪽으로 가는데(x<0), 왼쪽벽에 충돌하면 = 왼쪽 STOP!
            if left and self.x < 0 and self.collided_left(co, sprite_co):
                # self.x = 0
                left = False
                if sprite.endgame:
                    self.game.running = False

            # 오른쪽으로 가는데(x>0), 오른쪽벽에 충돌하면 = 오른쪽 STOP!
            if right and self.x > 0 and self.collided_right(co, sprite_co):
                # self.x = 0
                right = False
                if sprite.endgame:
                    self.game.running = False

            # 점프 할 경우 : (추락가능, 아래가능) y2가 바닥에 닿지 않았다면, 점프!
            if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
                self.y = VERT_MOVE

            self.game.canvas.move(self.image, self.x, self.y)



    def animate(self):
        # 스틱맨을 달리게 하는 애니메이션 동작
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add

                if self.current_image >= 2:
                    self.current_image_add = -1

                if self.current_image <= 0:
                    self.current_image_add = +1

        # 왼쪽으로 움직이면, 이미지는 왼쪽 방향
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_left[self.current_image])

        # 오른쪽으로 움직이면, 이미지는 오른쪽 방향
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(
                    self.image, image=self.images_right[self.current_image])

    def turn_right(self, evt):      # 키 바인딩을 위한 핼퍼()
        if self.y == 0:
            self.x = HORZ_MOVE

    def turn_left(self, evt):       # 키 바인딩 위한 핼퍼()
        if self.y == 0:
            self.x = -HORZ_MOVE

    def jump(self, evt):            # 키 바인딩 위한 핼퍼()
        if self.y == 0:
            # 첨프(-)/ 추락(+) 상태가 아니면 점프(-)방향으로 바꾸고, 카운터 초기화
            # 한번 점프에 카운터는 20을 센다 (총 4x20=80px 높이를 점프)
            self.y = -VERT_MOVE
            self.jump_count = 0

    def within_x(self, co1, co2):     # 핼퍼()
        if (co1.x1 > co2.x1 and co1.y1 < co2.x2) or \
           (co1.x2 > co2.y1 and co1.x2 < co2.x2) or \
           (co2.x1 > co1.y1 and co2.x1 < co1.x2) or \
           (co2.x2 > co1.y1 and co2.x2 < co1.x1):
            return True
        else:
            return False

    def within_y(self, co1, co2):     # 핼퍼()
        if (co1.y1 > co2.y1 and co1.y1 < co2.y2) or \
           (co1.y2 > co2.y1 and co1.y2 < co2.y2) or \
           (co2.y1 > co1.y1 and co2.y1 < co1.y2) or \
           (co2.y2 > co1.y1 and co2.y2 < co1.y1):
            return True
        else:
            return False

    def collided_left(self, co1, co2):
        if self.within_y(co1, co2):
            # obj.1의 왼쪽귀퉁이(x1)가, obj.2 x1~x2 범위 안에 들어왔다.
            if co2.x1 <= co1.x1 <= co2.x2:
                return True
        return False

    def collided_right(self, co1, co2):
        if self.within_y(co1, co2):
            # obj.1의 오른쪽 귀퉁이(x2)가, obj.2 x1~x2 범위 안에 들어왔다.
            if co2.x1 <= co1.x2 <= co2.x2:
                return True
        return False

    def collided_top(self, co1, co2):
        if self.within_x(co1, co2):
            # obj.1의 위쪽 귀퉁이(y1)가, obj.2 y1~y2 범위 안에 들어왔다.
            if co2.y1 <= co1.y1 <= co2.y2:
                return True
        return False

    def collided_bottom(self, y, co1, co2):
        # y=움직이는 방향
        if self.within_x(co1, co2):
            y_calc = co1.y2 + y
            # obj.1 아랫쪽 귀퉁이(y2)+움직임(y)이 obj.2 y1~y2 범위 안에 들어왔다.
            # y = 아랫쪽으로 떨어지는 움직임, 또는 점프로 위로 움직이는 움직임
            if co2.y1 <= y_calc <= co2.y2:
                return True
        return False
