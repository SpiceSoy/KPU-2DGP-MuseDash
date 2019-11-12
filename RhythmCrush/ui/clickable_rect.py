
class ClickableRect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def check_click(self, mouse_x, mouse_y):
        return abs(self.x - mouse_x) <= self.w/2 and abs(self.y - mouse_y) <= self.h/2
