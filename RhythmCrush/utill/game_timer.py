import time


def tick_to_sec(tick):
    return tick / 1000


def sec_to_tick(sec):
    return sec * 1000.0


class Timer:
    def __init__(self):
        self.is_active = False
        self.is_pause = False
        self.start_time = -1
        self.pause_time = 0
        self.pause_duration = 0

    def get_time_sec(self):
        return (time.time() - self.start_time) - self.pause_duration

    def get_time_tick(self):
        return sec_to_tick(self.get_time_sec())

    def start(self):
        self.start_time = time.time()
        self.is_active = True

    def stop(self):
        self.start_time = 0
        self.pause_time = 0
        self.pause_duration = 0
        self.is_pause = False
        self.is_active = False

    def pause(self):
        if self.is_active is True and self.is_pause is False:
            self.pause_time = time.time()
            print(f"pause_time is {self.pause_time}")
            self.is_pause = True

    def resume(self):
        if self.is_active is True and self.is_pause is True:
            self.pause_duration = self.pause_duration + (time.time() - self.pause_time)
            print(f"pause_duration is {self.pause_duration}")
            self.is_pause = False
