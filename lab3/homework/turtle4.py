from turtle import *

shape("turtle")

def draw_square(length, colorr):
    for i in range(4):
        color(colorr)
        forward(length)
        left(90)
        
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

draw_square(100, 'red')

mainloop()