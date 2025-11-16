from Rectangle import Rectangle
from Point import Point
from random import randint

lower_coord = (Point(randint(0,9),(randint(0,9))))
upper_coord = (Point(randint(10,19), (randint(10,19))))

print(f"Rectangle coordinates: \n({lower_coord.x}, {lower_coord.y}) and ({upper_coord.x}, {upper_coord.y})")

rectanglex = Rectangle(lower_coord, upper_coord)
print(f"The area of the rectangle is:  {rectanglex.calculate_area()}")
point1 = Point(float(input("Enter x value: ")), float(input("Enter y value: ")))

msg = "The Point falls inside the rectangle" if point1.falls_in_rectangle(rectanglex) \
        else "The Point do not fall inside the rectangle"

print(msg)
