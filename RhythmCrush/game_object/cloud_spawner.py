import random

from ..interface import IUpdatableObject, IDrawableObject
from RhythmCrush.game_object.cloud_object import Cloud

class CloudSpawner(IUpdatableObject, IDrawableObject):
    def __init__(self, game_world, x=1440, y_min=500, y_max=750, speed_min=0.9, speed_max=1.3, delay_min=0.7, delay_max=1.6):
        self.x = x
        self.y_min = y_min
        self.y_max = y_max
        self.speed_min = speed_min
        self.speed_max = speed_max
        self.game_world = game_world
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.timer = self.get_new_delay()

    def load(self):
        pass

    def draw(self):
        pass

    def update(self, delta_time):
        self.timer -= delta_time
        if self.timer < 0:
            self.timer = self.get_new_delay()
            self.game_world.add_object(Cloud(self.x, self.get_new_y(), self.game_world, self.get_new_speed()), 2)

    def get_new_delay(self):
        return random.random() * (self.delay_max - self.delay_min) + self.delay_min

    def get_new_speed(self):
        return random.random() * (self.speed_max - self.speed_min) + self.speed_min

    def get_new_y(self):
        return random.randint(self.y_min, self.y_max)
