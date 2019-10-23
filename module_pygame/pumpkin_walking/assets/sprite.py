"""
# ./assets/sprite.py - class MySprite(pygame.sprite.Sprite)
"""
print(__doc__)

import pygame
from assets.config import WINDOW_SIZE, START_POS, dir_images


class MySprite(pygame.sprite.Sprite):
    """
    # pygame Sprite 속성을 상속 받는다
    """
    def __init__(self):
        """ make image array & make rect """
        super(MySprite, self).__init__()
        # adding all the images to sprite array
        self.images = [pygame.image.load(dir_images+f"walk_{i+1:02d}.png")
                        for i in range(10)]
        self.index = 0
        self.image = pygame.transform \
                            .smoothscale(self.images[self.index], WINDOW_SIZE)
        self.rect = self.image.get_rect()
        self.rect.topleft = START_POS

        # self.rect = pygame.Rect(
        #         50,            # left=50,
        #         100,           # top=100,
        #         80,            # width=150,
        #         90,            # height=198,
        #     )

    def update(self):
        """ image update when it is called """
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
