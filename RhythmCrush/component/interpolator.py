from RhythmCrush.interface import IUpdatableObject


class BaseInterpolator(IUpdatableObject):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.current_value = self.src

    def update(self, delta_time):
        raise NotImplementedError()

    def get_current_value(self):
        return self.current_value

    @staticmethod
    def interpolator(src, dest, t, t_max=1.0):
        return (1-(t/t_max)) * src + (t/t_max) * dest


# 고정 완료시간
class FixedTimeInterpolator(BaseInterpolator):
    def __init__(self, src, dest, time=1):
        super().__init__(src, dest)
        self.time = time
        self.t = 0

    def update(self, delta_time):
        self.current_value = super().interpolator(self.src, self.dest, self.t)
        self.t += self.speed * delta_time


# 고정 비율 완료시간
class FixedRatioInterpolator(BaseInterpolator):
    def __init__(self, src, dest, ratio=0.25):
        super().__init__(src, dest)
        self.ratio = ratio

    def update(self, delta_time):
        self.current_value = super().interpolator(self.src, self.dest, self.ratio)
        if abs(self.current_value - self.dest) < 0.001:
            self.current_value = self.dest
            self.src = self.dest
        self.src = self.current_value


# 고정 속도
class FixedSpeedInterpolator(BaseInterpolator):
    def __init__(self, src, dest, speed):
        super().__init__(src, dest)
        self.speed = speed
        self.complete_time = abs(dest-src/speed)
        self.time = 0

    def update(self, delta_time):
        self.current_value = super().interpolator(self.src, self.dest, self.time/self.complete_time)
        self.time += delta_time
