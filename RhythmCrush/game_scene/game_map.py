import pico2d

from RhythmCrush.game_scene.base_scene import BaseScene
from RhythmCrush.game_scene import fail_scene
from RhythmCrush.game_scene import pause_scene
from RhythmCrush.game_scene import clear_scene

from RhythmCrush.game_object.note import Note
from RhythmCrush.game_object.note_container import NoteContainer
from RhythmCrush.game_object.player_object import Player

from RhythmCrush.component.game_music import Music, Effect
from RhythmCrush.component.combo import Combo
from RhythmCrush.component.hp import Hp
from RhythmCrush.component.score import Score
from RhythmCrush.component.accuracy import *


from RhythmCrush import ui
from RhythmCrush import handler_set

from RhythmCrush.utill.osu_file_format_parser import *
from RhythmCrush.component.interpolator import *


class NotePlayScene(BaseScene):
    def __init__(self, framework, music_tag):
        # 베이스 초기화
        super().__init__(framework)

        # 플레이할 음악
        self.music_tag = music_tag
        self.music = Music()

        # 효과음
        self.effect_don_normal = Effect()
        self.effect_don_hit = Effect()
        self.effect_kat_normal = Effect()
        self.effect_kat_hit = Effect()
        self.effect_combo_break = Effect()

        # 콤보 HP 점수
        self.combo = Combo()
        self.hp = Hp()
        self.score = Score()

        # 수치 인터포레이터
        self.hp_interpolator = FixedRatioInterpolator(self.hp.get_hp(), self.hp.get_hp(), 0.05)
        self.score_interpolator = FixedRatioInterpolator(self.score.get_score(), self.score.get_score(), 0.25)
        self.percent_interpolator = FixedRatioInterpolator(
            self.score.get_accuracy_percent(), self.score.get_accuracy_percent(), 0.25
        )

        # 플레이어
        self.player = Player(100, 400)

        # 노트 컨테이너
        self.notes = NoteContainer(music_tag, self.music.timer, self.hp, self.score, self.combo,
                                   self.effect_don_normal, self.effect_don_hit,
                                   self.effect_kat_normal, self.effect_kat_hit,
                                    self.effect_combo_break)

        # UI
        self.ui_combo_text = ui.UIText(800, 50, self.combo.now_combo, pt=100)
        self.ui_hp = ui.UIProgressBar(700, 600, 'ui-hp')
        self.ui_score = ui.UIText(100, self.framework.h - 100, self.score.get_score(), pt=25)
        self.ui_acc_percent = ui.UIText(10, 50, str(self.score.get_accuracy_percent()), pt=100)

        self.game_world.add_layer()
        self.game_world.add_object(self.player, 1)
        self.game_world.add_object(self.notes, 2)
        self.game_world.add_object(self.ui_combo_text, 3)
        self.game_world.add_object(self.ui_hp, 3)
        self.game_world.add_object(self.ui_score, 3)
        self.game_world.add_object(self.ui_acc_percent, 3)

    def load(self):
        super().load()
        # 음악 로드
        self.music.load(self.music_tag + "/../" + self.notes.get_props("AudioFilename"))
        # 효과음 로드
        self.effect_don_hit.load("Resource/Sound/don-hit.wav")
        self.effect_don_normal.load("Resource/Sound/don-normal.wav")
        self.effect_kat_hit.load("Resource/Sound/kat-hit.wav")
        self.effect_kat_normal.load("Resource/Sound/kat-normal.wav")
        self.effect_combo_break.load("Resource/Sound/combo-break.wav")

    def start(self):
        super().start()
        self.music.start()

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
        super().update(delta_time)
        # Interpolate
        self.hp_interpolator.dest = self.hp.get_hp()
        self.hp_interpolator.update(delta_time)
        self.score_interpolator.dest = self.score.get_score()
        self.score_interpolator.update(delta_time)
        self.percent_interpolator.dest = self.score.get_accuracy_percent()
        self.percent_interpolator.update(delta_time)

        # UIUpdate
        self.ui_combo_text.update_text(f"COMBO : {self.combo.now_combo}")
        self.ui_score.update_text(f"SCORE : {int(self.score_interpolator.get_current_value())}")
        self.ui_acc_percent.update_text(f"{int(self.percent_interpolator.get_current_value())}%")
        self.ui_hp.update_value(self.hp_interpolator.get_current_value(), self.hp.max_hp)
        if self.hp.get_hp() <= 0:
            self.framework.change_scene(fail_scene.FailScene(self.framework))
        self.check_game_is_end()

    def post_handler(self):
        def enter_pause_scene():
            self.framework.push_scene(pause_scene.PauseScene(self.framework))

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_p, enter_pause_scene)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, enter_pause_scene)
        )
        self.player.post_handler(self.input_handler)
        self.notes.post_handler(self.input_handler)

    def check_game_is_end(self):
        if self.notes.check_map_is_end():
            self.framework.push_scene(
                clear_scene.ClearScene(
                    self.framework,
                    int(self.score.get_score()),
                    int(self.score.get_accuracy_percent())
                )
            )