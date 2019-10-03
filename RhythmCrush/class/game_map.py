#자료형 저장 하고 관리해주는 클래스

from .game_music import Music
from .note import Note
from ..utill.osu_file_format_parser import *
from ..interface import IUpdatableObject
from ..interface import IDrawableObject


class GameMap:
    def __init__(self):
        self.note_list = []
        self.music = Music()
        pass

    def update(self, delta_time):
        self.music.update(delta_time)
        for note in self.note_list:
            pass

    def draw(self):
        raise NotImplementedError()
    


