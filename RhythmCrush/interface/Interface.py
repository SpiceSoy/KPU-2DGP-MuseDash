#-*- coding: utf-8 -*- 
# 매 프레임 호출해야하는 오브젝트 관련 인터페이스

class IUpdatableObject:
    def update(self,delta_time):
        raise NotImplementedError()

class IDrawableObject:
    def draw(self):
        raise NotImplementedError()