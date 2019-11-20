import parse

from RhythmCrush.utill import image_manager

from RhythmCrush.component.accuracy import *

from RhythmCrush.interface import IUpdatableObject
from RhythmCrush.interface import IDrawableObject

# note_img_dic = {0: 'note-don', 4: 'note-big-don', 8: 'note-kat', 12: 'note-big-kat'}
note_img_dic = {0: 'note-don', 4: 'note-don', 8: 'note-kat', 12: 'note-kat', 6: 'note-kat'}
note_type_dic = {0: InputType.Don, 4: InputType.Don, 8: InputType.Kat, 12: InputType.Kat, 6: InputType.Kat}
type_y_dic = {InputType.Don: 405 - 25, InputType.Kat: 405 + 60}
randomize_note_csr = {0: True, 4: False, 8: True, 12: False, 6: False}
randomize_note_time = {0: True, 4: False, 8: False, 12: False, 6: False}


class Note(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, time, note_type, hit_sound, extras, music_timer,
                 speed=1000, clip_x=1440, clip_y=810, line_x=100, line_y=405):
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
            print(extra_zero)
            result = parse.parse("{},{}", extra_zero)
            self.end_time = int(result[0])
            self.accuracy.slide = True
            print(f"슬라이더 or 스핀 {self.end_time - self.time} 존재")
            extra_zero = result[1]

        self.extras = (int(extra_zero), int(extras[1]), int(extras[2]), int(extras[3]))
        # 여기까지는 파일 포맷 그대로

        self.music_timer = music_timer

        self.speed = speed
        self.clip_x = clip_x
        self.clip_y = clip_y
        self.line_x = line_x
        self.line_y = type_y_dic[note_type_dic[self.hit_sound]]
        self.update_start_time = 5000

        self.image = image_manager.get_image_controller(
            note_img_dic[self.hit_sound],
            randomize_note_csr[self.hit_sound],
            randomize_note_time[self.hit_sound]
        )
        self.long_fx = image_manager.get_image_controller('slide-back-fx')

        pass

    def get_remain_value(self):
        current_music_tick = self.music_timer.get_time_tick()
        return self.time - current_music_tick

    def calculate_current_position(self):
        remain_value = self.get_remain_value()
        self.x = self.line_x + remain_value * (self.speed/1000.0)
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
        self.image.update(delta_time)
        return will_continue

    def is_in_clipped(self):
        if self.end_time != 0:
            padding = (self.end_time - self.time) * (self.speed/1000.0) + 200
        else:
            padding = 200
        return -padding <= self.x <= self.clip_x + padding and -padding <= self.y <= self.clip_y + padding

    def draw(self):
        if self.end_time != 0:
            width = (self.end_time - self.time) * (self.speed/1000.0)
            height = self.long_fx.image.h
            self.long_fx.draw(self.x + width/2, self.y, width, height)
        self.image.draw(self.x, self.y)

    def check_note_accuracy(self):
        self.accuracy.judge(self.get_remain_value())
        return self.accuracy.grade

    def check_hit(self, player_input):
        if self.end_time != 0:
            print("CheckHit")
            if (self.time - self.end_time) < self.get_remain_value() < 0:
                self.accuracy.judge(0, note_type_dic[self.hit_sound], note_type_dic[self.hit_sound])
            else:
                self.accuracy.judge(self.get_remain_value(), player_input, note_type_dic[self.hit_sound])
        else:
            self.accuracy.judge(self.get_remain_value(), player_input, note_type_dic[self.hit_sound])
        return self.accuracy

    def check_no_input(self):
        return self.accuracy.check_no_input(self.get_remain_value()) and self.end_time == 0

    def check_gone(self):
        if self.end_time != 0:
            return self.get_remain_value() + (self.end_time - self.time) < -500
        else:
            return self.get_remain_value() < -500