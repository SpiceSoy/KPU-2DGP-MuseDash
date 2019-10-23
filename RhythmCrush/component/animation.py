from ..interface import IUpdatableObject


class SubAnimation:
    def __init__(self, next: str):
        self.frame_buffer = []
        self.next = next

    def set_frame_buffer(self, buffer):
        self.frame_buffer = buffer;

    def add_frame(self, u, v, w, h, sec=float(0.16)):
        self.frame_buffer.append((u, v, w, h, sec))
        return self

    def add_frame_other_position(self, u, v):
        w = self.frame_buffer[-1][2]
        h = self.frame_buffer[-1][3]
        sec = self.frame_buffer[-1][4]
        self.frame_buffer.append((u, v, w, h, sec))
        return self

    def get_frame(self, index):
        return self.frame_buffer[index]

    def is_current_frame_end(self, frame_csr, frame_time):
        if len(self.frame_buffer) > 1:
            return self.frame_buffer[frame_csr][4] <= frame_time
        else:
            return False

    def get_current_animation(self, frame_csr):
        return self.frame_buffer[min(frame_csr, len(self.frame_buffer)-1)]

    def is_end(self, frame_csr):
        return frame_csr >= len(self.frame_buffer)

    def get_next(self):
        return self.next


class Animator(IUpdatableObject):
    def __init__(self):
        self.sub_animations = {}
        self.frame_csr = 0
        self.frame_time = float(0.0)
        self.current_key = None
        pass

    def add_sub_animation(self, key, sub_animation: SubAnimation):
        if len(self.sub_animations) == 0:
            self.current_key = key
        self.sub_animations[key] = sub_animation
        return self

    def get_current_sub_animation(self):
        return self.sub_animations[self.current_key]

    def current_sub_animation_is_end(self):
        return self.get_current_sub_animation().is_end(self.frame_csr)

    def change_current_animation(self, key):
        current = self.sub_animations[self.current_key]
        if current.get_next() is not None:
            self.reset_frame_info()
            if key is not "repeat":
                self.current_key = key

    def get_current_sub_animation_frame(self):
        return self.sub_animations[self.current_key].get_current_animation(self.frame_csr)

    def update(self, delta_time):
        current = self.sub_animations[self.current_key]
        self.frame_time += delta_time
        if self.get_current_sub_animation().is_current_frame_end(self.frame_csr, self.frame_time):
            self.frame_csr = self.frame_csr + 1
            self.frame_time = float(0.0)
        if self.current_sub_animation_is_end():
            self.change_current_animation(current.get_next())
        pass

    def reset_frame_info(self):
        self.frame_csr = 0
        self.frame_time = float(0.0)

    def reset_all(self, first_key=None):
        self.reset_frame_info()
        self.current_key = first_key
