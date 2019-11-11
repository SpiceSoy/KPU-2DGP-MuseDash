from ..game_scene.base_scene import BaseScene
from ..game_scene import title_scene

from .. import handler_set
from ..ui import *


import pico2d


class ClearScene(BaseScene):
    def __init__(self, framework, score: int, accuracy: int):
        super().__init__(framework)
        self.clear_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-clear-back')
        self.ui_score_text = UIText(480, self.framework.h - 260, f"SCORE: {score}", FontType.Fixedsys, pt=60,
                                    color=(83, 83, 83))
        self.ui_accuracy_text = UIText(480, self.framework.h - 260 - 60, f"ACCURACY: {accuracy} %", FontType.Fixedsys, pt=60,
                                    color=(83, 83, 83))
        self.block_input_timer = 1

    def load(self):
        super().load()
        self.clear_image.load()
        self.ui_score_text.load()
        self.ui_accuracy_text.load()

    def update(self, delta_time):
        self.block_input_timer -= delta_time
        pass

    def draw(self):
        self.clear_image.draw()
        self.ui_score_text.draw()
        self.ui_accuracy_text.draw()

    def post_handler(self):
        def game_end():
            if self.block_input_timer < 0:
                self.framework.exit()

        def move_menu():
            if self.block_input_timer < 0:
                self.framework.change_scene(
                    title_scene.TitleScene(self.framework)
                )

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_RETURN, move_menu)
        )
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
            handler_set.key_input(pico2d.SDLK_ESCAPE, game_end)
        )

        pass
