from ..game_scene.base_scene import BaseScene

from .. import handler_set
from ..ui import *

import pico2d


class TitleScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.csr = 0
        self.csr_y = [
            framework.h - 561,
            framework.h - 690
        ]
        self.button = [
            ClickableRect(1162, framework.h - 561, 350, 120),
            ClickableRect(1162, framework.h - 690, 350, 120)
        ]
        self.title_image = UIStaticImage(self.framework.w/2, self.framework.h/2, 'ui-title-back')
        self.csr_image = UIStaticImage(980, self.csr_y[self.csr], 'ui-csr')

        self.game_world.add_object(self.title_image, 0)
        self.game_world.add_object(self.csr_image, 1)

    def update(self, delta_time):
        self.csr_image.position[1] = self.csr_y[self.csr]
        super().update(delta_time)

    def post_handler(self):
        # 콜백 함수 선언 시작
        def game_end():
            self.framework.exit()

        def arrow_up():
            self.csr = pico2d.clamp(0, self.csr-1, 1)

        def arrow_down():
            self.csr = pico2d.clamp(0, self.csr+1, 1)

        # 고차 함수
        def get_csr_set_func(csr):
            def ret():
                self.csr = csr
            return ret

        def move_next_scene():
            from ..game_scene.select_scene import SelectScene
            self.framework.change_scene(SelectScene(self.framework))

        def menu_enter_func():
            if self.csr == 1:
                self.framework.exit()
            elif self.csr == 0:
                move_next_scene()
        # 콜백 함수 선언 종료

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
            handler_set.key_input(pico2d.SDLK_RETURN, menu_enter_func)
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, menu_enter_func, self.button[1])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, move_next_scene, self.button[0])
        )
