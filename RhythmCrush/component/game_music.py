# -*- coding: utf-8 -*-
# 리듬게임용 음악 모듈 - pico2d Music 클래스 래핑

import pico2d
from RhythmCrush.utill.game_timer import *
import time


class Music:
    def __init__(self):
        self.music_data = None
        self.timer = Timer()

    def __del__(self):
        print("Music Deleted")
        del self.music_data

    def load(self, url):
        print("Music Loaded" + str(url))
        self.music_data = pico2d.load_music(url)
        
    def start(self):
        self.timer.start()
        self.music_data.play()
        print("Music Play")


    def pause(self):
        self.timer.pause()
        self.music_data.pause()
        print("Music Pause")

    def resume(self):
        self.timer.resume()
        self.music_data.resume()
        print("Music Resume")

    def stop(self):
        self.timer.stop()
        self.music_data.stop()
        print("Music Stop")

class Effect:
    def __init__(self, url=None):
        self.wav = None
        if url is not None:
            self.load(url)

    def load(self, url):
        self.wav = pico2d.load_wav(url)

    def play(self):
        self.wav.play()
