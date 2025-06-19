from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake")
time.sleep(5)
screen.tracer(0)

screen.listen()

snake = Snake()
food = Food()
score = ScoreBoard()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend_snake()
        score.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset_snake()

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset_snake()

screen.exitonclick()