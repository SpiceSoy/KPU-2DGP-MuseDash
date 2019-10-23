from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager, input_manager
from .. import handler_set

# 애니메이션 및 입력 테스트용
class Player(IUpdatableObject, IDrawableObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image_controller = image_manager.get_image_controller('player-trex')
        # self.image_controller = ImageController(image_manager.load_image('player-trex'))
        # self.image_controller.add_animator()
        # animator = Animator()
        #
        # # 기본 서있기
        # default_anim = SubAnimation("repeat")
        # default_anim.add_frame(2031, 204 - 147, 132, 141)
        #
        # # 이동하기
        # move_anim = SubAnimation("repeat")
        # move_anim.add_frame(2295, 204 - 147, 132, 141)
        # move_anim.add_frame_other_position(2427, 204 - 147)
        #
        # animator.add_sub_animation("default", default_anim)
        # animator.add_sub_animation("run", move_anim)
        #
        # animator.change_current_animation("run")
        # self.image_controller.add_animator(animator)

    def post_handler(self, input_handler: input_manager.InputHandlerManager):
        def change_run():
            self.image_controller.animator.change_current_animation("run")

        def change_def():
            self.image_controller.animator.change_current_animation("default")

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_n, change_def)
        )

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_SPACE, change_run)
        )

    def draw(self):
        self.image_controller.draw(self.x, self.y)
        pass

    def update(self, delta_time):
        self.image_controller.update(delta_time)
        pass

    def handle_input(self, events):
        for event in events:
            if event.type == pico2d.SDL_KEYDOWN:
                if event.key == pico2d.SDLK_SPACE:
                    self.image_controller.animator.change_current_animation("run")
                elif event.key == pico2d.SDLK_n:
                    self.image_controller.animator.change_current_animation("default")
        pass
