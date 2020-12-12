from config import CHAOS_DIR, LIBRARY, PHONE_MEDIA_ROOT_DIR
from items.folders_tree import FoldersTree
from tools.walker_desktop import WalkerDesktop
from tools.walker_phone import WalkerPhone


def client_code_v1():
    """
    sort media files on desktop that was copied from phone
    """
    walker = WalkerDesktop(CHAOS_DIR, LIBRARY)
    walker.collect_data()
    # TODO: all files that wasn't started from IMG_we have to put to separate folder first and remove from dict - FIRST STEP
    # TODO FIRST STEP - extract screenshots, saved media and exports, move to folder
    print(walker)

    # TODO: all screenshots put to another folder - SECOND STEP
    walker.split_to_groups_by_date()  # TODO: create method that will split data sequences in to groups (for files that dont have exif data)
    walker.generate_catalogs_tree()
    FoldersTree.generate_catalog(LIBRARY)

    print(FoldersTree)

def client_code_v2():
    walker = WalkerPhone(PHONE_MEDIA_ROOT_DIR, LIBRARY)
    walker.find_png()
