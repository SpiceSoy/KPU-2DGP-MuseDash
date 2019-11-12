from ..game_scene.base_scene import BaseScene

from .. import handler_set
from ..ui import *


import pico2d


class ClearScene(BaseScene):
    normal_text_color = (83, 83, 83)

    def __init__(self, framework, score: int, accuracy: int):
        super().__init__(framework)
        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-clear-back')
        self.ui_score_text = UIText(480, self.framework.h - 260, f"SCORE: {score}", FontType.Fixedsys,
                                    pt=60, color=ClearScene.normal_text_color)
        self.ui_accuracy_text = UIText(480, self.framework.h - 260 - 60, f"ACCURACY: {accuracy} %", FontType.Fixedsys,
                                       pt=60, color=ClearScene.normal_text_color)
        self.block_input_timer = 1
        self.game_world.add_object(self.background_image, 0)
        self.game_world.add_object(self.ui_score_text, 1)
        self.game_world.add_object(self.ui_accuracy_text, 1)

    def update(self, delta_time):
        self.block_input_timer -= delta_time

    def post_handler(self):
        # 콜백 함수 시작
        def game_end():
            if self.block_input_timer < 0:
                self.framework.exit()

        def move_menu():
            if self.block_input_timer < 0:
                from ..game_scene.title_scene import TitleScene
                self.framework.change_scene(TitleScene(self.framework))
        # 콜백 함수 종료

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
