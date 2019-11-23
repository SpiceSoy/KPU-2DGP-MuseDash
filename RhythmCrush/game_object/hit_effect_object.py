from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager, input_manager
from .. import handler_set

# 애니메이션 및 입력 테스트용
class HitEffect(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, game_world, speed=10.0):
        self.x = x
        self.y = y
        self.image_controller = image_manager.get_image_controller('hit-effect')
        self.image_controller.set_speed(speed)
        self.game_world = game_world

        self.image_controller.animator.change_current_animation("exp")

    def load(self):
        pass
    def draw(self):
        self.image_controller.draw(self.x, self.y)

    def update(self, delta_time):
        self.image_controller.update(delta_time)
        if self.image_controller.animator.current_key == "def":
            self.game_world.delete_object(self)
