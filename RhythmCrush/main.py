# 메인 코드
import time

from RhythmCrush import framework

works = framework.Framework()

works.start()
prev_time = time.time()
now_time = time.time()

while works.is_active:
    prev_time = now_time
    now_time = time.time()
    delta_time = now_time - prev_time
    works.update(delta_time)
    works.draw()
