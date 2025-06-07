import turtle
from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
timmy.shape("turtle")

for _ in range(4):
    timmy.forward(150)
    timmy.right(90)


screen.exitonclick()