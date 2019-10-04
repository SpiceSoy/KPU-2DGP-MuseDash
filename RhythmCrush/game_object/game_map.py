#자료형 저장 하고 관리해주는 클래스

from .game_music import Music
from .note import Note
from ..utill.osu_file_format_parser import *
from ..utill.game_timer import *
from ..interface import IUpdatableObject
from ..interface import IDrawableObject

from RhythmCrush import debug


class GameMap(IUpdatableObject, IDrawableObject):
    def __init__(self, music_tag=None):
        self.is_active = False
        self.note_list = []
        self.music = Music()
        self.map = MusicNoteMap()
        self.timer = Timer()
        if music_tag is not None:
            self.load(music_tag)
        pass
    
    # 일단 Text URL 받게 설정
    def load(self, music_tag):
        self.map = load_map_source(music_tag)
        self.music.load(music_tag + "/../" + self.map.get_props("AudioFilename"))
        for note in self.map.get_hit_object():
            self.note_list.append(
                Note(
                    note[0], note[1], note[2], note[3], note[4],
                    (note[5], note[6], note[7], note[8]),
                    self.music.timer
                )
            )

    def start(self):
        self.timer.start()
        self.music.start()
        self.is_active = True

    def pause(self):
        self.timer.pause()
        self.music.pause()
        self.is_active = False

    def update(self, delta_time):
        if self.is_active:
            for note in self.note_list:
                note.update(delta_time)

    def draw(self):
        if self.is_active:
            for note in self.note_list:
                note.draw()
    


