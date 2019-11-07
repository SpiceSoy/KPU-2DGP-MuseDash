from ..game_scene.base_scene import BaseScene
from ..game_scene import title_scene

from .. import handler_set
from ..ui import *

import pico2d


class SelectScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        # self.csr_x = [
        #     544,
        #     594,
        #     594
        # ]
        # self.csr_y = [
        #     framework.h - 390,
        #     framework.h - 497,
        #     framework.h - 604,
        # ]
        # self.button = [
        #     ClickableRect(720, framework.h - 390, 325, 102),
        #     ClickableRect(720, framework.h - 497, 325, 102),
        #     ClickableRect(720, framework.h - 604, 325, 102)
        # ]
        self.csr_music = 0
        # self.csr_difficult = 0
        self.failed_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-select-back')
        # self.csr_image = UIStaticImage(560, self.csr_y[self.csr], 'ui-csr-48')
        # self.csr_image = UIStaticImage(560, self.csr_y[self.csr], 'ui-csr-72')
        self.music_list = {
            "Max Burnning!!": "Resource/Map/Third/BlackY - Max Burning!! (SpectorDG) [Senritsu's Futsuu].osu",
            "Chirality": "Resource/Map/Third/BlackY - Max Burning!! (SpectorDG) [Senritsu's Futsuu].osu",
            "Exit This Earth's Atomosphere": "Resource/Map/Third/BlackY - Max Burning!! (SpectorDG) [Senritsu's Futsuu].osu"
        }
        self.ui_music_list = [
            UIText(30, self.framework.h - 249 - 48 * i, f"{i}. {list(self.music_list.values())[i]}", FontType.Fixedsys, pt=48, color=(83, 83, 83))
            for i in range(len(self.music_list))
        ]

    def load(self):
        super().load()
        self.failed_image.load()
        for ui in self.ui_music_list:
            ui.load()
        # self.csr_image.load()

    def update(self, delta_time):
        for i in range(len(self.ui_music_list)):
            if i == self.csr_music:
                title = list(self.music_list.keys())[i]
                if len(title) > 15:
                    title = title[0:13] + "..."
                self.ui_music_list[i].update_text(f">  {title}")
            else:
                title = list(self.music_list.keys())[i]
                if len(title) > 15:
                    title = title[:13] + "..."
                self.ui_music_list[i].update_text(f"{i + 1}. {title}")
        # self.csr_image.position[0] = self.csr_x[self.csr]
        # self.csr_image.position[1] = self.csr_y[self.csr]
        pass

    def draw(self):
        self.failed_image.draw()
        for ui in self.ui_music_list:
            ui.draw()
        # self.csr_image.draw()

    def post_handler(self):
        def game_end():
            self.framework.exit()

        def arrow_up():
            self.csr_music = pico2d.clamp(0, self.csr_music - 1, 2)

        def arrow_down():
            self.csr_music = pico2d.clamp(0, self.csr_music + 1, 2)

        def set_csr(csr):
            def ret():
                self.csr = csr

            return ret

        def move_menu():
            self.framework.change_scene(
                title_scene.TitleScene(self.framework)
            )

        def menu_func():
            print(self.csr)
            if self.csr == 2:
                self.framework.exit()
            elif self.csr == 1:
                move_menu()
            elif self.csr == 0:
                self.framework.pop_scene()
                pass

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, move_menu)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, arrow_up)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, arrow_down)
        )
        # self.input_handler.add_handler(
        #     pico2d.SDL_MOUSEMOTION,
        #     handler_set.mouse_motion_input(set_csr(0), self.button[0])
        # )
        # self.input_handler.add_handler(
        #     pico2d.SDL_MOUSEMOTION,
        #     handler_set.mouse_motion_input(set_csr(1), self.button[1])
        # )
        # self.input_handler.add_handler(
        #     pico2d.SDL_MOUSEMOTION,
        #     handler_set.mouse_motion_input(set_csr(2), self.button[2])
        # )
        # self.input_handler.add_handler(
        #     pico2d.SDL_KEYDOWN,
        #     handler_set.key_input(pico2d.SDLK_RETURN, menu_func)
        # )
        # self.input_handler.add_handler(
        #     pico2d.SDL_MOUSEBUTTONDOWN,
        #     handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, menu_func, self.button[1])
        # )
        # self.input_handler.add_handler(
        #     pico2d.SDL_MOUSEBUTTONDOWN,
        #     handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, move_menu, self.button[0])
        # )
        pass
