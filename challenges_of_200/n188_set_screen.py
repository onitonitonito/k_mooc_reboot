import pygame
''' Just show black pad screen
        - the first preparation of shooting gamepad.
        - only gamepad, caption, main_loop were suggested.
'''

# Global vari.
BLACK = (0, 0, 0)
PAD_WIDTH = 480
PAD_HEIGHT = 640

# main function
def run_game():
    global gamepad, clock
    done_flag = False

    while not done_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done_flag = True

        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def init_game():
    global gamepad, clock

    pygame.init()

    gamepad = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
    pygame.display.set_caption('My GALAXTICA~!!')
    clock = pygame.time.Clock()


init_game()
run_game()
