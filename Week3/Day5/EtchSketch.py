from turtle import Turtle, Screen, clearscreen, home

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clear_screen_and_reset_position():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkey(clear_screen_and_reset_position, "c")
screen.exitonclick()