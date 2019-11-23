import time


def tick_to_sec(tick):
    return tick / 1000


def sec_to_tick(sec):
    return sec * 1000.0

# # 겟 타임시 실제 시간 계산
# class Timer:
#     def __init__(self):
#         self.is_active = False
#         self.is_pause = False
#         self.start_time = -1
#         self.pause_time = 0
#         self.pause_duration = 0
#
#     def get_time_sec(self):
#         return (time.time() - self.start_time) - self.pause_duration
#
#     def get_time_tick(self):
#         return sec_to_tick(self.get_time_sec())
#
#     def start(self):
#         self.is_active = True
#         self.start_time = time.time()
#
#     def stop(self):
#         self.start_time = 0
#         self.pause_time = 0
#         self.pause_duration = 0
#         self.is_pause = False
#         self.is_active = False
#
#     def pause(self):
#         if self.is_active is True and self.is_pause is False:
#             self.pause_time = time.time()
#             # print(f"pause_time is {self.pause_time}")
#             self.is_pause = True
#
#     def resume(self):
#         if self.is_active is True and self.is_pause is True:
#             self.pause_duration = self.pause_duration + (time.time() - self.pause_time)
#             # print(f"pause_duration is {self.pause_duration}")
#             self.is_pause = False

# # 업데이트 / 델타 타임 더하기로 실제 시간 계산
# class Timer:
#     def __init__(self):
#         self.is_active = False
#         self.is_pause = False
#         self.start_time = -1
#         self.pause_time = 0
#         self.pause_duration = 0
#         self.now_time = 0
#
#     def update(self,delta_time):
#         if self.is_pause:
#             self.pause_time += delta_time
#         else:
#             self.now_time += delta_time
#
#     def get_time_sec(self):
#         return self.now_time - self.pause_duration
#
#     def get_time_tick(self):
#         return sec_to_tick(self.get_time_sec())
#
#     def start(self):
#         self.is_active = True
#         self.start_time = time.time()
#
#     def stop(self):
#         self.start_time = 0
#         self.pause_time = 0
#         self.pause_duration = 0
#         self.is_pause = False
#         self.is_active = False
#
#     def pause(self):
#         if self.is_active is True and self.is_pause is False:
#             self.is_pause = True
#
#     def resume(self):
#         if self.is_active is True and self.is_pause is True:
#             self.is_pause = False

# 업데이트 / 업데이트에만 time.time
class Timer:
    def __init__(self):
        self.is_active = False
        self.is_pause = False
        self.start_time = -1
        self.pause_time = 0
        self.pause_duration = 0
        self.now_time = 0

    def update(self, delta_time):
        self.now_time = (time.time() - self.start_time)

    def get_time_sec(self):
        return self.now_time - self.pause_duration

    def get_time_tick(self):
        return sec_to_tick(self.get_time_sec())

    def start(self):
        self.is_active = True
        self.start_time = time.time()

    def stop(self):
        self.start_time = 0
        self.pause_time = 0
        self.pause_duration = 0
        self.is_pause = False
        self.is_active = False

    def pause(self):
        if self.is_active is True and self.is_pause is False:
            self.pause_time = time.time()
            self.is_pause = True

    def resume(self):
        if self.is_active is True and self.is_pause is True:
            self.pause_duration = self.pause_duration + (time.time() - self.pause_time)
            self.is_pause = False
