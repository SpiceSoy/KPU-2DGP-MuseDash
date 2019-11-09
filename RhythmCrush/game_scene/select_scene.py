from ..game_scene.base_scene import BaseScene
from ..game_scene import title_scene
from ..game_scene import game_map

from ..utill import music_meta_data
from ..utill import ResourceData

from .. import handler_set
from ..ui import *

import pico2d


class SelectScene(BaseScene):
    text_normal_color = (83, 83, 83)
    text_unvisible_color = (183, 183, 183)

    def __init__(self, framework):
        super().__init__(framework)
        self.csr_music = 0
        self.failed_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-select-back')
        # self.csr_image = UIStaticImage(560, self.csr_y[self.csr], 'ui-csr-48')
        self.csr_y = [self.framework.h - 412, self.framework.h - 502, self.framework.h - 592]
        self.csr_image = UIStaticImage(1010, self.csr_y[0], 'ui-csr-72')
        self.csr_difficult = -1
        self.music_list = []

    def load(self):
        self.failed_image.load()
        self.csr_image.load()
        self.music_list = music_meta_data.load_music_metadata_list(ResourceData.music_metadata_url)
        self.ui_music_list = [
            UIText(30, self.framework.h - 249 - 48 * i, f"{i}. {self.music_list[i].title}", FontType.Fixedsys, pt=48,
                   color=(83, 83, 83))
            for i in range(len(self.music_list))
        ]
        self.select_button = [
            ClickableRect(30, self.framework.h - 249 - 48 * i, 900, 72 + 4) for i in range(len(self.music_list))
        ]
        self.ui_title_text = UIText(608, self.framework.h - 260, self.music_list[0].title, FontType.Fixedsys, pt=72,
                                    color=(83, 83, 83))
        self.ui_artist_text = UIText(608, self.framework.h - 308, self.music_list[0].artist, FontType.Fixedsys, pt=48,
                                     color=(83, 83, 83))
        for ui in self.ui_music_list:
            ui.load()
        self.ui_title_text.load()
        self.ui_artist_text.load()
        self.ui_difficult_normal_text = UIText(1028, self.framework.h - 412, "NORMAL", FontType.Fixedsys, pt=72,
                                               color=(83, 83, 83))
        self.ui_difficult_hard_text = UIText(1028, self.framework.h - 502, "HARD", FontType.Fixedsys, pt=72,
                                             color=(83, 83, 83))
        self.ui_difficult_extreme_text = UIText(1028, self.framework.h - 592, "EXTREME", FontType.Fixedsys, pt=72,
                                                color=(83, 83, 83))
        self.difficult_button = [
            ClickableRect(1028, self.framework.h - 412, 500, 72 + 4),
            ClickableRect(1028, self.framework.h - 502, 500, 72 + 4),
            ClickableRect(1028, self.framework.h - 592, 500, 72 + 4),
        ]
        self.ui_difficult_normal_text.load()
        self.ui_difficult_hard_text.load()
        self.ui_difficult_extreme_text.load()
        super().load()

    def update(self, delta_time):
        for i in range(len(self.ui_music_list)):
            if i == self.csr_music:
                title = self.music_list[i].title
                if len(title) > 15:
                    title = title[0:13] + "..."
                self.ui_music_list[i].update_text(f">  {title}")
            else:
                title = self.music_list[i].title
                if len(title) > 15:
                    title = title[:13] + "..."
                self.ui_music_list[i].update_text(f"{i + 1}. {title}")

        title = self.music_list[self.csr_music].title
        if len(title) > 19:
            title = title[:17] + "..."
        self.ui_title_text.update_text(title)
        self.ui_artist_text.update_text(self.music_list[self.csr_music].artist)

        self.ui_difficult_normal_text.change_color(
            self.text_normal_color if self.music_list[self.csr_music].has_normal() else self.text_unvisible_color)
        self.ui_difficult_hard_text.change_color(
            self.text_normal_color if self.music_list[self.csr_music].has_hard() else self.text_unvisible_color)
        self.ui_difficult_extreme_text.change_color(
            self.text_normal_color if self.music_list[self.csr_music].has_extreme() else self.text_unvisible_color)
        if self.csr_difficult != -1:
            self.csr_image.position[1] = self.csr_y[self.csr_difficult]
        pass

    def draw(self):
        self.failed_image.draw()
        for ui in self.ui_music_list:
            ui.draw()
        self.ui_title_text.draw()
        self.ui_artist_text.draw()
        # self.csr_image.draw()
        self.ui_difficult_normal_text.draw()
        self.ui_difficult_hard_text.draw()
        self.ui_difficult_extreme_text.draw()
        if self.csr_difficult != -1:
            self.csr_image.draw()

    def post_handler(self):
        def game_end():
            self.framework.exit()

        def arrow_up():
            if self.csr_difficult == -1:
                self.csr_music = pico2d.clamp(0, self.csr_music - 1, len(self.music_list)-1)
            else:
                difficult_list = self.music_list[self.csr_music].get_difficult_csr_list()
                self.csr_difficult = difficult_list[difficult_list.index(self.csr_difficult) - 1]

        def arrow_down():
            if self.csr_difficult == -1:
                self.csr_music = pico2d.clamp(0, self.csr_music + 1, len(self.music_list)-1)
            else:
                difficult_list = self.music_list[self.csr_music].get_difficult_csr_list()
                self.csr_difficult = difficult_list[(difficult_list.index(self.csr_difficult) + 1) % len(difficult_list)]

        def escape():
            if self.csr_difficult == -1:
                self.framework.change_scene(title_scene.TitleScene(self.framework))
            else:
                self.csr_difficult = -1

        def enter():
            if self.csr_difficult == -1:
                self.csr_difficult = difficult_list = self.music_list[self.csr_music].get_difficult_csr_list()[0]
            else:
                self.framework.change_scene(
                    game_map.NotePlayScene(self.framework, self.music_list[self.csr_music].get_difficult_url(self.csr_difficult))
                )
                pass

        def set_music_csr(csr):
            def ret():
                self.csr_music = csr
                self.csr_difficult = -1
            return ret

        def set_difficult_csr(csr):
            def ret():
                if self.music_list[self.csr_music].has_difficult(csr):
                    self.csr_difficult = csr
            return ret

        def move_menu():
            self.framework.change_scene(
                title_scene.TitleScene(self.framework)
            )

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, escape)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_RETURN, enter)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, arrow_up)
        )
        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, arrow_down)
        )
        for i in range(len(self.select_button)):
            self.input_handler.add_handler(
                pico2d.SDL_MOUSEMOTION,
                handler_set.mouse_motion_input(set_music_csr(i), self.select_button[i])
            )

        for i in range(len(self.difficult_button)):
            self.input_handler.add_handler(
                pico2d.SDL_MOUSEMOTION,
                handler_set.mouse_motion_input(set_difficult_csr(i), self.difficult_button[i])
            )
        for i in range(len(self.difficult_button)):
            self.input_handler.add_handler(
                pico2d.SDL_MOUSEBUTTONDOWN,
                handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, enter, self.difficult_button[i])
            )
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
