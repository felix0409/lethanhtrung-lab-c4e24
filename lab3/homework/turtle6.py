from turtle import *
from random import randint

def draw_star(x, y, length):
        setpos(x, y)
        for i in range(5):
                forward(length)
                left(144)
                
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    color(R, G, B)

speed(0)
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    change_color()
    draw_star(x, y, length)

exitonclick()
mainloop()