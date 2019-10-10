import enum
from ..interface import IUpdatableObject


class SubAnimation(IUpdatableObject):
    def __init__(self, next: str):
        self.frame_buffer = []
        self.frame_csr = 0
        self.frame_time = float(0.0)
        self.next = next
        return self

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
        self.speed = speed

    def get_frame(self, index):
        return self.frame_buffer[index]

    def update(self, delta_time):
        if len(self.frame_buffer) > 1:
            self.frame_time += delta_time
            if self.frame_buffer[self.frame_csr][4] <= self.frame_time:
                self.frame_csr += 1
                self.frame_time = float(0.0)

    def get_current_animation(self):
        return self.frame_buffer[min(self.frame_csr, len(self.frame_buffer)-1)]

    def is_end(self):
        return self.frame_csr > len(self.frame_buffer)

    def get_next(self):
        return self.next

    def reset(self):
        self.frame_time = 0


class Animator(IUpdatableObject):
    def __init__(self):
        self.sub_animations = {}
        self.current_key = None
        pass

    def add_sub_animation(self, key, sub_animation: SubAnimation):
        if len(self.sub_animations) == 0:
            self.current_key = key
        self.sub_animations[key] = sub_animation
        return self

    def current_sub_animation_is_end(self):
        return self.sub_animations[self.current_key].is_end()

    def change_current_animation(self, key):
        current = self.sub_animations[self.current_key]
        if key is not None:
            current.reset()
            if key is not "repeat":
                self.current_key = key

    def get_current_sub_animation(self):
        return self.sub_animations[self.current_key].get_frame()

    def update(self, delta_time):
        current = self.sub_animations[self.current_key]
        current.update(delta_time)
        if self.current_sub_animation_is_end():
            self.change_current_animation(current.get_next())
        pass
