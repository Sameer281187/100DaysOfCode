from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()
ts = timmy.getscreen()
ts.bgcolor("white")
for i in range(25):
    if i % 2 == 0:
        timmy.pendown()
    else:
        timmy.penup()
    timmy.forward(10)












screen.exitonclick()







