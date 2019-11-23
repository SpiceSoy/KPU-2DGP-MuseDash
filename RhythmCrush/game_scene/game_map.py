import pico2d

from RhythmCrush.game_scene.base_scene import BaseScene
from RhythmCrush.game_scene import fail_scene
from RhythmCrush.game_scene import pause_scene
from RhythmCrush.game_scene import clear_scene
from RhythmCrush.game_scene import ready_scene

from RhythmCrush.game_object.note import Note
from RhythmCrush.game_object.note_container import NoteContainer
from RhythmCrush.game_object.hit_effect_object import HitEffect
from RhythmCrush.game_object.player_object import Player
from RhythmCrush.game_object.cloud_spawner import CloudSpawner
from RhythmCrush.game_object.cloud_object import Cloud
from RhythmCrush.game_object.loop_image import HorizontalLoopImage

from RhythmCrush.component.game_music import Music, Effect
from RhythmCrush.component.combo import Combo
from RhythmCrush.component.hp import Hp
from RhythmCrush.component.score import Score
from RhythmCrush.component.accuracy import *


from RhythmCrush import ui
from RhythmCrush import handler_set
from RhythmCrush.utill.font_manager import *

from RhythmCrush.utill.osu_file_format_parser import *
from RhythmCrush.component.interpolator import *


class NotePlayScene(BaseScene):
    normal_text_color = (83, 83, 83)
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

        self.speed = 1000.0

        # 수치 인터포레이터
        self.hp_interpolator = FixedRatioInterpolator(self.hp.get_hp(), self.hp.get_hp(), 0.05)
        self.score_interpolator = FixedRatioInterpolator(self.score.get_score(), self.score.get_score(), 0.25)
        self.percent_interpolator = FixedRatioInterpolator(
            self.score.get_accuracy_percent(), self.score.get_accuracy_percent(), 0.25
        )
        self.speed_interpolator = FixedRatioInterpolator(self.speed, self.speed, 0.05)

        # 플레이어
        self.player = Player(100, 400)

        # 배경 루프 이미지
        self.back_image = ui.UIStaticImage(self.framework.w/2, self.framework.h/2, 'ui-game-back')
        self.ground_loop_image = HorizontalLoopImage(
            self.framework.w/2, self.framework.h/2 - 60, self.framework.w, self.framework.h, 'loop-ground', 1000
        )

        # 배경 구름
        self.cloud_spawner = CloudSpawner(self.game_world)

        # 노트 컨테이너
        self.notes = NoteContainer(music_tag, self.music.timer, self.game_world, self.hp, self.score, self.combo,
                                   self.effect_don_normal, self.effect_don_hit,
                                   self.effect_kat_normal, self.effect_kat_hit,
                                    self.effect_combo_break)

        # UI
        self.ui_combo_text = ui.UIText(800, 50, str(self.combo.now_combo),
                                       FontType.Fixedsys, pt=100, color=NotePlayScene.normal_text_color)

        self.ui_hp = ui.UIProgressBar(400, 750, 'ui-hp')
        self.ui_score = ui.UIText(850, 750, str(self.score.get_score()), FontType.Fixedsys,
                                  pt=75, color=NotePlayScene.normal_text_color)
        self.ui_acc_percent = ui.UIText(10, 50, str(self.score.get_accuracy_percent()), FontType.Fixedsys,
                                        pt=100,color=NotePlayScene.normal_text_color)

        self.ui_cur_speed = ui.UIText(400, 50, str(self.speed_interpolator.get_current_value() / 1000.0)[:3], FontType.Fixedsys,
                                        pt=100, color=NotePlayScene.normal_text_color)

        self.ui_hit_line = ui.UIStaticImage(200, self.framework.h/2, 'ui-hit-line')


        self.game_world.add_layer()
        self.game_world.add_object(self.cloud_spawner, 0)
        self.game_world.add_object(self.back_image, 0)
        self.game_world.add_object(self.player, 1)
        self.game_world.add_object(self.ground_loop_image, 1)
        self.game_world.add_object(self.notes, 2)
        self.game_world.add_object(self.ui_combo_text, 3)
        self.game_world.add_object(self.ui_hp, 3)
        self.game_world.add_object(self.ui_score, 3)
        self.game_world.add_object(self.ui_acc_percent, 3)
        self.game_world.add_object(self.ui_cur_speed, 3)
        self.game_world.add_object(self.ui_hit_line, 3)

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
        pico2d.hide_lattice()

    def draw(self):
        super().draw()

    def start(self):
        super().start()
        self.music.start()
        self.notes.position_update_first()
        self.framework.push_scene(ready_scene.ReadyScene(self.framework))

    def resume(self):
        super().resume()
        self.music.resume()

    def pause(self):
        super().pause()
        self.music.pause()

    def stop(self):
        super().stop()
        print("Child Stop")
        self.music.stop()
        del self.music

    def update(self, delta_time):
        super().update(delta_time)
        # Interpolate
        self.hp_interpolator.dest = self.hp.get_hp()
        self.hp_interpolator.update(delta_time)
        self.score_interpolator.dest = self.score.get_score()
        self.score_interpolator.update(delta_time)
        self.percent_interpolator.dest = self.score.get_accuracy_percent()
        self.percent_interpolator.update(delta_time)
        self.speed_interpolator.dest = self.speed
        self.speed_interpolator.update(delta_time)

        # UIUpdate
        self.ui_combo_text.update_text(f"COMBO : {self.combo.now_combo}")
        self.ui_score.update_text(f"SCORE : {int(self.score_interpolator.get_current_value())}")
        self.ui_acc_percent.update_text(f"{int(self.percent_interpolator.get_current_value())}%")
        self.ui_hp.update_value(self.hp_interpolator.get_current_value(), self.hp.max_hp)
        self.ui_cur_speed.update_text(str(self.speed_interpolator.get_current_value() / 1000.0)[:3])
        if self.hp.get_hp() <= 0:
            self.framework.change_scene(fail_scene.FailScene(self.framework))
        self.check_game_is_end()

        self.notes.set_note_speed(self.speed_interpolator.get_current_value())
        self.ground_loop_image.set_speed(self.speed_interpolator.get_current_value())

        for o in self.game_world.all_object():
            if type(o) == Cloud:
                o.speed = self.speed_interpolator.get_current_value()

    def post_handler(self):

        def get_change_speed(delta):
            def change_speed():
                self.speed += delta
            return change_speed

        def enter_pause_scene():
            self.framework.push_scene(ready_scene.ReadyScene(self.framework))
            self.framework.push_scene(pause_scene.PauseScene(self.framework))

        def up_effect():
            # self.game_world.add_object(HitEffect(200, 400 + 50 + 10, self.game_world), 3)
            pass

        def down_effect():
            # self.game_world.add_object(HitEffect(200, 400 - 50, self.game_world), 3)
            pass

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_p, enter_pause_scene)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, enter_pause_scene)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_LEFT, get_change_speed(-100.0))
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_RIGHT, get_change_speed(100.0))
        )

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, up_effect)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, down_effect)
        )
        self.player.post_handler(self.input_handler)
        self.notes.post_handler(self.input_handler)

    def check_game_is_end(self):
        if self.notes.check_map_is_end():
            self.framework.change_scene(
                clear_scene.ClearScene(
                    self.framework,
                    int(self.score.get_score()),
                    int(self.score.get_accuracy_percent())
                )
            )