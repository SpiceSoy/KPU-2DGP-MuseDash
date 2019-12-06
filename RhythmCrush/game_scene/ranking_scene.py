from ..game_scene.base_scene import BaseScene
from ..component import ranking
from .. import handler_set
from ..ui import *


import pico2d


class RankingScene(BaseScene):
    normal_text_color = (83, 83, 83)
    match_text_color = (170, 0, 0)
    difficult_text = ["NORMAL", "HARD", "EXTREME"]

    def __init__(self, framework, music_name, difficult, score: int, accuracy: int, max_combo: int):
        super().__init__(framework)
        print("왜 두번 불려지냐")
        self.music_name = music_name
        self.difficult = difficult
        self.max_combo = max_combo
        self.background_image = UIStaticImage(self.framework.w / 2, self.framework.h / 2, 'ui-ranking-back')

        self.ui_rank_title = UIText(350, self.framework.h - 165,
                                    f"{self.music_name}",
                                    FontType.Fixedsys, pt=64 - max(0,len(self.music_name) - 18) * 2, color=RankingScene.normal_text_color)

        self.ui_rank_difficult = UIText(350, self.framework.h - 215,
                                    f"{RankingScene.difficult_text[int(self.difficult)]}",
                                    FontType.Fixedsys, pt=42, color=RankingScene.normal_text_color)

        raw_rank_data = ranking.get_rank_list(self.music_name, str(self.difficult))

        now_rank_data = ranking.RankData()
        now_rank_data.music_name = self.music_name
        now_rank_data.difficult = self.difficult
        now_rank_data.accuracy = accuracy
        now_rank_data.score = score
        now_rank_data.max_combo = self.max_combo
        now_rank_data.now = True
        raw_rank_data.append(now_rank_data)
        rank_data = sorted(raw_rank_data, key=lambda obj: obj.score, reverse=True)

        self.ranked_list = []
        for i in range(5):
            if i >= len(rank_data):
                break
            _cur_color = RankingScene.match_text_color if rank_data[i].now is True else RankingScene.normal_text_color
            _grade = UIText(365, self.framework.h - 270 - i * 90, f"{i+1}.",
                                    FontType.Fixedsys, pt=64, color=_cur_color)
            _score = UIText(465, self.framework.h - 270 - i * 90, f"{rank_data[i].score}",
                                    FontType.Fixedsys, pt=64, color=_cur_color)
            _combo = UIText(455, self.framework.h - 270 - i * 90 - 45, f"MAX HIT : {rank_data[i].max_combo}",
                                    FontType.Fixedsys, pt=32, color=_cur_color)
            _acc = UIText(365, self.framework.h - 270 - i * 90 - 45, f"{rank_data[i].accuracy}%",
                                    FontType.Fixedsys, pt=32, color=_cur_color)
            self.ranked_list.append(_grade)
            self.game_world.add_object(_grade, 1)
            self.ranked_list.append(_score)
            self.game_world.add_object(_score, 1)
            self.ranked_list.append(_combo)
            self.game_world.add_object(_combo, 1)
            self.ranked_list.append(_acc)
            self.game_world.add_object(_acc, 1)

        for i in range(5):
            if i+5 >= len(rank_data):
                break
            _cur_color = RankingScene.match_text_color if rank_data[i + 5].now is True else RankingScene.normal_text_color
            _grade = UIText(350 + 380, self.framework.h - 270 - i * 90, f"{i+6}.",
                                    FontType.Fixedsys, pt=64, color=_cur_color)
            _score = UIText(450 + 380, self.framework.h - 270 - i * 90, f"{rank_data[i+5].score}",
                                    FontType.Fixedsys, pt=64, color=_cur_color)
            _combo = UIText(440 + 380, self.framework.h - 270 - i * 90 - 45, f"MAX HIT : {rank_data[i+5].max_combo}",
                                    FontType.Fixedsys, pt=32, color=_cur_color)
            _acc = UIText(350 + 380, self.framework.h - 270 - i * 90 - 45, f"{rank_data[i+5].accuracy}%",
                                    FontType.Fixedsys, pt=32, color=_cur_color)
            self.ranked_list.append(_grade)
            self.game_world.add_object(_grade, 1)
            self.ranked_list.append(_score)
            self.game_world.add_object(_score, 1)
            self.ranked_list.append(_combo)
            self.game_world.add_object(_combo, 1)
            self.ranked_list.append(_acc)
            self.game_world.add_object(_acc, 1)

        ranking.post_rank(now_rank_data)

        self.block_input_timer = 0.75

        self.game_world.add_object(self.background_image, 0)
        self.game_world.add_object(self.ui_rank_title, 1)
        self.game_world.add_object(self.ui_rank_difficult, 1)



    def draw(self):
        self.framework.get_index_stack(-2).draw()
        super().draw()
        
        
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
            pico2d.SDL_MOUSEBUTTONDOWN,
            handler_set.mouse_button_input(pico2d.SDL_BUTTON_LEFT, move_menu)
        )

        self.input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_ESCAPE, game_end)
        )
