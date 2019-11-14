from ..component.animation import *
from ..component.image_controller import *
from ..interface import IUpdatableObject, IDrawableObject
from ..utill import image_manager, input_manager

from ..component.interpolator import *
from ..component.accuracy import *
from .. import handler_set


# 애니메이션 및 입력 테스트용
class AccuracyEffect(IUpdatableObject, IDrawableObject):
    judgement_dic = {
        AccuracyGrade.Bad: 'acc-bad',
        AccuracyGrade.Good: 'acc-good',
        AccuracyGrade.Miss: 'acc-miss',
        AccuracyGrade.Nice: 'acc-nice',
        AccuracyGrade.Perfect: 'acc-perfect',
    }
    controller_dic = {}

    def __init__(self, x, y, accuracy, world):
        self.x = x
        self.y = y
        self.world = world
        self.move_length = 100
        self.acc = accuracy
        if len(AccuracyEffect.controller_dic) == 0:
            for key, item in AccuracyEffect.judgement_dic.items():
                AccuracyEffect.controller_dic[key] = image_manager.get_image_controller(item)

        self.image_controller = AccuracyEffect.controller_dic[accuracy]

        self.position_interpolator = DeltatimeRatioInterpolator(self.y, self.y + self.move_length * 2, 0.6)
        self.alpha_interpolator = DeltatimeRatioInterpolator(1.0, -1.0, 0.6)

    def load(self):
        pass

    def draw(self):
        self.image_controller.set_alpha(self.alpha_interpolator.get_current_value())
        self.image_controller.draw(self.x, self.position_interpolator.get_current_value())

    def update(self, delta_time):
        self.image_controller.update(delta_time)
        self.position_interpolator.update(delta_time)
        self.alpha_interpolator.update(delta_time)
        if self.position_interpolator.get_current_value() > self.y + self.move_length:
            self.world.delete_object(self)
            del self


