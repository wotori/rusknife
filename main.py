from config import CHAOS_DIR, LIBRARY
from items.folder import Folder
from items.folders_tree import FoldersTree
from tools.walker import Walker

if __name__ == '__main__':
    walker = Walker(CHAOS_DIR)
    walker.collect_data()
    walker.generate_catalogs_tree(LIBRARY)
    print(FoldersTree)

# TODO: просканировать все файлы, получить exif.
# TODO: на основе exif создать список дат и структуру папок
