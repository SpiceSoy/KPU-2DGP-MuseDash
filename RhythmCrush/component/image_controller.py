import pico2d
from ..interface import IUpdatableObject
from ..component.animation import Animator


class ImageController(IUpdatableObject):
    def __init__(self, image: pico2d.Image):
        self.animator = None
        self.speed = 1
        self.image = image

    def add_animator(self, animator: Animator):
        self.animator = animator

    def get_frame(self, index):
        return self.frame_buffer[index]

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def draw(self, x, y, w=None, h=None):
        if self.animator is None:
            self.image.draw(x, y, w, h)
        else:
            frame = self.animator.get_current_sub_animation()
            self.image.clip_draw(frame[0], frame[1], frame[2], frame[3], x, y, w, h)

    def composite_draw(self, rad, flip, x, y, w=None, h=None):
        if self.animator is None:
            self.image.composite_draw(rad, flip, x, y, w, h)
        else:
            frame = self.animator.get_current_sub_animation()
            self.image.composite_draw(rad, flip, frame[0], frame[1], frame[2], frame[3], x, y, w, h)

    def update(self, delta_time):
        if self.animator is not None:
            self.animator.update(delta_time * self.speed)
