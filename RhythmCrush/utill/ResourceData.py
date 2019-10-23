from ..component.animation import *

image_base_dir_url = "Resource/Image/"

image_url_dic = {
        'note-back-big': "Note/taikobigcircle.png",
        'note-front-big': "Note/taikobigcircleoverlay.png",
        'note-back': "Note/taikohitcircle.png",
        'note-front': "Note/taikohitcircleoverlay.png",
        'player-trex': "Char/t_rex_sprite.png"
    }

image_cache = {}

animators = {}


def load_player():
    animator = Animator()
    # 기본 서있기
    default_anim = SubAnimation("repeat")
    default_anim.add_frame(2031, 204 - 147, 132, 141)
    # 이동하기
    move_anim = SubAnimation("repeat")
    move_anim.add_frame(2295, 204 - 147, 132, 141)
    move_anim.add_frame_other_position(2427, 204 - 147)

    animator.add_sub_animation("default", default_anim)
    animator.add_sub_animation("run", move_anim)

    animator.change_current_animation("run")

    animators['player-trex'] = animator
    pass

load_player()