import enum

from ..ui.ui_base import *

from ..utill import image_manager


class UIStaticImage(BaseUIObject):
    def __init__(self, x, y, tag, w=None, h=None):
        super().__init__(x, y)
        self.image_tag = tag
        self.image_controller = None
        self.w = w
        self.h = h

    def load(self):
        self.image_controller = image_manager.get_image_controller(self.image_tag)

    def draw(self):
        if self.visible:
            self.image_controller.draw(self.position[0], self.position[1], self.w, self.h)


