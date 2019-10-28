from ..component.animation import *

image_base_dir_url = "Resource/Image/"

image_url_dic = {
        'note-back-big': "Note/taikobigcircle.png",
        'note-front-big': "Note/taikobigcircleoverlay.png",
        'note-back': "Note/taikohitcircle.png",
        'note-front': "Note/taikohitcircleoverlay.png",
        'player-trex': "Char/t_rex_sprite.png",
        'note-don': "Char/t_rex_sprite.png",
        'note-big-don': "Note/taikohitcircle.png",
        'note-kat': "Char/t_rex_sprite.png",
        'note-big-kat': "Note/taikohitcircle.png",
        'ui-hp': "UI/hp_bar.png",
        'ui-title-back': "UI/title_back.png",
        'ui-csr': "UI/csr.png"
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

    move_anim = SubAnimation("repeat")
    move_anim.add_frame(2295, 204 - 147, 132, 141)
    move_anim.add_frame_other_position(2427, 204 - 147)

    up_anim = SubAnimation("run")
    up_anim.add_frame(2902, 204 - 147, 222, 141, 0.05)
    up_anim.add_frame(2295, 204 - 147, 132, 141, 0.1)

    down_anim = SubAnimation("run")
    down_anim.add_frame(2295, 204 - 147, 132, 141, 0.05)
    down_anim.add_frame(2902, 204 - 147, 222, 141, 0.1)


    animator.add_sub_animation("default", default_anim)
    animator.add_sub_animation("run", move_anim)
    animator.add_sub_animation("up", up_anim)
    animator.add_sub_animation("down", down_anim)

    animator.change_current_animation("run")

    animators['player-trex'] = animator
    pass


def load_don():
    animator = Animator()
    # 기본 서있기
    # 이동하기
    move_anim = SubAnimation("repeat")
    move_anim.add_frame(402, 204 - 126, 138, 121)
    move_anim.add_frame_other_position(540, 204 - 126)
    animator.add_sub_animation("run", move_anim)

    animator.change_current_animation("run")

    animators['note-don'] = animator
    pass


def load_kat():
    animator = Animator()
    # 기본 서있기
    # 이동하기
    move_anim = SubAnimation("repeat")
    move_anim.add_frame(684, 204 - 111, 51, 105,2100000)
    move_anim.add_frame_other_position(684 + 1 * 51, 204 - 111)
    move_anim.add_frame_other_position(684 + 2 * 51, 204 - 111)
    move_anim.add_frame_other_position(684 + 3 * 51, 204 - 111)
    move_anim.add_frame_other_position(684 + 4 * 51, 204 - 111)
    move_anim.add_frame_other_position(684 + 5 * 51, 204 - 111)
    animator.add_sub_animation("run", move_anim)

    animator.change_current_animation("run")

    animators['note-kat'] = animator
    pass

load_player()
load_don()
load_kat()