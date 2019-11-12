from ..game_scene.base_scene import BaseScene

from .. import handler_set
from ..ui import *


import pico2d


class FailScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.csr = 0
        self.csr_y = [
            framework.h - 561,
            framework.h - 690
        ]
        self.button = [
            ClickableRect(720, framework.h - 561, 350, 120),
            ClickableRect(720, framework.h - 690, 350, 120)
        ]
        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-fail-back')
        self.csr_image = UIStaticImage(560, self.csr_y[self.csr], 'ui-csr')
        self.game_world.add_object(self.background_image, 0)
        self.game_world.add_object(self.csr_image, 1)

    def update(self, delta_time):
        self.csr_image.position[1] = self.csr_y[self.csr]

    def post_handler(self):
        # 콜백 함수 시작
        def game_end():
            self.framework.exit()

        def arrow_up():
            self.csr = pico2d.clamp(0, self.csr-1, 1)

        def arrow_down():
            self.csr = pico2d.clamp(0, self.csr+1, 1)

        def get_csr_set_func(csr):
            def ret():
                self.csr = csr
            return ret

        def move_menu():
            from ..game_scene.title_scene import TitleScene
            self.framework.change_scene(TitleScene(self.framework))

        def menu_func():
            if self.csr == 1:
                self.framework.exit()
            elif self.csr == 0:
                move_menu()
        #콜백 함수 종료

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, game_end)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, arrow_up)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, arrow_down)
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEMOTION,
            handler_set.mouse_motion_input(get_csr_set_func(0), self.button[0])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEMOTION,
            handler_set.mouse_motion_input(get_csr_set_func(1), self.button[1])
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_RETURN, menu_func)
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, menu_func, self.button[1])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, move_menu, self.button[0])
        )
