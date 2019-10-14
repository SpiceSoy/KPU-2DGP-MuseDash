import enum
import pico2d
from ..framework import *


class CallChain:
    def __init__(self):
        self.chain = {}

    def add_chain(self, key, func):
        self.chain[key] = func

    def del_chain(self, key):
        self.chain.pop(key)

    def is_in(self, key):
        return key in self.chain

    def execute(self, event):
        for key, func in self.chain:
            func(event)


class InputHandlerManager:
    def __init__(self, framework : Framework):
        self.last_id = 0
        self.framework = framework
        self.call_chain_dict = {}

    def alloc_id(self):
        self.last_id += 1
        return self.last_id - 1

    def add_handler(self, event_type, func):
        index = self.alloc_id()
        if event_type not in self.call_chain_dict:
            self.call_chain_dict[event_type] = CallChain()
        self.call_chain_dict[event_type].add_chain(index, func)
        return index

    def del_handler(self, key, event_type=None):
        if event_type is not None:
            for dict_key, chain in self.call_chain_dict:
                if chain.is_in(key):
                    chain.del_chain(key)
        else:
            self.call_chain_dict[event_type].del_chain(key)

    def default_event_handle(self, event):
        if event.type is pico2d.SDL_QUIT:
            self.framework.is_active = False

    def handle_event(self):
        events = pico2d.get_events()
        for event in events:
            if event.type in self.call_chain_dict:
                self.call_chain_dict[event.type].excute(event)
