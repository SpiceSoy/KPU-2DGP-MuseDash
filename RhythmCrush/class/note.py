import pico2d

from ..interface import IUpdatableObject
from ..interface import IDrawableObject


class Note(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, time, type, hit_sound, extras):
        self.x = x
        self.y = y
        self.time = time
        self.type = type
        self.hit_sound = hit_sound
        self.extras = extras
        self.speed = 1
        pass
    def calculate_current_position(self):
        raise NotImplementedError()
        pass
    def set_note_speed(self,speed):
        self.speed = speed
    def update(self,delta_time):
        raise NotImplementedError()
        pass
    def draw(self):
        raise NotImplementedError()
        pass

class NoteMap:
    def __init__(self):
        pass
