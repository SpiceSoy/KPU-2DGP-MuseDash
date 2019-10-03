# 메인 코드 : Canvas 관리
import pico2d
import time

pico2d.open_canvas(w=int(1440), h=int(810))


start_time = time.time()

while True:
    events = pico2d.get_events()
    pico2d.clear_canvas()
    for evs in events:
        if evs.key == 27:
            exit()
    pico2d.debug_print(str(time.time() - start_time))
    pico2d.update_canvas()
    pico2d.delay(1/100)
    pass
