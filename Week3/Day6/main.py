from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake")
screen.tracer(0)

screen.listen()

snake = Snake()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()