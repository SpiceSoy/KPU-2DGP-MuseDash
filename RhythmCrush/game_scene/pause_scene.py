from ..game_scene.base_scene import BaseScene

from .. import handler_set
from ..ui import *


import pico2d


class PauseScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.csr_x = [
            544,
            594,
            594
        ]
        self.csr_y = [
            framework.h - 390,
            framework.h - 497,
            framework.h - 604,
        ]
        self.button = [
            ClickableRect(720, framework.h - 390, 325, 102),
            ClickableRect(720, framework.h - 497, 325, 102),
            ClickableRect(720, framework.h - 604, 325, 102)
        ]
        self.csr = 0
        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-pause-back')
        self.csr_image = UIStaticImage(560, self.csr_y[self.csr], 'ui-csr-small')
        self.game_world.add_object(self.background_image, 0)
        self.game_world.add_object(self.csr_image, 1)

    def load(self):
        super().load()

    def update(self, delta_time):
        self.csr_image.position[0] = self.csr_x[self.csr]
        self.csr_image.position[1] = self.csr_y[self.csr]

    def draw(self):
        self.framework.get_index_stack(-2).draw()
        super().draw()

    def post_handler(self):
        # 콜백 함수 시작
        def game_end():
            self.framework.exit()

        def return_game():
            self.framework.pop_scene()

        def arrow_up():
            self.csr = pico2d.clamp(0, self.csr-1, 2)

        def arrow_down():
            self.csr = pico2d.clamp(0, self.csr+1, 2)

        def set_csr(csr):
            def ret():
                self.csr = csr
            return ret

        def move_menu():
            from ..game_scene.title_scene import TitleScene
            self.framework.change_scene(TitleScene(self.framework))

        def menu_func():
            print(self.csr)
            if self.csr == 2:
                game_end()
            elif self.csr == 1:
                move_menu()
            elif self.csr == 0:
                return_game()
                pass
        # 콜백 함수 종료

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, return_game)
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
            handler_set.mouse_motion_input(set_csr(0), self.button[0])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEMOTION,
            handler_set.mouse_motion_input(set_csr(1), self.button[1])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEMOTION,
            handler_set.mouse_motion_input(set_csr(2), self.button[2])
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
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, menu_func, self.button[0])
        )
        self.input_handler.add_handler(
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, menu_func, self.button[2])
        )
