import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2, 0)
            new_car.setheading(180)
            new_car.goto(300,random.randrange(-250, 250))
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
