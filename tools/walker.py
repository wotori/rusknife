from os import walk


class Walker:
    data_bag = None

    def __init__(self, path):
        self.task_path = path

    def collect_data(self):
        for item in walk(self.task_path):
            print(item)
            # TODO: просканировать все файлы, получить exif.
            # TODO: на основе exif создать список дат и структуру папок
