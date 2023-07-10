import os
from googleapiclient.discovery import build


API_YOUTUBE = os.getenv('API_YOUTUBE')
youtube = build("youtube", "v3", developerKey=API_YOUTUBE)



class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        request = youtube.channels().list(part="snippet,contentDetails", id=self.channel_id)
        response = request.execute()
        print(response)

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return youtube
