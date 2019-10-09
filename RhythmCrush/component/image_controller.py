import pico2d
from ..interface import IUpdatableObject


class ImageController(IUpdatableObject):
    def __init__(self, image: pico2d.Image):
        self.frame_buffer = []
        self.frame_csr = 0
        self.frame_time = float(0.0)
        self.image = image
        self.speed = 1

    def add_frame(self, u, v, w, h, sec=float(0.05)):
        self.frame_buffer.append((u, v, w, h, sec))
        return self

    def add_frame_other_position(self, u, v):
        w = self.frame_buffer[-1][2]
        h = self.frame_buffer[-1][3]
        sec = self.frame_buffer[-1][4]
        self.frame_buffer.append((u, v, w, h, sec))
        return self

    def change_speed(self, speed):
        self.speed

    def get_frame(self, index):
        return self.frame_buffer[index]

    def draw(self, x, y, w=None, h=None):
        if len(self.frame_buffer) == 0:
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
        if len(self.frame_buffer) == 0:
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
        if len(self.frame_buffer) > 1:
            self.frame_time += delta_time * self.speed
            if self.frame_buffer[self.frame_csr][4] <= self.frame_time:
                self.frame_csr += 1
                self.frame_csr %= len(self.frame_buffer)
                self.frame_time = float(0.0)
