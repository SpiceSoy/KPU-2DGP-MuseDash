import enum


class InputType(enum.Enum):
    Don = 1
    Kat = 2


class AccuracyGrade(enum.Enum):
    Perfect = 3
    Nice = 2
    Good = 1
    Ignore = 0
    Bad = -1
    Miss = -2
    NoInput = -3


class Judgement:
    hit_range_tick = 250
    perfect_ratio = 0.1
    nice_ratio = 0.2
    good_ratio = 0.4
    bad_ratio = 0.45
    hit_group = (AccuracyGrade.Perfect, AccuracyGrade.Nice, AccuracyGrade.Good, AccuracyGrade.Bad, AccuracyGrade.Miss)
    success_group = (AccuracyGrade.Perfect, AccuracyGrade.Nice, AccuracyGrade.Good)
    fail_group = (AccuracyGrade.Miss, AccuracyGrade.Bad, AccuracyGrade.NoInput)
    @staticmethod
    def post_accuracy_map(hit_range_tick: int, perfect: float, nice: float, good: float, bad: float):
        Judgement.hit_range_tick = hit_range_tick
        Judgement.perfect_ratio = perfect
        Judgement.nice_ratio = nice
        Judgement.good_ratio = good
        Judgement.bad_ratio = bad
        pass

    @staticmethod
    def check_accuracy(difference):
        if abs(difference) > Judgement.hit_range_tick:
            return AccuracyGrade.Ignore
        else:
            ratio = abs(difference / Judgement.hit_range_tick)
            if 0 <= ratio < Judgement.perfect_ratio:
                return AccuracyGrade.Perfect
                pass
            elif Judgement.perfect_ratio <= ratio < Judgement.nice_ratio:
                return AccuracyGrade.Nice
                pass
            elif Judgement.nice_ratio <= ratio < Judgement.good_ratio:
                return AccuracyGrade.Good
                pass
            elif Judgement.good_ratio <= ratio < Judgement.bad_ratio:
                return AccuracyGrade.Bad
                pass
            elif Judgement.bad_ratio <= ratio <= 1:
                return AccuracyGrade.Miss
                pass
        pass

    @staticmethod
    def check_no_input(difference):
        return difference / Judgement.hit_range_tick < -Judgement.bad_ratio

    @staticmethod
    def is_hit(accuracy: AccuracyGrade):
        return accuracy in Judgement.hit_group

    @staticmethod
    def is_success(accuracy: AccuracyGrade):
        return accuracy in Judgement.success_group

    @staticmethod
    def is_fail(accuracy: AccuracyGrade):
        return accuracy in Judgement.fail_group


class Accuracy:
    def __init__(self, difference=None):
        if difference is not None:
            self.judge(difference)
        else:
            self.difference = 0
            self.grade = AccuracyGrade.Ignore

    def judge(self, difference, input_type: InputType, note_type: InputType):
        self.difference = difference
        self.grade = Judgement.check_accuracy(self.difference)
        if self.is_hit() and input_type != note_type:
            self.grade = AccuracyGrade.Miss

    def is_ignore(self):
        return self.grade == AccuracyGrade.Ignore

    def is_hit(self):
        return Judgement.is_hit(self.grade)

    def is_success(self):
        return Judgement.is_success(self.grade)

    def is_fail(self):
        return Judgement.is_fail(self.grade)

    def is_gone(self):
        return self.difference < -Judgement.hit_range_tick or self.grade != AccuracyGrade.Ignore

    def check_no_input(self, difference):
        if self.grade == AccuracyGrade.Ignore and Judgement.check_no_input(difference) == True:
            self.grade = AccuracyGrade.NoInput
            self.difference = 0
            return True
        return False

