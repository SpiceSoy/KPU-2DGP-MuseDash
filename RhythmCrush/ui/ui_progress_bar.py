import enum

from ..ui.ui_base import *

from ..utill import image_manager


# origin To end
class ProgressbarDirection(enum.Enum):
    RightToLeft = 0
    DownToTop = 1
    LeftToRight = 2
    TopToDown = 3


class UIProgressBar(BaseUIObject):
    direction_dic = {
        ProgressbarDirection.RightToLeft: 1.0, ProgressbarDirection.DownToTop: 1.0,
        ProgressbarDirection.LeftToRight: -1.0, ProgressbarDirection.TopToDown: -1.0
    }

    def __init__(self, x, y, tag, w=None, h=None, direction: ProgressbarDirection = ProgressbarDirection.LeftToRight):
        super().__init__(x, y)
        self.ratio = 1.0
        self.image_tag = tag
        self.image_controller = None
        self.direction = direction

    def load(self):
        self.image_controller = image_manager.get_image_controller(self.image_tag)


    def update_value(self, value: float, value_max: float = 1.0):
        self.ratio = value / value_max

    def draw(self):
        src_w = self.image_controller.image.w
        src_h = self.image_controller.image.h
        plus = UIProgressBar.direction_dic[self.direction]
        if self.direction in (ProgressbarDirection.LeftToRight, ProgressbarDirection.RightToLeft):
            cal_w = self.image_controller.image.w * self.ratio
            cal_h = self.image_controller.image.h
            x = self.position[0] + plus * ((1 - self.ratio) * self.image_controller.image.w / 2)
            y = self.position[1]
        else:
            cal_w = self.image_controller.image.w
            cal_h = self.image_controller.image.h * self.ratio
            x = self.position[0]
            y = self.position[1] + plus * ((1 - self.ratio) * self.image_controller.image.h / 2)
        self.image_controller.clip_draw_no_animation(0, 0, int(cal_w), int(cal_h), int(x), int(y))






