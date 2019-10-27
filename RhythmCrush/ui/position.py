import math


class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def scale(self):
        return math.sqrt(self.scale_sqare())

    def scale_square(self):
        return self.x * self.x + self.y * self.y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other):
        self.x *= other
        self.y *= other

    def __truediv__(self, other):
        self.x /= other
        self.y /= other

