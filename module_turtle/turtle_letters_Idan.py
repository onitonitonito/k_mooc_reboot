"""
# Draw Letters In Turtle
# https://stackoverflow.com/questions/43689387/draw-letters-in-turtle
"""
# [IMPORTANT] : CHECK! How to colntol
#  - stting the window size
#  - giving a scale to the letters

print(__doc__)

# from turtle import (Turtle, Screen,)
import turtle

NAME = "IDAN"
BORDER = 2
BOX_WIDTH, BOX_HEIGHT = 6, 10  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size

def letter_A(turtle):
    turtle.forward(HEIGHT / 2)
    for _ in range(3):
        turtle.forward(HEIGHT / 2)
        turtle.right(90)
        turtle.forward(WIDTH)
        turtle.right(90)
    turtle.forward(HEIGHT)

def letter_D(turtle):
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.circle(-HEIGHT / 2, 180, 30)

def letter_I(turtle):
    turtle.right(90)
    turtle.forward(WIDTH)
    turtle.backward(WIDTH / 2)
    turtle.left(90)
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.backward(WIDTH / 2)
    turtle.forward(WIDTH)

def letter_N(turtle):
    turtle.forward(HEIGHT)
    turtle.goto(turtle.xcor() + WIDTH, BORDER)
    turtle.forward(HEIGHT)

LETTERS = {'A': letter_A, 'D': letter_D, 'I': letter_I, 'N': letter_N}

window = turtle.Screen()
window.setup(200, 100)  # arbitrarly set the screen size, you can
window.title("Turtle writing my name: {}".format(NAME))
window.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = turtle.Turtle()

for i, letter in enumerate(NAME):
    marker.penup()
    marker.goto(i * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

window.mainloop()
