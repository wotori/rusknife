from os import walk
from os import path


class Walker:
    data_bag = []

    def __init__(self, path):
        self.task_path = path

    def collect_data(self):
        for item in walk(self.task_path):
            if item[2] == []:
                continue
            cur_path = item[0]
            for media_file in item[2]:
                media_file_path = path.join(cur_path, media_file)
                self.data_bag.append(media_file_path)

            # TODO: просканировать все файлы, получить exif.
            # TODO: на основе exif создать список дат и структуру папок
