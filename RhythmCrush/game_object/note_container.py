from RhythmCrush.interface.Interface import IUpdatableObject, IDrawableObject

from RhythmCrush import handler_set
from RhythmCrush.game_object.note import *
from RhythmCrush.game_object.hit_effect_object import *
from RhythmCrush.utill.input_manager import *
from RhythmCrush.utill.osu_file_format_parser import *
from RhythmCrush.game_object.accuracy_effect import *


class NoteContainer(IUpdatableObject, IDrawableObject):
    def __init__(self, music_tag, music_timer, world, hp, score, combo,
                 effect_don_normal, effect_don_hit, effect_kat_normal, effect_kat_hit, effect_combo_break):
        self.world = world
        self.music_tag = music_tag
        self.music_timer = music_timer
        self.map = MusicNoteMap()
        self.note_list = []

        self.effect_don_hit = effect_don_hit;
        self.effect_don_normal = effect_don_normal;
        self.effect_kat_hit = effect_kat_hit;
        self.effect_kat_normal = effect_kat_normal;
        self.effect_combo_break = effect_combo_break;
        #
        self.hp = hp
        self.score = score
        self.combo = combo

        # 최적화용 변수
        self.start_index = 0
        self.extra_update_count = 5
        self.extra_check_count = 10
        self.start_hit = 0

    def load(self):
        # 맵 파일 로드
        self.map = load_map_source(self.music_tag)
        # 노트 로드
        for note in self.map.get_hit_object():
            self.note_list.append(
                Note(
                    note[0], note[1], note[2], note[3], note[4],
                    (note[5], note[6], note[7], note[8]),
                    self.music_timer
                )
            )
        self.start_index = 0

    def update(self, delta_time):
        count = self.extra_update_count
        for i in range(self.start_index, len(self.note_list)):
            note = self.note_list[i]
            if note.check_no_input():
                self.hp.check(note.accuracy.grade)
                self.score.add_score(note.accuracy)
                self.spawn_effect(AccuracyGrade.Miss)
                if not self.combo.is_zero():
                    self.effect_combo_break.play()
                self.combo.break_combo()
            if note.update(delta_time) is False:
                count -= 1
            if note.check_gone():
                self.start_index = i
            if count < 0:
                break;

    def draw(self):
        for i in range(self.start_index, len(self.note_list)):
            note = self.note_list[i]
            if note.is_in_clipped():
                note.draw()
            else:
                if note.time - self.music_timer.get_time_tick() > 100:
                    break

    def check_map_is_end(self):
        return self.note_list[-1].get_remain_value() < -2000

    def check_note_accuracy(self, player_input):
        count = self.extra_check_count
        # for i in range(self.start_index, len(self.note_list)):
        for i in range(0, len(self.note_list)):
            note = self.note_list[i]
            if not note.accuracy.is_gone():
                acc = note.check_hit(player_input)
                if acc.is_hit():
                    note.on_hit()
                    self.world.add_object(HitEffect(note.x, note.y, self.world), 3)
                    return acc
                else:
                    count -= 1
            if count < 0:
                return Accuracy()
        return Accuracy()

    def get_props(self, title: str):
        return self.map.get_props(title)

    def position_update_first(self):
        for note in self.note_list:
            note.calculate_current_position()

    def spawn_effect(self, acc):
        if Judgement.is_hit(acc):
            self.world.add_object(AccuracyEffect(150, 450, acc, self.world), 3)

    def set_note_speed(self, speed):
        for n in self.note_list:
            n.set_note_speed(speed)

    def post_handler(self, input_handler: InputHandlerManager):
        def touch_type(type, hit, normal):
            def touch():
                ac = self.check_note_accuracy(type)
                self.hp.check(ac.grade)
                self.score.add_score(ac)
                print(f"grade : {ac.grade} / diff_time : {ac.difference}")
                print(f"{str(self.combo)} / current_hp : {self.hp.get_hp()}")
                self.spawn_effect(ac.grade)
                if ac.is_success():
                    hit.play()
                    self.combo.plus_combo()
                elif ac.is_fail():
                    if not self.combo.is_zero():
                        self.effect_combo_break.play()
                    self.combo.break_combo()
                else:
                    normal.play()
            return touch

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, touch_type(InputType.Don, self.effect_don_hit, self.effect_don_normal))
        )
        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, touch_type(InputType.Kat, self.effect_kat_hit, self.effect_kat_normal))
        )

