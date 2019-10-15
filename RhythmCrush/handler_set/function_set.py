import pico2d


def key_input(key, func):
    def ret(event):
        if event.key == key:
            func()
    return ret
