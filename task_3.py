from random import randint
from turtle import *
import turtle

t = turtle.Turtle()

t.speed("fast")


STEP = 30
MOUNT = [0, 10, 100, 150, 60, 20, 0, 20, 40, 60, 20, 10, 0]
for i in range(len(MOUNT)):
    if MOUNT[i]==0:
        goto(i * STEP,MOUNT[i])
        continue
    goto(i * STEP, MOUNT[i] + randint(0,20))

t.home
t.forward(400)


exitonclick
