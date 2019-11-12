from RhythmCrush.component.accuracy import *


class Hp:
    def __init__(self):
        self.max_hp = 1000.0
        self.hp = self.max_hp
        self.hp_delta = 250.0
        self.grade_delta_ratio = {
            AccuracyGrade.Perfect: 0.5,
            AccuracyGrade.Nice: 0.4,
            AccuracyGrade.Good: 0.25,
            AccuracyGrade.Ignore: 0.0,
            AccuracyGrade.Bad: -0.8,
            AccuracyGrade.Miss: -1.0,
            AccuracyGrade.NoInput: -1.0,
        }

    def check(self, grade : AccuracyGrade):
        self.hp += self.grade_delta_ratio[grade] * self.hp_delta
        self.hp = max(min(self.hp, self.max_hp), 0.0)

    def is_game_over(self):
        return self.hp <= 0.0

    def get_hp(self):
        return self.hp
