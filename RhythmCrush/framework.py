# 메인 프레임워크
import time
from .utill.input_manager import *
from RhythmCrush.game_scene import *


class Framework:
    def __init__(self, w=int(1440), h=int(810)):
        self.w = w
        self.h = h
        self.is_active = False
        self.prev_time = 0
        self.now_time = 0
        self.scene_stack = []
        self.scene_stack.append(TitleScene(self))

    def start(self):
        self.is_active = True
        print(self.w)
        print(self.h)
        pico2d.open_canvas(self.w, self.h)
        Framework.custom_audio_init()
        self.scene_stack[-1].load()
        self.scene_stack[-1].start()
        self.prev_time = time.time()
        self.now_time = time.time()

    def loop(self):
        while self.is_active:
            self.prev_time = self.now_time
            self.now_time = time.time()
            delta_time = self.now_time - self.prev_time
            self.update(delta_time)
            self.draw()

    def update(self, delta_time):
        self.scene_stack[-1].handle_input()
        self.scene_stack[-1].update(delta_time)

    def draw(self):
        pico2d.clear_canvas()
        self.scene_stack[-1].draw()
        pico2d.update_canvas()

    def exit(self):
        self.is_active = False

    def change_scene(self, scene_inst):
        while len(self.scene_stack) > 0:
            self.scene_stack[-1].stop()
            self.scene_stack.pop()
        self.scene_stack.append(scene_inst)
        scene_inst.start()

    def push_scene(self, scene_inst):
        if len(self.scene_stack) > 0:
            self.scene_stack[-1].pause()
        self.scene_stack.append(scene_inst)
        scene_inst.start()

    def pop_scene(self):
        if len(self.scene_stack) > 0:
            self.scene_stack[-1].stop()
            self.scene_stack.pop()
        if len(self.scene_stack) > 0:
            self.scene_stack[-1].resume()

    def get_index_stack(self, index):
        return self.scene_stack[index]

    @staticmethod
    def custom_audio_init():
        # pico2d 오디오 재설정
        pico2d.Mix_CloseAudio()
        ret = pico2d.Mix_OpenAudio(44100, pico2d.MIX_DEFAULT_FORMAT, pico2d.MIX_DEFAULT_CHANNELS, 1024)
        if -1 == ret:
            print('WARNING: Audio functions are disabled due to speaker or sound problems')
        else:
            audio_on = True

        if audio_on:
            pico2d.Mix_AllocateChannels(32)
            pico2d.Mix_Volume(-1, 64)
            pico2d.Mix_VolumeMusic(64)
