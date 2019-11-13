from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager, input_manager
from .. import handler_set

# 애니메이션 및 입력 테스트용
class Player(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_controller = image_manager.get_image_controller('player-trex')

    def load(self):
        pass

    def post_handler(self, input_handler: input_manager.InputHandlerManager):
        def change_run():
            self.image_controller.animator.change_current_animation("run")

        def change_def():
            self.image_controller.animator.change_current_animation("default")

        def change_up():
            self.image_controller.animator.change_current_animation("up")

        def change_down():
            self.image_controller.animator.change_current_animation("down")

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_n, change_def)
        )

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_SPACE, change_run)
        )

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_UP, change_up)
        )

        input_handler.add_handler(
            pico2d.SDL_KEYDOWN,
            handler_set.key_input(pico2d.SDLK_DOWN, change_down)
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
