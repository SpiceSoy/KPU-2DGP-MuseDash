import pico2d

from ..utill import image_manager
from ..utill import game_timer

from ..interface import IUpdatableObject
from ..interface import IDrawableObject

note_type_dic = {'normal': 'note-back-big'}


class Note(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, time, note_type, hit_sound, extras, music_timer,
                 speed=10, clip_x=1440, clip_y=810, line_x=100, line_y=0):
        """
        :type music_timer: game_timer.Timer
        """
        # 여기부터
        self.x = x
        self.y = y
        self.time = time
        self.note_type = note_type
        self.hit_sound = hit_sound
        self.extras = extras
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
        current_music_tick = self.music_timer.get_timer_tick()
        remain_value = current_music_tick - self.time
        self.x = self.line_x + remain_value * self.speed
        self.y = self.y
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
            self.image.draw(self, self.x, self.y)
        pass
