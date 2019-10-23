"""
# for TEST : StickMan
"""

import assets.script_run
from tkinter import Tk

from assets.config import *
from assets.class_object import (
                        Game, Coords, Sprite,
                        ExitDoorSprite,         # Inherit 'Sprite'
                        PlatformSprite,         # Inherit 'Sprite'
                        StickManSprite,         # Inherit 'Sprite'
                        )

print(__doc__)

if __name__ == '__main__':

    game = Game()

    sprites = [
        #                 바종류, x,  y,  width, height
        PlatformSprite(game, 1,  30, 410,   75,  13),
        PlatformSprite(game, 2, 120, 450,  114,  13),
        PlatformSprite(game, 3, 250, 490,  147,  13),

        #                     x,    y,  width, height
        ExitDoorSprite(game,  10,   0,   45,   65),
        StickManSprite(game, 470, 500,   45,   55),

        ]
    game.sprites.extend(sprites)
    game.mainloop()
