import shutil
import datetime

from tools.walker_interface import WalkerInterface
import os


class WalkerPhone(WalkerInterface):
    def __init__(self, media_root_path, library):
        super().__init__(media_root_path, library)

    def find_png(self):
        for item in os.walk(self.task_path):
            if not item[2]:
                continue
            cur_path = item[0]
            for media_file_name in item[2]:
                media_file_path = os.path.join(cur_path, media_file_name)
                media_source = media_file_name[:3]
                media_extention = media_file_name[-3:]
                if media_source == "IMG" and media_extention == "PNG":
                    self.get_png(media_file_path)

    def get_png(self, path):
        import_date = str(datetime.date.today())  # TODO: refactor this with WalkerDesktop

        # store folders names TODO: optimize this
        screenshots_path = os.path.join(self.library_path, 'screenshots')
        screenshots_import_date_folder_path = os.path.join(self.library_path, 'screenshots', import_date)

        # create folders structure if not already created
        if "screenshots" not in os.listdir(self.library_path):
            os.mkdir(screenshots_path)
        elif import_date not in os.listdir(screenshots_path):
            os.mkdir(screenshots_import_date_folder_path)

        # move file
        shutil.copy2(path, screenshots_import_date_folder_path)
