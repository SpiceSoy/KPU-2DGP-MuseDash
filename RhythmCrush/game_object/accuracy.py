import enum


class Accuracy(enum.Enum):
    Perfect = 3
    Nice = 2
    Good = 1
    Ignore = 0
    Bad = -1
    Miss = -2


class Judgement:
    hit_range_tick = 250
    perfect_ratio = 0.2
    nice_ratio = 0.2
    good_ratio = 0.2
    bad_ratio = 0.2
    @staticmethod
    def post_accuracy_map(hit_range_tick: int, perfect: float, nice: float, good: float, bad: float):
        Judgement.hit_range_tick = hit_range_tick
        Judgement.perfect_ratio = perfect
        Judgement.nice_ratio = nice
        Judgement.good_ratio = good
        Judgement.bad_ratio = bad
        pass

    @staticmethod
    def check_accuracy(music_tick, now_tick):
        difference = music_tick - now_tick
        if abs(difference) > Judgement.hit_range_tick:
            return Accuracy.Ignore
        else:
            ratio = abs(difference / Judgement.hit_range_tick)
            if ratio in range(0, Judgement.perfect_ratio):
                return Accuracy.Perfect
                pass
            elif ratio in range(Judgement.perfect_ratio, Judgement.nice_ratio):
                return Accuracy.Nice
                pass
            elif ratio in range(Judgement.nice_ratio, Judgement.good_ratio):
                return Accuracy.Good
                pass
            elif ratio in range(Judgement.good_ratio, Judgement.bad_ratio):
                return Accuracy.Bad
                pass
            elif ratio in range(Judgement.bad_ratio, 1):
                return Accuracy.Miss
                pass
        pass
