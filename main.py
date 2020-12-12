from config import CHAOS_DIR, LIBRARY
from items.folder import Folder
from items.folders_tree import FoldersTree
from tools.walker import Walker

if __name__ == '__main__':
    walker = Walker(CHAOS_DIR)
    walker.collect_data()
    # TODO: create method that will split data sequences in to groups (for files that dont have exif data)
    walker.generate_catalogs_tree()
    FoldersTree.generate_catalog(LIBRARY)

    print(FoldersTree)
