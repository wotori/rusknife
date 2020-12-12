from os import walk
from os import path
import time
from exif import Image


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
                self.data_bag.append({"media_root": cur_path,
                                      'file_name': media_file_name,
                                      'media_file_path': media_file_path})

    def data_stracture_builder(self, media_file_name, media_file_path):
        media_source = media_file_name[:3]
        media_extention = media_file_name[-3:]

        # strategy for camera photos
        if media_source == "IMG" and media_extention == "JPG":
            with open(media_file_path, "rb") as media_file:
                image = Image(media_file)
                image_datetime = image.datetime_digitized

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
            # strategy for pos processed media
            pass

    def media_builder(self):
        for file in self.data_bag:
            with open(file, 'rb'):
                self.objects_bag.append(Image(file))
