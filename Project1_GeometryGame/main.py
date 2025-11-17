import turtle
from turtle import Turtle

from Project1_GeometryGame.Point import GuiPoint
from Rectangle import GuiRect
from Point import Point
from random import randint

lower_coord = (Point(randint(0,200),(randint(0,200))))
upper_coord = (Point(randint(201,400), (randint(201,400))))

print(f"Rectangle coordinates: \n({lower_coord.x}, {lower_coord.y}) and ({upper_coord.x}, {upper_coord.y})")

rectanglex = GuiRect(lower_coord, upper_coord)
print(f"The area of the rectangle is:  {rectanglex.calculate_area()}")
point1 = GuiPoint(float(input("Enter x value: ")), float(input("Enter y value: ")))

msg = "The Point falls inside the rectangle" if point1.falls_in_rectangle(rectanglex) \
        else "The Point do not fall inside the rectangle"

print(msg)

my_turtle = Turtle()
rectanglex.draw_rectangle(my_turtle)
point1.draw_point(my_turtle)
turtle.done()
