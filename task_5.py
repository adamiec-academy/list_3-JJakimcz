from turtle import *
import turtle

t = turtle.Turtle()
wn = turtle.Screen()


STEP = 35
wn.tracer(0) 
for i in range(2):
    for x in range(360):
        forward(STEP * (x%20))
        penup
        goto(0,0)
        pendown
        left(0.5)
        
wn.update()
wn.mainloop() 
exitonclick
