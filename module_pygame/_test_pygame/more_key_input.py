"""
# PyGame Tutorial: More on Input
# https://nerdparadise.com/programming/pygame/part6
#
# - pygame.key.get_pressed()
# - pygame.mouse.get_pos()
# - pygame.mouse.get_pressed()
#
"""
# pygame.key.get_pressed()
# - will get a list of booleans that describes the state of each keyboard key.
# The value of the key constant (such as pygame.K_TAB)
# can be used as the index into this giant list. Therefore
# pygame.key.get_pressed()[pygame.K_TAB] is an expression that is true when
# the tab key is pressed.
#
# pygame.mouse.get_pos()
# - returns the coordinates of the mouse cursor. Will return (0, 0) if
# the mouse hasn't moved over the screen yet.
#
# pygame.mouse.get_pressed()
# - like pygame.key.get_pressed(), returns the state of each mouse button.
# The value returned is a tuple of size 3 that corresponds to the left,
# middle, and right buttons.
print(__doc__)

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    (x,y) = (0,0)

    mode = 'blue'
    points = []

    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)

                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            draw_line_between(screen, i, points[i], points[i + 1], radius, mode)
            i += 1

        pygame.display.flip()

        clock.tick(60)

def draw_line_between(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)



if __name__ == '__main__':
    main()
