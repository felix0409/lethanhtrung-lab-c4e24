from turtle import *

def draw_star(x, y, length):
        setpos(x, y)
        for i in range(5):
                forward(length)
                left(144)
                
draw_star(0, 0, 150)
exitonclick()
mainloop()