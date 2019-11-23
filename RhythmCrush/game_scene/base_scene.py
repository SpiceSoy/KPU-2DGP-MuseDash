from ..utill.game_timer import *
from ..utill.input_manager import *
from ..interface import IUpdatableObject
from ..interface import IDrawableObject
from ..game_object.game_world import GameWorld


class BaseScene(IUpdatableObject, IDrawableObject):
    def __init__(self, framework):
        self.framework = framework
        self.is_active = False
        self.timer = Timer()
        self.input_handler = InputHandlerManager(framework)
        self.is_loaded = False
        self.game_world = GameWorld()

    def load(self):
        self.is_loaded = True
        self.post_handler()
        self.game_world.load()

    def start(self):
        self.timer.start()
        self.is_active = True
        if not self.is_loaded:
            self.load()

    def resume(self):
        self.timer.resume()
        self.is_active = True

    def pause(self):
        self.timer.pause()
        self.is_active = False

    def stop(self):
        self.timer.stop()
        self.is_active = False
        print("stopopop")

    def handle_input(self):
        self.input_handler.handle_event()

    def update(self, delta_time):
        self.game_world.update(delta_time)

    def draw(self):
        self.game_world.draw()

    def post_handler(self):
        pass
