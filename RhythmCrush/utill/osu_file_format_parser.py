# -*- coding: utf-8 -*-
# Osu Bitmap Parser

import os
import parse

from RhythmCrush import debug


class FileNotFound(Exception):
    pass


class FileNotLoaded(Exception):
    pass


class MusicNoteMap:
    """
    게임맵에 대하여 파싱한 정보들을 저장하는 컨테이너입니다.
    """
    def __init__(self):
        self.props = {}
        self.hit_objects = []
        self.timing_points = []

    def add_value(self, key, value):
        save_target_dic = {
            "General": lambda v: self.props.update(v),
            "Metadata": lambda v: self.props.update(v),
            "Difficulty": lambda v: self.props.update(v),
            "HitObjects": lambda v: self.hit_objects.append(v),
            "TimingPoints": lambda v: self.timing_points.append(v)
        }
        if key in save_target_dic and value is not None:
            save_target_dic[key](value)

    def get_props(self, key):
        if key in self.props:
            return self.props[key]

    def get_hit_object(self):
        return self.hit_objects

    def get_timing_point(self):
        return self.timing_points

    def __str__(self):
        str_result = "MusicNoteMap :: Content\n"
        str_result += "Props\n"
        for item in self.props:
            str_result += f"{ str(item) } : { str(self.props[item]) }" + "\n"
        str_result += "Timing Objects\n"
        for item in self.timing_points:
            str_result += str(item) + "\n"
        str_result += "Hit Objects\n"
        for item in self.hit_objects:
            str_result += str(item) + "\n"
        return str_result


def get_line_prop(line):
    result = parse.parse("{}:{}", line)
    if result is not None:
        key = result[0]
        item = result[1].strip()
        return {key: item}


def get_line_timing(line):
    result = parse.parse("{},{},{},{},{},{},{},{}", line)
    if result is not None:
        return result.fixed


def get_line_hit_object(line):
    result = parse.parse("{},{},{},{},{},{}:{}:{}:{}:", line)
    if result is not None:
        return result.fixed


def get_line_none(line):
    return None


line_type = ("General", "Editor", "Metadata", "Difficulty", "Events", "TimingPoints", "HitObjects")

line_parse_func = {
    "Events": get_line_none,
    "Editor": get_line_none,
    "General": get_line_prop,
    "Metadata": get_line_prop,
    "Difficulty": get_line_prop,
    "HitObjects": get_line_hit_object,
    "TimingPoints": get_line_timing
}


def parse_map_text(text_data):
    result = MusicNoteMap()
    line_context = None
    while True:
        line = text_data.readline()
        # line 파싱 코드
        if not line:
            break
        context_parse_result = parse.parse("[{}]", line)
        if context_parse_result is not None:
            # 문단 파악
            line_context = context_parse_result[0]
            debug.print_console("parse_file", f"Read Line Context { line_context }")
        else:
            if line_context is not None:
                line_parse_result = line_parse_func[line_context](line)
                if line_parse_result is not None:
                    debug.print_console("parse_file", "Read Line And Add Values")
                    result.add_value(line_context, line_parse_result)
            # 라인 읽기
            pass
    debug.print_console("parse_file", "Parse End")
    return result


def load_map_source(url):
    return parse_map_text(open(url, 'r', encoding='UTF8'))


# 단위 테스트 코드
if __name__ == "__main__":
    debug_url = os.path.abspath(
        "../Resource/Map/FirstTest/Camellia - Exit This Earth's Atomosphere (Camellia's PLANETARY200STEP Remix) (nyanmi-1828) [Satellite].osu")
    debug_result = load_map_source(debug_url)
    note_type = []
    for hits in debug_result.get_hit_object():
        if not hits[4] in note_type:
            note_type.append(hits[4])
    for ty in note_type:
        print(ty)
    # print(str(debug_result))
