from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import datetime

class Drive():
    def __init__(self): 
        gauth = GoogleAuth()
        gauth.CommandLineAuth()  # <--
        self.drive = GoogleDrive(gauth)

        # privates
        # TODO -> Create folder if it's equal to none.
        self._current_year_folder_id = self._get_folder_by_name(datetime.datetime.now().year)['id'];

    def upload_image(self, title: str, image_path: str, sender=None) -> str:
        try:
            file = self.drive.CreateFile({'parents': [{'id': self._current_year_folder_id}]})
            file.SetContentFile(image_path)
            file['title'] = title;
            if sender:
                file['description'] = f"Enviado por {sender}"
            file.Upload()
            return file['embedLink']
        except:
            return "A problem happened uploading the image to google drive."

    def get_folder_link(self) -> str:
        return self._get_folder_by_name("Drive")['alternateLink']


    def _get_folder_by_name(self, name: str) -> int:
        try:
            folders = self.drive.ListFile({'q': f"title='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"})
            return folders.GetList()[0]
        except:
            print(f"Couldn't find folder named {name}")

if __name__ == '__main__':
    drive = Drive()
    print(drive.get_folder_link())
