import os
import json
from googleapiclient.discovery import build


API_YOUTUBE = os.getenv('API_YOUTUBE')

youtube = build("youtube", "v3", developerKey=API_YOUTUBE)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        request = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id)
        response = request.execute()

        self.__channel_id = channel_id
        self.title = response["items"][0]["snippet"]["title"]
        self.description = response["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = response["items"][0]["statistics"]["subscriberCount"]
        self.view_count = response["items"][0]["statistics"]["viewCount"]
        self.video_count = response["items"][0]["statistics"]["videoCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        request = youtube.channels().list(part="snippet,contentDetails,statistics", id=self.channel_id)
        response = request.execute()
        print(response)

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return youtube

    def to_json(self, file_name) -> None:
        """
        Сохраняет данные в JSON-файл
        """
        request = youtube.channels().list(part="snippet,contentDetails,statistics", id=self.channel_id)
        response = request.execute()

        with open(file_name, 'w') as file:
            json.dump([response], file)
