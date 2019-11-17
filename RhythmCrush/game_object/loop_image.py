from RhythmCrush.interface.Interface import IUpdatableObject, IDrawableObject
from RhythmCrush.utill.image_manager import *
from RhythmCrush.utill.ResourceData import *


class HorizontalLoopImage(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, w, h, image_tag, speed_x):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed_x = speed_x
        self.image_contoler = get_image_controller(image_tag)

        self.t = 0;

    def load(self):
        pass

    def update(self, delta_time):
        speedRatio = self.speed_x / 1000.0
        img_w = self.image_contoler.image.w + ((speedRatio - 1.0)/2)
        self.t += self.speed_x * delta_time
        if self.t > img_w:
            self.t -= img_w

    def draw(self):
        speedRatio = self.speed_x / 1000.0
        img_w = self.image_contoler.image.w + ((speedRatio - 1.0)/2)
        img_h = self.image_contoler.image.h
        self.image_contoler.draw(self.x - self.t, self.y, img_w, img_h)
        self.image_contoler.draw(self.x - self.t + img_w, self.y, img_w, img_h)
        self.image_contoler.draw(self.x - self.t - img_w, self.y, img_w, img_h)

    def set_speed(self,speed):
        self.speed_x = speed