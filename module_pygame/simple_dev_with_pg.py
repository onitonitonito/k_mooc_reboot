"""
# Game development with Pygame - Python Tutorial
# https://pythonspot.com/game-development-with-pygame/
"""
# initialize()
# while running():
#    game_logic()
#    get_input()
#    update_screen()
# deinitialize()

import pygame
from pygame.locals import *

class MyApp(object):
    posXY = (10, 10)
    winSize = (640, 480)
    filename_img = "statics\\pygame.png"

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.winSize, pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load(self.filename_img).convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._image_surf, self.posXY)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()




if __name__ == "__main__" :
    ma = MyApp()
    ma.on_execute()
