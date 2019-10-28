import pico2d


def key_input(key, func):
    def ret(event):
        if event.key == key:
            func()
    return ret


def mouse_motion_input(func, clickable=None):
    def ret(event):
        if clickable is None or clickable.check_click(event.x, event.y):
            func()
    return ret


def mouse_button_input(button, func, clickable=None):
    def ret(event):
        if event.button == button:
            if clickable is None or clickable.check_click(event.x, event.y):
                func()
    return ret