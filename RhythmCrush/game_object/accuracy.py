import enum


class Accuracy(enum.Enum):
    Perfect = 3
    Nice = 2
    Good = 1
    Ignore = 0
    Bad = -1
    Miss = -2


class Judgement:
    hit_range_tick = 150
    perfect_ratio = 0.2
    nice_ratio = 0.3
    good_ratio = 0.4
    bad_ratio = 0.1
    @staticmethod
    def post_accuracy_map(hit_range_tick: int, perfect: float, nice: float, good: float, bad: float):
        Judgement.hit_range_tick = hit_range_tick
        Judgement.perfect_ratio = perfect
        Judgement.nice_ratio = nice
        Judgement.good_ratio = good
        Judgement.bad_ratio = bad
        pass

    @staticmethod
    def check_accuracy(map_tick, now_tick):
        difference = map_tick - now_tick
        # print(difference)
        if abs(difference) > Judgement.hit_range_tick:
            return Accuracy.Ignore
        else:
            ratio = abs(difference / Judgement.hit_range_tick)
            if 0 <= ratio < Judgement.perfect_ratio:
                return Accuracy.Perfect
                pass
            elif Judgement.perfect_ratio <= ratio < Judgement.nice_ratio:
                return Accuracy.Nice
                pass
            elif Judgement.nice_ratio <= ratio < Judgement.good_ratio:
                return Accuracy.Good
                pass
            elif Judgement.good_ratio <= ratio < Judgement.bad_ratio:
                return Accuracy.Bad
                pass
            elif Judgement.bad_ratio <= ratio < 1:
                return Accuracy.Miss
                pass
        pass

    @staticmethod
    def is_hit(accuracy: Accuracy):
        return accuracy == Accuracy.Perfect or accuracy == Accuracy.Good or accuracy == Accuracy.Nice
