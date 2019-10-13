# 메인 프레임워크
import pico2d

from .interface import IUpdatableObject, IDrawableObject
from .game_object import game_map


class Framework(IUpdatableObject, IDrawableObject):
    def __init__(self, w=int(1440), h=int(810), start=False):
        self.w = w
        self.h = h
        self.is_active = start
        self.game_map = game_map.GameMap()
        if start is True:
            self.start()

    def close(self):
        self.is_active = False

    def start(self):
        self.is_active = True
        print(self.w)
        print(self.h)
        pico2d.open_canvas(self.w, self.h)
        import os
        print(os.listdir())
        self.game_map.load("Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")
        self.game_map.start()

    def handle_events(self):
        events = pico2d.get_events()
        for event in events:
            if event.type is pico2d.SDL_QUIT:
                self.is_active = False
            elif event.type is pico2d.SDL_KEYDOWN and event.key is pico2d.SDLK_ESCAPE:
                self.is_active = False

    def update(self, delta_time):
        self.handle_events()
        self.game_map.update(delta_time)
        pass

    def draw(self):
        pico2d.clear_canvas()
        self.game_map.draw()
        pico2d.update_canvas()
        pass
