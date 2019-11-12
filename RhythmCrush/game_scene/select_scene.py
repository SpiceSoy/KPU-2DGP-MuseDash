from ..game_scene.base_scene import BaseScene

from RhythmCrush.component import music_meta_data
from ..utill import ResourceData

from .. import handler_set
from ..ui import *

import pico2d


def summarize_text(text: str, max_length: int):
    if len(text) > max_length:
        summarized_text = text[:max_length-2] + "..."
    else:
        summarized_text = text
    return summarized_text


class SelectScene(BaseScene):
    normal_text_color = (83, 83, 83)
    inactive_text_color = (183, 183, 183)

    def __init__(self, framework):
        super().__init__(framework)
        self.csr_music = 0
        self.csr_y = [self.framework.h - 412, self.framework.h - 502, self.framework.h - 592]
        self.csr_difficult = -1
        self.music_list = music_meta_data.load_music_metadata_list(ResourceData.music_metadata_url)

        self.select_button = [
            ClickableRect(30, self.framework.h - 249 - 48 * i, 900, 72 + 4) for i in range(len(self.music_list))
        ]
        self.difficult_button = [
            ClickableRect(1028, self.framework.h - 412, 500, 72 + 4),
            ClickableRect(1028, self.framework.h - 502, 500, 72 + 4),
            ClickableRect(1028, self.framework.h - 592, 500, 72 + 4),
        ]

        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-select-back')
        self.csr_image = UIStaticImage(1010, self.csr_y[0], 'ui-csr-72')
        self.ui_music_list = [
            UIText(30, self.framework.h - 249 - 48 * i, f"{i}. {self.music_list[i].title}", FontType.Fixedsys, pt=48,
                   color=(83, 83, 83))
            for i in range(len(self.music_list))
        ]
        self.ui_title_text = UIText(608, self.framework.h - 260, self.music_list[0].title, FontType.Fixedsys,
                                    pt=72, color=(83, 83, 83))
        self.ui_artist_text = UIText(608, self.framework.h - 308, self.music_list[0].artist, FontType.Fixedsys,
                                     pt=48, color=(83, 83, 83))
        self.ui_difficult_normal_text = UIText(1028, self.framework.h - 412, "NORMAL", FontType.Fixedsys,
                                               pt=72, color=SelectScene.normal_text_color)
        self.ui_difficult_hard_text = UIText(1028, self.framework.h - 502, "HARD", FontType.Fixedsys,
                                             pt=72, color=SelectScene.normal_text_color)
        self.ui_difficult_extreme_text = UIText(1028, self.framework.h - 592, "EXTREME", FontType.Fixedsys,
                                                pt=72, color=SelectScene.normal_text_color)

        self.game_world.add_object(self.background_image, 0)
        self.game_world.add_object(self.csr_image, 2)
        self.game_world.add_object(self.ui_title_text, 1)
        self.game_world.add_object(self.ui_artist_text, 1)
        self.game_world.add_object(self.ui_difficult_normal_text, 1)
        self.game_world.add_object(self.ui_difficult_hard_text, 1)
        self.game_world.add_object(self.ui_difficult_extreme_text, 1)
        for obj in self.ui_music_list:
            self.game_world.add_object(obj, 1)

    def update(self, delta_time):
        for i in range(len(self.ui_music_list)):
            title = summarize_text(self.music_list[i].title, 15)
            if i == self.csr_music:
                self.ui_music_list[i].update_text(f">  {title}")
            else:
                self.ui_music_list[i].update_text(f"{i + 1}. {title}")

        title = summarize_text(self.music_list[self.csr_music].title, 19)

        self.ui_title_text.update_text(title)
        self.ui_artist_text.update_text(self.music_list[self.csr_music].artist)

        self.ui_difficult_normal_text.change_color(
            self.normal_text_color if self.music_list[self.csr_music].has_normal() else self.inactive_text_color
        )
        self.ui_difficult_hard_text.change_color(
            self.normal_text_color if self.music_list[self.csr_music].has_hard() else self.inactive_text_color
        )
        self.ui_difficult_extreme_text.change_color(
            self.normal_text_color if self.music_list[self.csr_music].has_extreme() else self.inactive_text_color
        )

        if self.csr_difficult != -1:
            self.csr_image.position[1] = self.csr_y[self.csr_difficult]
            self.csr_image.is_visible = True
        else:
            self.csr_image.is_visible = False

    def post_handler(self):
        # 콜백 함수 시작
        def arrow_up():
            if self.csr_difficult == -1:
                self.csr_music = pico2d.clamp(0, self.csr_music - 1, len(self.music_list)-1)
            else:
                # 앞의 난이도로 이동
                difficult_list = self.music_list[self.csr_music].get_difficult_csr_list()
                self.csr_difficult = difficult_list[difficult_list.index(self.csr_difficult) - 1]

        def arrow_down():
            if self.csr_difficult == -1:
                self.csr_music = pico2d.clamp(0, self.csr_music + 1, len(self.music_list)-1)
            else:
                # 뒤의 난이도로 이동
                difficult_list = self.music_list[self.csr_music].get_difficult_csr_list()
                self.csr_difficult = difficult_list[(difficult_list.index(self.csr_difficult) + 1) % len(difficult_list)]

        def escape():
            if self.csr_difficult == -1:
                from ..game_scene.title_scene import TitleScene
                self.framework.change_scene(TitleScene(self.framework))
            else:
                self.csr_difficult = -1

        def enter():
            if self.csr_difficult == -1:
                self.csr_difficult = self.music_list[self.csr_music].get_difficult_csr_list()[0]
            else:
                from ..game_scene.game_map import NotePlayScene
                self.framework.change_scene(
                    NotePlayScene(self.framework, self.music_list[self.csr_music].get_difficult_url(self.csr_difficult))
                )

        def get_music_csr_set_func(csr):
            def ret():
                self.csr_music = csr
                self.csr_difficult = -1
            return ret

        def get_difficult_csr_set_func(csr):
            def ret():
                if self.music_list[self.csr_music].has_difficult(csr):
                    self.csr_difficult = csr
            return ret
        # 콜백 함수 종료

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
                handler_set.mouse_motion_input(get_music_csr_set_func(i), self.select_button[i])
            )

        for i in range(len(self.difficult_button)):
            self.input_handler.add_handler(
                pico2d.SDL_MOUSEMOTION,
                handler_set.mouse_motion_input(get_difficult_csr_set_func(i), self.difficult_button[i])
            )
        for i in range(len(self.difficult_button)):
            self.input_handler.add_handler(
                pico2d.SDL_MOUSEBUTTONDOWN,
                handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, enter, self.difficult_button[i])
            )