import json


class MusicMetaData:
    def __init__(self):
        self.title = None
        self.artist = None
        self.url_difficult_normal = None
        self.url_difficult_hard = None
        self.url_difficult_extreme = None

    def has_normal(self):
        return self.url_difficult_normal is not None

    def has_hard(self):
        return self.url_difficult_hard is not None

    def has_extreme(self):
        return self.url_difficult_extreme is not None

    def get_difficult_csr_list(self):
        difficult_csr_list = []
        for i in range(3):
            if self.has_difficult(i):
                difficult_csr_list.append(i)
        return difficult_csr_list

    def has_difficult(self, difficult_csr: int):
        return [self.has_normal(), self.has_hard(), self.has_extreme()][difficult_csr]

    def __str__(self):
        return f"{self.title} " + f"{self.artist}"+ f"\n{self.url_difficult_normal}"+ \
        f"\n{self.url_difficult_hard}"+ f"\n{self.url_difficult_extreme}\n"


def load_music_metadata(data: dict):
    ret = MusicMetaData()
    ret.title = data['title']
    ret.artist = data['artist']
    ret.url_difficult_normal = data['normal_url'] if 'normal_url' in data.keys() else None
    ret.url_difficult_hard = data['hard_url'] if 'hard_url' in data.keys() else None
    ret.url_difficult_extreme = data['extreme_url'] if 'extreme_url' in data.keys() else None
    ret.url_difficult_normal = ret.url_difficult_normal if ret.url_difficult_normal != "" else None
    ret.url_difficult_hard = ret.url_difficult_hard if ret.url_difficult_hard != "" else None
    ret.url_difficult_extreme = ret.url_difficult_extreme if ret.url_difficult_extreme != "" else None
    return ret


def load_music_metadata_list(url):
    return_list = []
    with open(url, "r") as file:
        data_list = json.load(file)
        for ds in data_list:
            return_list.append(load_music_metadata(ds))
    return return_list


if __name__ == "__main__":
    for i in load_music_metadata_list("../Resource/Map/music_meta.json"):
        print(str(i))
