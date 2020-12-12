from os import walk
from os import path
from exif import Image
from datetime import datetime

from items.folder import Folder
from items.folders_tree import FoldersTree
from items.media_file import MediaFile


class Walker:

    def __init__(self, media_root_path):
        self.task_path = media_root_path
        self.data_bag = []

    def collect_data(self):
        """
        collecting all data across root catalog
        """
        for item in walk(self.task_path):
            if not item[2]:
                continue
            cur_path = item[0]
            for media_file_name in item[2]:
                media_file_path = path.join(cur_path, media_file_name)
                media_datetime = self.get_img_date(media_file_path, media_file_name)
                file = MediaFile(cur_path,
                                 media_file_name,
                                 media_file_path,
                                 media_datetime)
                self.data_bag.append(file)

    def get_img_date(self, media_file_path, media_file_name):
        media_source = media_file_name[:3]
        media_extention = media_file_name[-3:]
        try:
            if media_extention[-3:] == "JPG" and media_source == "IMG":
                with open(media_file_path, 'rb') as img_file:
                    image = Image(img_file)
                    datetime = image.datetime_digitized
                    return datetime
            else:
                return None
        except:  # mostly files that was saved in gallery (iOS)
            return None

    def generate_catalogs_tree(self):
        media_file_dict: MediaFile
        folders_list = []
        for n, media_file_dict in enumerate(self.data_bag):
            if media_file_dict.media_data_created:
                date = media_file_dict.media_data_created
                date_obj = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
                datetime_folder_name = date_obj.date().strftime("%Y_%m_%d")
                if datetime_folder_name not in folders_list:
                    folders_list.append(datetime_folder_name)
        FoldersTree.folders_names = folders_list

    def data_stracture_builder(self, media_file_name):
        media_source = media_file_name[:3]
        media_extention = media_file_name[-3:]

        # strategy for camera photos
        if media_source == "IMG" and media_extention == "JPG":
            pass

        # strategy for camera video
        elif media_source == "IMG" and media_extention == "MP4":
            pass

        # strategy for editing AAE file
        elif media_source == "IMG" and media_extention == "AAE":
            pass

        # strategy for screenshots
        elif media_source == "IMG" and media_extention == "PNG":
            pass

        else:
            # strategy for pos processed media that was saved from chats, rendered e.t.c.
            pass
