import json
import os

class RankData:
    def __init__(self):
        self.music_name = ""
        self.difficult = 0
        self.score = 0
        self.max_combo = 0
        self.accuracy = 0

    def to_save_dict(self):
        return {
            "score": self.score,
            "max_combo": self.max_combo,
            "accuracy": self.accuracy
        }


rank_file_dir = "Data/rank.json"
rank_data = {}


def post_rank(rank: RankData):
    global rank_data
    if rank.music_name not in rank_data:
        rank_data[rank.music_name] = {0: [], 1: [], 2: []}
    rank_data[rank.music_name][str(rank.difficult)].append(rank.to_save_dict())
    dump()

def get_rank_list(music_name, difficult):
    global rank_data
    data = []
    for dic in rank_data[music_name][difficult]:
        ele = RankData()
        ele.music_name = music_name
        ele.difficult = difficult
        ele.score = int(dic["score"])
        ele.max_combo = int(dic["max_combo"])
        ele.accuracy = int(dic["accuracy"])
        data.append(ele)
    return data

def dump():
    global rank_data
    with open(rank_file_dir, 'w', encoding='utf-8') as make_file:
        print("DUMPPED")
        json.dump(rank_data, make_file, indent="\t")

def load():
    global rank_data
    if os.path.isfile(rank_file_dir):
        with open(rank_file_dir, 'r', encoding='utf-8') as load_file:
            rank_data = json.load(load_file)

load()