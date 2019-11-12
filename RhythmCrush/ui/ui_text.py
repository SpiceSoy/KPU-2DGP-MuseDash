import pico2d

from ..ui.ui_base import BaseUIObject
from ..utill.font_manager import *


class UIText(BaseUIObject):
    def __init__(self, x, y, text: str = "", font=FontType.NanumSquare, style=FontStyle.Regular, pt=20,
                 color=(0, 0, 0)):
        super().__init__(x, y)
        self.text = text
        self.font_type = font
        self.font_style = style
        self.size = pt
        self.color = color
        self.font = None

    def load(self):
        self.font = FontManager.load(self.font_type, self.font_style, self.size)

    def update_text(self, text):
        self.text = text

    def change_color(self, color=(0, 0, 0)):
        self.color = color

    def draw(self):
        if self.is_visible:
            self.font.draw(self.position[0], self.position[1], self.text, self.color)
