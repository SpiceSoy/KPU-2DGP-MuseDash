#-*- coding: utf-8 -*- 
# 리듬게임용 음악 모듈 - pico2d Music 클래스 래핑

import pico2d
import time
from Interface.Interface import IUpdatableObject

class Music(IUpdatableObject):
    def __init__(self,url = None):
        if url != None:
            self.start_time = 0
            self.load()
        pass
    def load(self,url):
        self.music_data = pico2d.load_music(url)
        
    def start(self):
        self.start_time = time.time()
        self.music_data.play()

    def pause(self):
        self.music_data.pause()
        
    def stop(self):
        self.music_data.stop()

    def get_current_sec(self):
        return time.time() - self.start_time

    def get_current_tick(self):
        return (time.time() - self.start_time) * 1000

    def get_length_sec(self):
        pass

    def get_length_tick(self):
        pass





#단위 테스트 코드
if __name__ == "__main__":
    debug_url = os.path.abspath("Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")
    text_data = open(debug_url,'r',encoding='UTF8')
    parse_file(text_data)
    