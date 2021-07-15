from io import BytesIO

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class StorageManager:
    __drive = None

    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.__drive = GoogleDrive(gauth)

    def upload(self, title, filepath):
        file_list = self.__drive.ListFile(
            {'q': f'title = "{title}"'}).GetList()
        if file_list:
            file_id = file_list[0]['id']
            f = self.__drive.CreateFile({'id': file_id})
        else:
            f = self.__drive.CreateFile()
        f.SetContentFile(filepath)
        f['title'] = title
        f.Upload()

    def get(self, title) -> BytesIO:
        file_id = self.__drive.ListFile(
            {'q': f'title = "{title}"'}).GetList()[0]['id']
        f = self.__drive.CreateFile({'id': file_id})
        f.FetchContent()
        return f.content
