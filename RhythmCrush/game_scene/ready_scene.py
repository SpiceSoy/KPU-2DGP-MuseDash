from ..game_scene.base_scene import BaseScene

from RhythmCrush.utill import image_manager

import pico2d


class ReadyScene(BaseScene):
    def __init__(self, framework):
        super().__init__(framework)
        self.background_image = image_manager.get_image_controller('ready-anim')
        self.end_timer = 4.0

    def draw(self):
        if self.framework.get_index_stack(-1) == self:
            self.framework.get_index_stack(-2).draw()
        else:
            self.framework.get_index_stack(-3).draw()
        super().draw()
        self.background_image.draw(self.framework.w/2, self.framework.h/2)

    def update(self, delta_time):
        self.background_image.update(delta_time)
        self.end_timer -= delta_time
        if self.end_timer < 0:
            self.framework.pop_scene()
