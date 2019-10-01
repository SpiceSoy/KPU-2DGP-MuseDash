import pico2d

from Interface.Interface import IUpdatableObject
from Interface.Interface import IDrawableObject

#이미지 로드 할때 오픈 캔버스 하고 하기

class Note(IUpdatableObject,IDrawableObject):
    def __init__(self, x, y, time, type, hit_sound, extras):
        self.x = x
        self.y = y
        self.time = time
        self.type = type
        self.hit_sound = hit_sound
        self.extras = extras
        pass
    def update(self,delta_time):
        pass
    def draw(self):
        pass