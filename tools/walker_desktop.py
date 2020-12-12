import os
import shutil
from os import walk
from os import path
from exif import Image
import datetime

from items.folders_tree import FoldersTree
from items.media_file import MediaFile
from tools.walker_interface import WalkerInterface


class WalkerDesktop(WalkerInterface):

    def __init__(self, media_root_path, library):
        super().__init__(media_root_path, library)

    def collect_data(self):
        """
        collecting all data across root catalog
        move screenshots and other files to specific folder in library
        store camera files to dict for further postprocess with self.first_preprocess_file(file) method
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
                self.first_preprocess_file(file)

    def first_preprocess_file(self, file):
        """
        :param file:
        extract screenshots and exported media and move them to specific folder
        camera media files add to WalkerDesktop data_bag attribute for further processing
        """
        media_source = file.media_name[:3]
        media_extention = file.media_name[-3:]
        if media_source == "IMG" and media_extention == "PNG":
            self.save_screenshot_media(file)
        elif media_source != "IMG":
            self.save_other_media(file)
        else:
            self.data_bag.append(file)

    def save_screenshot_media(self, file):
        # TODO: Find and destry this bug
        """ TODO: check this description in PEP8 styling
        discription:
        proceed png files

        note:
        this could have a bug that I coldn't find.
        It writes all png to single file with folder name
        """
        import_date = str(datetime.date.today())
        screenshots_path = os.path.join(self.library_path, 'screenshots')
        screenshots_import_date_folder_path = os.path.join(self.library_path, 'screenshots', import_date)

        # create folders structure if not already created
        if "screenshots" not in os.listdir(self.library_path):
            os.mkdir(screenshots_path)
        elif import_date not in os.listdir(screenshots_path):
            os.mkdir(screenshots_import_date_folder_path)

        # move file
        shutil.move(file.media_path, screenshots_import_date_folder_path)

    def save_other_media(self, file):
        import_date = str(datetime.date.today())
        other_media_path = os.path.join(self.library_path, 'other_media')
        other_media_import_date_folder_path = os.path.join(self.library_path, 'other_media', import_date)

        # create folders structure if not already created
        if "other_media" not in os.listdir(self.library_path):
            os.mkdir(other_media_path)
        elif import_date not in os.listdir(other_media_path):
            os.mkdir(other_media_import_date_folder_path)

        # move file
        shutil.move(file.media_path, other_media_import_date_folder_path)

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
                datetime_folder_name = datetime.datetime.strftime(date, '%Y:%m:%d %H:%M:%S')
                if datetime_folder_name not in folders_list:
                    folders_list.append(datetime_folder_name)
        self.unique_data_list = folders_list
        FoldersTree.folders_names = folders_list  # SOLID - S. mb we don't need FoldersTree here

    # this interface should split media data into groups TODO: finish this later
    def split_to_groups_by_date(self):
        structure = {}
        data_list = []
        in_point = 0
        item: MediaFile
        previous_date = False
        for n, item in enumerate(self.data_bag):
            date = item.media_data_created
            if date and date not in data_list:
                if previous_date:
                    structure[previous_date].append(self.data_bag[in_point: n - 1])
                data_list.append(date)
                structure[date] = self.data_bag[in_point:n]
                in_point = n + 1
                previous_date = date

        return structure

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
