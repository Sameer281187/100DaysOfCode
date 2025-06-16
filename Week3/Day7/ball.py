from turtle import Turtle

class Ball(Turtle):
    new_xcor = 0
    new_ycor = 0
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        self.new_xcor = self.xcor() + self.x_move
        self.new_ycor = self.ycor() + self.y_move
        self.goto(self.new_xcor, self.new_ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1