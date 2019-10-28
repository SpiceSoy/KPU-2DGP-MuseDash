from ..game_scene.base_scene import BaseScene

from .. import handler_set
from ..ui import *

import pico2d


class TitleScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.title_image = None

    def load(self):
        self.title_image = UIStaticImage(self.framework.w/2, self.framework.h/2, 'ui-title-back')

    def update(self, delta_time):
        pass

    def draw(self):
        self.title_image.draw()

    def post_handler(self):
        def game_end():
            self.framework.exit()

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, game_end)
        )
        pass
