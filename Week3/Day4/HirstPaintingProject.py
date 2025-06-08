import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('HirstDotColors.jpg', 35)
final_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    final_colors.append(new_color)


screen = Screen()
timmy = Turtle()

screen.colormode(255)
timmy.pensize(10)
timmy.speed(0)
y_cordinate = timmy.ycor()
x_cordinate = timmy.xcor()
y_cordinate -= 300
x_cordinate -= 300
timmy.penup()

for _ in range(30):
    timmy.setx(x_cordinate)
    timmy.sety(y_cordinate)
    for _ in range(30):
        timmy.color(random.choice(final_colors))
        timmy.pendown()
        timmy.forward(1)
        timmy.penup()
        timmy.forward(20)
    y_cordinate += 20

screen.exitonclick()