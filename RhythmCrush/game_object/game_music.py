# -*- coding: utf-8 -*-
# 리듬게임용 음악 모듈 - pico2d Music 클래스 래핑

import pico2d
from ..utill.game_timer import *
import time


class Music:
    def __init__(self, url=None):
        self.music_data = None
        self.timer = Timer()
        if url is not None:
            self.load()

    def load(self, url):
        self.music_data = pico2d.load_music(url)
        
    def start(self):
        self.timer.start()
        self.music_data.play()

    def pause(self):
        self.timer.pause()
        self.music_data.pause()

    def resume(self):
        self.timer.resume()
        self.music_data.resume()

    def stop(self):
        self.music_data.stop()

    def get_length_sec(self):
        pass

    def get_length_tick(self):
        pass


class Effect:
    def __init__(self, url=None):
        self.wav = None
        if url is not None:
            self.load(url)

    def load(self, url):
        self.wav = pico2d.load_wav(url)

    def play(self):
        self.wav.play()
