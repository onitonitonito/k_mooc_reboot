# This script should be converted for Py/3.6 (this is for py/2.x)
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

HEIGHT = 9; WIDTH = 9          #  FIELD_SIZE = Snake movement of the site ( length and width )
FIELD_SIZE = HEIGHT * WIDTH
HEAD = 0    # Snake head is always located in the first element of the snake array

# Used to represent the number of different things, because the matrix will be processed on each grid to reach the path length of the food,
# So there is a need for a large enough interval between these three variables ( > HEIGHT * WIDTH)
FOOD = 0
UNDEFINED = (HEIGHT + 1) * (WIDTH + 1)
SNAKE = 2 * UNDEFINED

# Because snake is a one-dimensional array, so the corresponding element directly with the following values ​​that move in four directions
LEFT = -1; RIGHT = 1; UP = -WIDTH; DOWN = WIDTH
ERR = -1111   # Err Code

# Use one-dimensional arrays to represent two-dimensional things
# line 0, HEIGHT line / Column 0, WIDTH line were listed as fence, not available
board = [0] * FIELD_SIZE        # Maximum Board[].arry lenth   = (FIELD_SIZE) : # Board indicates the rectangular space of the snake movement
snake = [0] * (FIELD_SIZE+1)    # Maximum Snake[].array length = (FIELD_SIZE + 1)
snake[HEAD] = 1*WIDTH+1         # The initial snake POSITION= (1,1) : calculated
snake_size = 1                  # The initial snake length is 1
# The temporary variable corresponding to the above variable is used when the snake is tentatively moved
tmpboard = [0] * FIELD_SIZE
tmpsnake = [0] * (FIELD_SIZE+1)
tmpsnake[HEAD] = 1*WIDTH+1
tmpsnake_size = 1

food = 3 * WIDTH + 3            # Food: initial (3,3) : food location (0 ~ FIELD_SIZE-1)
best_move = ERR                 # Best_move: movement direction

mov = [LEFT, RIGHT, UP, DOWN]   # Motion direction array
key = KEY_RIGHT                 # Received keys and scores
score = 1                       # Score also means snake long

# Check whether a cell has been covered by the snake, no coverage was free, return true
def is_cell_free(idx, psize, psnake):
    return not (idx in psnake[:psize])

# Check whether a position idx can move in the move direction
def is_move_possible(idx, move):
    flag = False
    if move == LEFT:
        flag = True if idx%WIDTH > 1 else False
    elif move == RIGHT:
        flag = True if idx%WIDTH < (WIDTH-2) else False
    elif move == UP:
        flag = True if idx > (2*WIDTH-1) else False # that is idx/WIDTH > 1
    elif move == DOWN:
        flag = True if idx < (FIELD_SIZE-2*WIDTH) else False # that is idx/WIDTH < HEIGHT-2
    return flag
# Reset the board
# Board_refresh, UNDEFINED value has become the path to reach the food length
# If you want to restore, reset it
def board_reset(psnake, psize, pboard):
    for i in range(FIELD_SIZE):
        if i == food:
            pboard[i] = FOOD
        elif is_cell_free(i, psize, psnake): # The location is empty
            pboard[i] = UNDEFINED
        else:                                # The position is snake
            pboard[i] = SNAKE

# Breadth first search traverse the entire board,
# Calculate the path length of each non-SNAKE element on the board to reach the food
def board_refresh(pfood, psnake, pboard):
    queue = []
    queue.append(pfood)
    inqueue = [0] * FIELD_SIZE
    found = False
    # After the end of the cycle, in addition to the snake\'s body,
    # The numeric code in each of the other chunks from its path to the length of the food
    while len(queue)!=0:
        idx = queue.pop(0)
        if inqueue[idx] == 1: continue
        inqueue[idx] = 1
        for i in range(4):
            if is_move_possible(idx, mov[i]):
                if idx + mov[i] == psnake[HEAD]:
                    found = True
                if pboard[idx+mov[i]] < SNAKE: # if the point is not the snake's body

                    if pboard[idx+mov[i]] > pboard[idx]+1:
                        pboard[idx+mov[i]] = pboard[idx] + 1
                    if inqueue[idx+mov[i]] == 0:
                        queue.append(idx+mov[i])
    return found

