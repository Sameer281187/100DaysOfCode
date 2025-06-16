from turtle import Turtle
Y_COR = 0
X_COR = 350
class Paddle(Turtle):
    x_coordinate = 0
    y_coordinate = 0
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        self.x_coordinate = self.xcor()
        self.y_coordinate = self.ycor()
        self.goto(self.x_coordinate, self.y_coordinate + 20)

    def move_down(self):
        self.x_coordinate = self.xcor()
        self.y_coordinate = self.ycor()
        self.goto(self.x_coordinate, self.y_coordinate - 20)
