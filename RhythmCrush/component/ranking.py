import json


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


class Ranking:
    rank_file_dir = "Data/rank.json"

    def __init__(self):
        self.data = {}

    def post_rank(self, rank: RankData):
        if rank.music_name not in self.data:
            self.data[rank.music_name] = {0: [], 1: [], 2: []}
        self.data[rank.music_name][rank.difficult].append(rank.to_save_dict())

    def get_rank_list(self, music_name, difficult):
        data = []
        for dic in self.data[music_name][difficult]:
            ele = RankData()
            ele.music_name = music_name
            ele.difficult = difficult
            ele.score = int(dic["score"])
            ele.max_combo = int(dic["max_combo"])
            ele.accuracy = int(dic["accuracy"])
            data.append(ele)
        return data

    def dump(self):
        with open(Ranking.rank_file_dir, 'w', encoding='utf-8') as make_file:
            json.dump(self.data, make_file, indent="\t")

    def load(self):
        with open(Ranking.rank_file_dir, 'w', encoding='utf-8') as load_file:
            self.data = json.load(load_file)
