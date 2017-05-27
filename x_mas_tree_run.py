from package_i.x_mas_tree import *

order_leaf = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 1000, 5000]
order_trunk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 100, 500]

for x,y in zip(order_leaf, order_trunk):
    x_mas_tree(x,y)
    time.sleep(1)


starbucks(60)
triangle(60,10)
triangle(60, 20)
trunk(60, 4)
