from ..utill.game_timer import *
from ..interface import IUpdatableObject
from ..interface import IDrawableObject

from .. import debug


class BaseScene(IUpdatableObject, IDrawableObject):
    def __init__(self, framework):
        self.framework = framework
        self.is_active = False
        self.timer = Timer()

    def load(self):
        pass

    def start(self):
        self.timer.start()
        self.is_active = True

    def resume(self):
        self.timer.resume()
        self.is_active = True

    def pause(self):
        self.timer.pause()
        self.is_active = False

    def stop(self):
        self.timer.stop()
        self.is_active = False

    def update(self, delta_time):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()


