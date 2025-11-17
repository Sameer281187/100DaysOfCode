class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def calculate_area(self):
        length = self.point2.x - self.point1.x
        breadth = self.point2.y - self.point1.y
        return length * breadth


class GuiRect(Rectangle):

    def draw_rectangle(self, pen):
        pen.penup()
        pen.goto(self.point1.x, self.point1.y)

        pen.pendown()
        pen.goto(self.point2.x, self.point1.y)
        pen.goto(self.point2.x, self.point2.y)
        pen.goto(self.point1.x, self.point2.y)
        pen.goto(self.point1.x, self.point1.y)