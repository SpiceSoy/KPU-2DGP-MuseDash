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

    def __str__(self):
        print(self.title)
        print(self.artist)
        print(self.url_difficult_normal)
        print(self.url_difficult_hard)
        print(self.url_difficult_extreme)


def load_music_metadata(data: dict):
    ret = MusicMetaData()
    ret.title = data['title']
    ret.artist = data['artist']
    diff_key_list = ['normal_url', 'hard_url', 'extreme_url']
    for keys in diff_key_list:
        if keys in data.keys():
            ret.url_difficult_normal = data[keys]
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
        print(str(i.title))
