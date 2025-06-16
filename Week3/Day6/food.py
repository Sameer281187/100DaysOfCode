from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed(0)
        self.refresh_food_location()

    def refresh_food_location(self):
        self.goto(random.randint(-260, 260), random.randint(-260, 260))