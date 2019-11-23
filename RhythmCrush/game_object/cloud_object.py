from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager, input_manager
from RhythmCrush.game_object.game_world import GameWorld
from .. import handler_set

# 애니메이션 및 입력 테스트용
class Cloud(IUpdatableObject, IDrawableObject):
    def __init__(self, x, y, game_world, speed_ratio, speed=1000.0):
        self.x = x
        self.y = y
        self.speed_ratio = speed_ratio
        self.speed = speed
        self.image_controller = image_manager.get_image_controller('cloud-fx')
        self.game_world = game_world
        self.deleted = False

    def load(self):
        pass

    def draw(self):
        self.image_controller.draw(self.x, self.y)

    def update(self, delta_time):
        self.image_controller.update(delta_time)
        if self.x < -2 * self.image_controller.image.w:
            self.game_world.delete_object(self)
        else:
            self.x -= self.speed * self.speed_ratio * delta_time
