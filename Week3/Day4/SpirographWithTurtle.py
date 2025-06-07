import random
from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
timmy.speed(0)
gap = 5
for _ in range(360//gap):
    timmy.color(random.random(), random.random(), random.random())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + gap)
screen.exitonclick()