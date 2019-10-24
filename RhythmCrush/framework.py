# 메인 프레임워크
import time
from .utill.input_manager import *
from RhythmCrush.game_scene import game_map


class Framework:
    def __init__(self, w=int(1440), h=int(810)):
        self.w = w
        self.h = h
        self.is_active = False
        self.prev_time = 0
        self.now_time = 0
        self.game_scene = game_map.NotePlayScene(self, "Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")

    def start(self):
        self.is_active = True
        print(self.w)
        print(self.h)
        pico2d.open_canvas(self.w, self.h)
        Framework.custom_audio_init()
        self.game_scene.load()
        self.game_scene.start()
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
        self.game_scene.handle_input()
        self.game_scene.update(delta_time)

    def draw(self):
        pico2d.clear_canvas()
        self.game_scene.draw()
        pico2d.update_canvas()

    @staticmethod
    def custom_audio_init():
        # pico2d 오디오 재설정
        pico2d.Mix_CloseAudio()
        ret = pico2d.Mix_OpenAudio(44100, pico2d.MIX_DEFAULT_FORMAT, pico2d.MIX_DEFAULT_CHANNELS, 2048)
        if -1 == ret:
            print('WARNING: Audio functions are disabled due to speaker or sound problems')
        else:
            audio_on = True

        if audio_on:
            pico2d.Mix_AllocateChannels(32)
            pico2d.Mix_Volume(-1, 64)
            pico2d.Mix_VolumeMusic(64)
