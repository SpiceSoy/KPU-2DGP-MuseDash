from ..game_object.accuracy import *


class Combo:
    def __init__(self):
        self.now_combo = 0
        self.max_combo = 0

    def plus_combo(self):
        self.now_combo += 1
        self.max_combo = max(self.now_combo, self.max_combo)

    def break_combo(self):
        self.now_combo = 0

    def is_zero(self):
        return self.now_combo == 0

    def __str__(self):
        return f"current_combo : {self.now_combo} / max_combo : {self.max_combo}"