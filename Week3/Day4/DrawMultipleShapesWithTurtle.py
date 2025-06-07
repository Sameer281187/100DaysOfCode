from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()

for i in range(3,11):
    angle = 360/i
    timmy.color(random.random(), random.random(), random.random())
    for _ in range(i):
        timmy.forward(80)
        timmy.right(angle)





screen.exitonclick()