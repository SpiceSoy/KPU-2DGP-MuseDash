# 메인 코드
import time

from RhythmCrush import framework

works = framework.Framework()

works.start()
delta_time = time.time()

while works.is_active:
    delta_time = time.time() - delta_time
    works.update(delta_time)
    works.draw()
