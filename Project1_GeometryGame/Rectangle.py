class Rectangle:
    def __init__(self, lower_left, upper_right):
        self.lower_left = lower_left
        self.upper_right = upper_right

    def calculate_area(self):
        length = self.upper_right.x - self.lower_left.x
        breadth = self.upper_right.y - self.lower_left.y
        return length * breadth