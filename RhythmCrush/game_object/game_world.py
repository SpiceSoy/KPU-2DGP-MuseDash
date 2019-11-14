from ..interface import IUpdatableObject, IDrawableObject

class GameWorld(IUpdatableObject, IDrawableObject):
    def __init__(self, layer_count: int = 3):
        self.obj_layer = []
        for i in range(3):
            self.obj_layer.append([])

    def __del__(self):
        self.clear()

    def add_layer(self, count=1):
        for i in range(count):
            self.obj_layer.append([])

    def add_object(self, obj, layer):
        self.obj_layer[layer].append(obj)

    def delete_object(self, obj):
        for i in range(len(self.obj_layer)):
            if obj in self.obj_layer[i]:
                self.obj_layer[i].remove(obj)
                del obj

    def clear(self):
        for obj in self.all_object():
            del obj

    def all_object(self):
        for i in range(len(self.obj_layer)):
            for o in self.obj_layer[i]:
                yield o

    def load(self):
        for o in self.all_object():
            o.load()

    def update(self, delta_time):
        for o in self.all_object():
            o.update(delta_time)

    def draw(self):
        for o in self.all_object():
            o.draw()