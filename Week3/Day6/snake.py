from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40,0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_body(position)

    def add_snake_body(self, pos):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(pos)
        self.snakes.append(snake_body)

    def extend_snake(self):
        self.add_snake_body(self.snakes[-1].position())

    def move_snake(self):
        for a in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[a - 1].xcor()
            new_y = self.snakes[a - 1].ycor()
            self.snakes[a].goto(new_x, new_y)
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)