
import turtle as tu
""" n is the size parameter, the shown tree is for n=50.
Takes a minute or two to draw. (this is fastest mode of TURTLE)
refer to SOF(StackOverFlow) Here: https://goo.gl/ZnN7Sh
"""

# n = int(input('n= : '))*1.0
n = 50

tu.speed("fastest")
tu.left(90)
tu.forward(3*n)
tu.color("orange", "yellow")
tu.begin_fill()
tu.left(126)
for i in range(5):
    tu.forward(n/5)
    tu.right(144)
    tu.forward(n/5)
    tu.left(72)
tu.end_fill()
tu.right(126)

tu.color("dark green")
tu.backward(n*4.8)

def tree(d, s):
    if d <= 0: return
    tu.forward(s)
    tree(d-1, s*.8)
    tu.right(120)
    tree(d-3, s*.5)
    tu.right(120)
    tree(d-3, s*.5)
    tu.right(120)
    tu.backward(s)
tree(15, n)
tu.backward(n/2)

import time
time.sleep(60)
