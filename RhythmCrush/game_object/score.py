from ..game_object.accuracy import *


class Score:
    score_max = 300
    accuracy_score_ratio = {
        AccuracyGrade.Perfect: 1.0,
        AccuracyGrade.Nice: 0.75,
        AccuracyGrade.Good: 0.4,
        AccuracyGrade.Bad: 0.1,
        AccuracyGrade.Miss: 0.0,
        AccuracyGrade.NoInput: 0.0,
        AccuracyGrade.Ignore: 0.0,
    }
    accuracy_percent_ratio = {
        AccuracyGrade.Perfect: 1.0,
        AccuracyGrade.Nice: 0.9,
        AccuracyGrade.Good: 0.6,
        AccuracyGrade.Bad: 0.25,
        AccuracyGrade.Miss: 0.0,
        AccuracyGrade.NoInput: 0.0,
        AccuracyGrade.Ignore: 0.0,
    }

    def __init__(self):
        self.score = 0
        self.accuracy_percent_total = 0.0
        self.accuracy_count = 0.0

    def add_score(self, acc: Accuracy):
        self.score += Score.accuracy_score_ratio[acc.grade] * Score.score_max
        self.accuracy_percent_total += Score.accuracy_percent_ratio[acc.grade]
        if acc.grade != AccuracyGrade.Ignore:
            self.accuracy_count += 1

    def get_score(self):
        return self.score

    def get_accuracy_percent(self):
        if self.accuracy_count == 0:
            return 0.0
        return self.accuracy_percent_total / self.accuracy_count * 100.0