# From the snake head, according to the board element value,
# Select the shortest path from 4 field points around the snake head
def choose_shortest_safe_move(psnake, pboard):
    best_move = ERR
    min = SNAKE
    for i in range(4):
        if is_move_possible(psnake[HEAD], mov[i]) and pboard[psnake[HEAD]+mov[i]]<min:
            min = pboard[psnake[HEAD]+mov[i]]
            best_move = mov[i]
    return best_move

# From the snake head, according to the board element value,
# Select the farthest path from the 4 field points around the snakehead
def choose_longest_safe_move(psnake, pboard):
    best_move = ERR
    max = -1
    for i in range(4):
        if is_move_possible(psnake[HEAD], mov[i]) and pboard[psnake[HEAD]+mov[i]]<UNDEFINED and pboard[psnake[HEAD]+mov[i]]>max:
            max = pboard[psnake[HEAD]+mov[i]]
            best_move = mov[i]
    return best_move

# Check whether you can chase the snake tail movement, that is, between the snakehead and snake tail is a path
# To avoid the snake head into a dead end
# Virtual operation, in tmpboard, tmpsnake carried out
def is_tail_inside():
    global tmpboard, tmpsnake, food, tmpsnake_size
    tmpboard[tmpsnake[tmpsnake_size-1]] = 0 # virtual to snake into food (because it is virtual, so in tmpsnake, tmpboard)
    tmpboard[food] = SNAKE # place the place where the food is placed as a snake
    result = board_refresh(tmpsnake[tmpsnake_size-1], tmpsnake, tmpboard) # Find the path length for each position to snake
    for i in range(4): # if the snake head and snake tail next to, then return False. That can not follow_tail, chasing snake tail movement
        if is_move_possible(tmpsnake[HEAD], mov[i]) and tmpsnake[HEAD]+mov[i]==tmpsnake[tmpsnake_size-1] and tmpsnake_size>3:
            result = False
    return result

# Let the snake head run a step toward the snake tail
# Regardless of the snake, the direction of the snake tail
def follow_tail():
    global tmpboard, tmpsnake, food, tmpsnake_size
    tmpsnake_size = snake_size
    tmpsnake = snake[:]
    board_reset(tmpsnake, tmpsnake_size, tmpboard) # reset virtual board
    tmpboard[tmpsnake[tmpsnake_size-1]] = FOOD # Let the snake become food
    tmpboard[food] = SNAKE  # Let the food place into a snake
    board_refresh(tmpsnake[tmpsnake_size-1], tmpsnake, tmpboard) # Find the path length of each location
    tmpboard[tmpsnake[tmpsnake_size-1]] = SNAKE # Restore snake tail

    return choose_longest_safe_move(tmpsnake, tmpboard) # return to the running direction (let snake head movement 1 step)

# In a variety of programs are not, casually find a feasible direction to go (1 step),
def any_possible_move():
    global food , snake, snake_size, board
    best_move = ERR
    board_reset(snake, snake_size, board)
    board_refresh(food, snake, board)
    min = SNAKE

    for i in range(4):
        if is_move_possible(snake[HEAD], mov[i]) and board[snake[HEAD]+mov[i]]<min:
            min = board[snake[HEAD]+mov[i]]
            best_move = mov[i]
    return best_move

def shift_array(arr, size):
    for i in range(size, 0, -1):
        arr[i] = arr[i-1]

def new_food():
    global food, snake_size
    cell_free = False
    while not cell_free:
        w = randint(1, WIDTH-2)
        h = randint(1, HEIGHT-2)
        food = h * WIDTH + w
        cell_free = is_cell_free(food, snake_size, snake)
    win.addch(int(food/WIDTH)+1, food%WIDTH, '@')       # Screen's disturbed, so int()+1s were added

