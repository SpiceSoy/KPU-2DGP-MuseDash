import math


class Vec2D:
    @staticmethod
    def scale(target):
        return math.sqrt(Vec2D.scale_square(target))

    @staticmethod
    def scale_square(target):
        return target[0] * target[0] + target[1] * target[1]

    @staticmethod
    def add(target_a, target_b):
        return target_a[0] + target_b[0], target_a[1] + target_b[1]

    @staticmethod
    def sub(target_a, target_b):
        return target_a[0] - target_b[0], target_a[1] - target_b[1]

    @staticmethod
    def mul(target_a, scalar):
        return target_a[0] * scalar, target_a[1] * scalar

    @staticmethod
    def div(target_a, scalar):
        return target_a[0] / scalar, target_a[1] / scalar

