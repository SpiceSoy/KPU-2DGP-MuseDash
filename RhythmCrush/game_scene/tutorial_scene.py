from ..game_scene.base_scene import BaseScene
from .. import handler_set
from ..ui import *

import pico2d


class TutorialScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-tutorial-back')
        self.game_world.add_object(self.background_image, 0)
        self.block_input_timer = 2

    def draw(self):
        self.framework.get_index_stack(-2).draw()
        super().draw()

    def update(self, delta_time):
        self.block_input_timer -= delta_time
        if self.block_input_timer < -1:
            self.framework.pop_scene()

    def post_handler(self):
        def move_menu():
            if self.block_input_timer < 0:
                self.framework.pop_scene()

        # 콜백 함수 종료

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_RETURN, move_menu)
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, move_menu)
        )

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, move_menu)
        )
