"""
# 스틱맨 대쉬 : StickMan Dash!
# TkInter 모듈을 사용하여 게임을 제작하며, 클래스 오브젝트의 '상관관계'를 이해 한다.
# 12 개의 오브젝트를 사용한다. (바닥판 10개, 나가는 문 1개, 스틱맨 1개)
"""
#  - Game(object)   : 모든 오브젝트의 바탕, Tkinter 모듈로 메인'윈도우'를 만든다
#  - Coords(object) : 스프라이트의 2점 좌표를 생성하여 충돌여부 판단
#  - Sprite(object) : 모든 스프라이트의 '상속'의 기본 '모체'가 된다.
#  - ExitDoorSprite(Sprite) : 나가는 문, 스프라이트 객체
#  - PlatformSprite(Sprite) : 바닥판 스프라이트 객체
#  - StickManSprite(Sprite) : 움직이는 스틱맨 스프라이트 객체

import assets.script_run

from assets.config import *
from assets.class_object import (
                        Game, Coords, Sprite,
                        ExitDoorSprite,         # Inherit 'Sprite'
                        PlatformSprite,         # Inherit 'Sprite'
                        StickManSprite,         # Inherit 'Sprite'
                        )

def main():
    # 게임 오브젝트 '선언' - tkinter 게임 윈도우 생성
    game = Game()

    # 스프라이트 오브젝트를 선언한다 --> game.sprites 에 추가한다.
    sprites = [
            #                 바종류, x,  y,  width, height
            PlatformSprite(game, 2,  45,  60, 114, 13),
            PlatformSprite(game, 2, 170, 120, 114, 13),
            PlatformSprite(game, 3, 300, 160, 147, 13),
            PlatformSprite(game, 1, 230, 200,  75, 13),
            PlatformSprite(game, 1, 170, 250,  75, 13),
            PlatformSprite(game, 2,  50, 300, 114, 13),
            PlatformSprite(game, 2, 175, 350, 114, 13),
            PlatformSprite(game, 3, 300, 400, 147, 13),
            PlatformSprite(game, 3, 150, 440, 147, 13),
            PlatformSprite(game, 3,   0, 480, 147, 13),

            #                     x,    y,  width, height
            ExitDoorSprite(game, 10,  0,   45, 65),
            StickManSprite(game, 470, 500, 45, 55),
        ]

    # 사전 작업으로, 12 개의 스프라이트 오브젝트를 game.sprites '리스트'에 추가 한다.
    # 정지 된 오브젝트 = 10+1, 움직이는 오브젝트 = 1개 (스틱맨)
    game.sprites.extend(sprites)
    game.mainloop()


if __name__ == '__main__':
    main()
