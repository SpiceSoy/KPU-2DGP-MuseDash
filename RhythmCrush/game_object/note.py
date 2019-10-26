import pico2d
import parse

from ..utill import image_manager
from ..utill import game_timer

from ..game_object.accuracy import *

from ..interface import IUpdatableObject
from ..interface import IDrawableObject
from .. import debug

note_type_dic = {0: 'note-don', 4: 'note-big-don', 8: 'note-kat', 12: 'note-big-kat'}
randomize_note_csr = {0: True, 4: False, 8: True, 12: False}
randomize_note_time = {0: True, 4: False, 8: False, 12: False}


class Note(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, time, note_type, hit_sound, extras, music_timer,
                 speed=1, clip_x=1440, clip_y=810, line_x=100, line_y=405):
        # 여기부터
        self.x = -1000
        self.y = -1000
        self.time = int(time)
        self.note_type = int(note_type)
        self.hit_sound = int(hit_sound)
        self.accuracy = Accuracy()

        extra_zero = extras[0]
        if extras[0].find(',') is -1:
            self.end_time = 0
        else:
            result = parse.parse("{},{}", extra_zero)
            self.end_time = int(result[0])
            extra_zero = result[1]

        self.extras = (int(extra_zero), int(extras[1]), int(extras[2]), int(extras[3]))
        # 여기까지는 파일 포맷 그대로

        self.music_timer = music_timer

        self.speed = speed
        self.clip_x = clip_x
        self.clip_y = clip_y
        self.line_x = line_x
        self.line_y = line_y
        self.update_start_time = 5000
        # TODO 실제 들어오는 Type 값에 맞춰서 변경 필요
        # self.image = image_manager.load_image(note_type_dic[note_type])
        self.image = image_manager.get_image_controller(
            note_type_dic[self.hit_sound],
            randomize_note_csr[self.hit_sound],
            randomize_note_time[self.hit_sound]
        )
        pass

    def get_remain_value(self):
        current_music_tick = self.music_timer.get_time_tick()
        return self.time - current_music_tick

    def calculate_current_position(self):
        remain_value = self.get_remain_value()
        debug.print_console("note-calc", f"Remain Value is {remain_value}")
        self.x = self.line_x + remain_value * self.speed
        self.y = self.line_y
        return self.update_start_time > remain_value

    def set_note_speed(self, speed):
        self.speed = speed

    def set_clip_port(self, size_x, size_y):
        self.clip_x = size_x
        self.clip_y = size_y

    def set_update_start_time(self, time):
        self.update_start_time = time

    def update(self, delta_time):
        will_continue = self.calculate_current_position()
        self.accuracy.check_no_input(self.get_remain_value())
        self.image.update(delta_time)
        return will_continue

    def is_in_clipped(self):
        padding = 200
        return -padding <= self.x <= self.clip_x + padding and -padding <= self.y <= self.clip_y + padding

    def draw(self):
        self.image.draw(self.x, self.y)

    def check_note_accuracy(self):
        self.accuracy.judge(self.get_remain_value())
        return self.accuracy.grade

    def check_hit(self):
        self.accuracy.judge(self.get_remain_value())
        return self.accuracy

    def check_no_input(self):
        self.accuracy.check_no_input(self.get_remain_value())
