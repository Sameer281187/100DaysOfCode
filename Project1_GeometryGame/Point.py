class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x \
                and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        else:
            return False
