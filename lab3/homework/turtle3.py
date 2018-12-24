from turtle import *

shape("turtle")

def draw_square(length, colorr):
    for i in range(4):
        color(colorr)
        forward(length)
        left(90)
        

draw_square(100, 'red')

mainloop()