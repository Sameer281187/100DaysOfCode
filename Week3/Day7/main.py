import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PADDLE_RIGHT_POSITION = (350, 0)
PADDLE_LEFT_POSITION = (-350, 0)
PLAYER_RIGHT_SCORE_POSITION = (100, 200)
PLAYER_LEFT_SCORE_POSITION = (-100, 200)

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong game")
screen.tracer(0)

screen.listen()

right_paddle = Paddle(PADDLE_RIGHT_POSITION)
left_paddle = Paddle(PADDLE_LEFT_POSITION)
ball = Ball()
right_player_score = Scoreboard(PLAYER_RIGHT_SCORE_POSITION)
left_player_score = Scoreboard(PLAYER_LEFT_SCORE_POSITION)

screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

x_fac = 1
y_fac = 1

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #Detect collision with the top/ bottom walls and bounce the ball off them
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddles and bounce the ball off them
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if the ball goes out of bounds then stop the game
    if ball.xcor() > 400:
        ball.reset_position()
        left_player_score.score_update()

    if ball.xcor() < -400:
        ball.reset_position()
        right_player_score.score_update()


screen.exitonclick()