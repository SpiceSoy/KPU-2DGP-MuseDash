import pico2d
from ..interface import IUpdatableObject
from ..component.animation import Animator


class ImageController(IUpdatableObject):
    def __init__(self, image: pico2d.Image):
        self.animator = None
        self.speed = 1

    def add_animator(self, animator: Animator):
        self.animator = animator

    def get_frame(self, index):
        return self.frame_buffer[index]

    def draw(self, x, y, w=None, h=None):
        if self.animator is None:
            self.image.draw(x, y, w, h)
        else:
            self.image.clip_draw(
                self.frame_buffer[self.frame_csr][0],
                self.frame_buffer[self.frame_csr][1],
                self.frame_buffer[self.frame_csr][2],
                self.frame_buffer[self.frame_csr][3],
                x, y, w, h
            )

    def composite_draw(self, rad, flip, x, y, w=None, h=None):
        if self.animator is None:
            self.image.composite_draw(rad, flip, x, y, w, h)
        else:
            self.image.clip_draw(
                rad, flip,
                self.frame_buffer[self.frame_csr][0],
                self.frame_buffer[self.frame_csr][1],
                self.frame_buffer[self.frame_csr][2],
                self.frame_buffer[self.frame_csr][3],
                x, y, w, h
            )

    def update(self, delta_time):
        pass