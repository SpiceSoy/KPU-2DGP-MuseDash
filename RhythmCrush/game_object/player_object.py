from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager


# 애니메이션 및 입력 테스트용
class Player(IUpdatableObject, IDrawableObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image_controller = ImageController(image_manager.load_image('player-trex'))
        # self.image_controller.add_animator()
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
        self.image_controller.add_animator(animator)

    def draw(self):
        self.image_controller.draw(self.x, self.y)
        pass

    def update(self, delta_time):
        self.image_controller.update(delta_time)
        pass

    def handle_input(self, events):
        # for event in events:
        pass
