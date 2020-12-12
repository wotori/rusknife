from abc import ABC


class WalkerInterface(ABC):

    def __init__(self, media_root_path, library):
        self.task_path = media_root_path
        self.library_path = library
        self.data_bag = []
        self.unique_data_list = []