# True snake in this function, towards pbest_move take a step
def make_move(pbest_move):
    global key, snake, board, snake_size, score
    shift_array(snake, snake_size)
    snake[HEAD] += pbest_move

    # By esc exit, getch while ensuring the fluency of the drawing, without it will only see the final result
    win.timeout(10)
    event = win.getch()
    key = key if event == -1 else event
    if key == 27: return

    p = snake[HEAD]
    win.addch(int(p/WIDTH)+1, p%WIDTH, '*')

    # If the newly added snake head is the location of the food
    # Snake plus 1, generate new food, reset the board (because the original path length has not been used)
    if snake[HEAD] == food:
        board[snake[HEAD]] = SNAKE  # new snake head
        snake_size += 1
        score += 1
        if snake_size < FIELD_SIZE: new_food()
    else: # If the newly added snake head is not the place of food
        board[snake[HEAD]] = SNAKE              # new snake head
        board[snake[snake_size]] = UNDEFINED    # Snake becomes a space
        win.addch(int(snake[snake_size]/WIDTH)+1, snake[snake_size]%WIDTH, ' ')

# Virtual operation once, and then check the operation at the call to check whether this feasible
# Viable operation.
# Virtual run after eating the food, get the virtual snake on the board position
def virtual_shortest_move():
    global snake, board, snake_size, tmpsnake, tmpboard, tmpsnake_size, food
    tmpsnake_size = snake_size
    tmpsnake = snake[:] # If direct tmpsnake = snake, both point to the same memory
    tmpboard = board[:] # board is already the location of the path to reach the length of the food, and no longer calculate
    board_reset(tmpsnake, tmpsnake_size, tmpboard)

    food_eated = False
    while not food_eated:
        board_refresh(food, tmpsnake, tmpboard)
        move = choose_shortest_safe_move(tmpsnake, tmpboard)
        shift_array(tmpsnake, tmpsnake_size)
        tmpsnake[HEAD] += move # Add a new position to the snake head
        # If the newly added snake head is just the location of the food
        # The length plus 1, reset the board, the food that position becomes part of the snake (SNAKE)
        if tmpsnake[HEAD] == food:
            tmpsnake_size += 1
            board_reset(tmpsnake, tmpsnake_size, tmpboard) # After the virtual run, the snake at the board position
            tmpboard[food] = SNAKE
            food_eated = True
        else:  # If the snakehead is not the location of the food, the new position is snakehead and the last one becomes a space
            tmpboard[tmpsnake[HEAD]] = SNAKE
            tmpboard[tmpsnake[tmpsnake_size]] = UNDEFINED

# If there is a path between the snake and the food, call this function
def find_safe_way():
    global snake, board
    safe_move = ERR
    # Fictitiously run once, since there is a path between the snake and the food, so it is effective
    # After running the virtual snake in the board to get the location, that is, tmpboard, see label101010
    virtual_shortest_move() # The function is the only call
    if is_tail_inside(): # If the virtual operation, the snakehead between the snake has a path, then select the shortest path to run (1 step)
        return choose_shortest_safe_move(snake, board)
    safe_move = follow_tail() # otherwise virtual follow_tail 1 step, if it can do, return true
    return safe_move


curses.initscr()
win = curses.newwin(HEIGHT, WIDTH, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
win.addch(int(food/WIDTH)+1, food%WIDTH, '@')    #Err.corr ='integer arugument expected, go float'


while key != 27:        # 27 = '<-'
    win.border(0)
    win.addstr(0, 1, 'S: %-d '%score)
    win.timeout(10)
    # Receive keyboard input, but also make the display smooth
    event = win.getch()
    key = key if event == -1 else event

    # Reset the matrix
    board_reset(snake, snake_size, board)

    # If the snake can eat food, board_refresh returns true
    # And the board is in addition to the snake (= SNAKE), the other
    # element values ​​represent the shortest path length from that point to the food
    if board_refresh(food, snake, board):
        best_move  = find_safe_way() # find_safe_way only call
    else:
        best_move = follow_tail()

    if best_move == ERR:
        best_move = any_possible_move()
    # Above a thought, only to draw a direction, run one step
    if best_move != ERR: make_move(best_move)
    else: break

curses.endwin()

print("\nScore - " + str(score))
