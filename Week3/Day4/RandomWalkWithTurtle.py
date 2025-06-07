from turtle import Turtle, Screen
import random

screen = Screen()
timmy = Turtle()

directions = {
    "right" : timmy.right,
    "left" : timmy.left
}

timmy.speed(0)
timmy.pensize(6)
for _ in range(100):
    timmy.color(random.random(), random.random(), random.random()   )
    turn_direction = random.choice(list(directions.keys()))
    timmy.forward(20)
    directions[turn_direction](random.choice([0, 90, 180, 270]))

screen.exitonclick()