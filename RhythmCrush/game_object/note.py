import pico2d
import parse

from ..utill import image_manager
from ..utill import game_timer

from ..interface import IUpdatableObject
from ..interface import IDrawableObject
from RhythmCrush import debug

note_type_dic = {'normal': 'note-back-big'}


class Note(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, time, note_type, hit_sound, extras, music_timer,
                 speed=1, clip_x=1440, clip_y=810, line_x=100, line_y=405):
        # 여기부터
        self.x = int(x)
        self.y = int(y)
        self.time = int(time)
        self.note_type = int(note_type)
        self.hit_sound = int(hit_sound)
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
        # TODO 실제 들어오는 Type 값에 맞춰서 변경 필요
        # self.image = image_manager.load_image(note_type_dic[note_type])
        self.image = image_manager.load_image(note_type_dic['normal'])
        pass

    def calculate_current_position(self):
        current_music_tick = self.music_timer.get_time_tick()
        remain_value = self.time - current_music_tick
        debug.print_console("note-calc", f"Remain Value is {remain_value}")
        self.x = self.line_x + remain_value * self.speed
        self.y = self.line_y
        pass

    def set_note_speed(self, speed):
        self.speed = speed

    def set_clip_port(self, size_x, size_y):
        self.clip_x = size_x
        self.clip_y = size_y

    def update(self, delta_time):
        self.calculate_current_position()
        pass

    def draw(self):
        padding = 200
        if -padding <= self.x <= self.clip_x + padding and -padding <= self.y <= self.clip_y + padding:
            self.image.draw(self.x, self.y)
            debug.print_console("note", f"Drawing Note")
            # debug.print_console("note", f"Drawing at {self.x} , {self.y}")
        else:
            debug.print_console("note", f"Clipping Note")
            # debug.print_console("note", f"Clip at {self.x} , {self.y}")
        pass
