from ..utill.game_timer import *
from ..utill.input_manager import *
from ..interface import IUpdatableObject
from ..interface import IDrawableObject

from .. import debug


class BaseScene(IUpdatableObject, IDrawableObject):
    def __init__(self, framework):
        self.framework = framework
        self.is_active = False
        self.timer = Timer()
        self.input_handler = InputHandlerManager(framework)

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

    def handle_input(self):
        self.input_handler.handle_event()

    def update(self, delta_time):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()


