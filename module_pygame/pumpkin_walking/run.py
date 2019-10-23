"""
# run.py
# ----------------
# PyGame Sprite Animation Tutorial - Simple Walk Loop
# June 8, 2018 by Belal Khan
"""
# https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/
# ?fbclid=IwAR24REc-FAR72Ymh-JPq037rdIXZKGsavVLwyDG-U5Kf8VNk0NQOmhgtUrs

import pygame
from pygame.locals import *         # 키값

from assets.config import *
from assets.sprite import MySprite

print(__doc__)

pygame.init()

def main():
    """
    # for test
    # <MySprite sprite(in 1 groups)> <Surface(150x198x32 SW)>
    # for sprite in my_group:
    #     print(sprite, sprite.image)
    """
    screen = pygame.display.set_mode(WINDOW_SIZE)
    print(WINDOW_SIZE)

    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        if get_index_event_key() == 0:
            exit_screen()

        screen.fill(BACKGROUND_COLOR)
        my_group.update()
        my_group.draw(screen)

        pygame.display.update()
        CLOCK.tick(FPS)

def exit_screen():
    pygame.quit()
    sys.exit()

def move_left():
    pass

def move_right():
    pass

def move_up():
    pass

def move_down():
    pass                

def get_index_event_key():
    """
    # 이벤트 키값에 대응하는 event_dict 인덱스값=0,1,2,3,4 를 반환.
    # print(event.type)   # for test ... 2-KeyDown / 3-KeyUp
    # print(event)        # for test ... event object
    """
    for event in pygame.event.get():
        event_dict = {
            'quit': [
                    (event.type == QUIT),
                    (event.type == KEYUP and event.key == K_ESCAPE), ],
            'up': [(event.type == KEYUP and event.key == K_UP), ],
            'down': [(event.type == KEYUP and event.key == K_DOWN), ],
            'left': [(event.type == KEYUP and event.key == K_LEFT), ],
            'right': [(event.type == KEYUP and event.key == K_RIGHT), ],
        }

        # show key-event on console
        for key in event_dict.keys():
            if True in [*event_dict[key]]:
                print(f'----[{key.upper()}]----')
                return list(event_dict.keys()).index(key)


if __name__ == '__main__':
    main()
