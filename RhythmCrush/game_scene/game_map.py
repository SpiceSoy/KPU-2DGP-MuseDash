from ..game_scene.base_scene import *

from ..game_object.game_music import Music
from ..game_object.note import Note
from ..game_object.player_object import  Player

from ..utill.osu_file_format_parser import *


class NotePlayScene(BaseScene):
    def __init__(self, framework, music_tag):
        super().__init__(framework)
        self.note_list = []
        self.music = Music()
        self.map = MusicNoteMap()
        self.start_index = 0
        self.music_tag = music_tag

    # 일단 Text URL 받게 설정
    def load(self):
        self.map = load_map_source(self.music_tag)
        self.music.load(self.music_tag + "/../" + self.map.get_props("AudioFilename"))
        self.start_index = 0
        for note in self.map.get_hit_object():
            self.note_list.append(
                Note(
                    note[0], note[1], note[2], note[3], note[4],
                    (note[5], note[6], note[7], note[8]),
                    self.music.timer
                )
            )

        self.player = Player()
        self.player.x = 100
        self.player.y = 400
        self.player.post_handler(self.framework.input_manager)

    def start(self):
        super().start()
        self.music.start()
        self.start_index = 0

    def resume(self):
        super().start()
        self.music.resume()

    def pause(self):
        super().start()
        self.music.pause()

    def stop(self):
        super().stop()
        self.music.stop()

    def update(self, delta_time):
        if self.is_active:
            self.player.update(delta_time)

            for i in range(self.start_index, len(self.note_list)):
                note = self.note_list[i]
                note.update(delta_time)
                if note.time - self.music.timer.get_time_tick() < 0:
                    self.start_index = i

            # for note in self.note_list:
            #     note.update(delta_time)

    def draw(self):
        if self.is_active:
            self.player.draw()

            # import pico2d
            # pico2d.debug_print("start_index = " + str(self.start_index))
            for i in range(self.start_index, len(self.note_list)):
                note = self.note_list[i]
                if note.is_in_clipped():
                    note.draw()
                else:
                    if note.time - self.music.timer.get_time_tick() > 100:
                        break
                    # break
            # for note in self.note_list:
            #     if note.is_in_clipped():
            #         note.draw()
            #     else:
            #         break


