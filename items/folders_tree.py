import os

class FoldersTree:
    folders = []
    folders_names = []

    def __repr__(self):
        return len(self.folders)

    @classmethod
    def generate_catalog(cls, library_path):
        for folder_name in cls.folders_names:
            catalog_path = os.path.join(library_path, folder_name)
            os.mkdir(catalog_path)
