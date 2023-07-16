import os
import json
from googleapiclient.discovery import build


API_YOUTUBE = os.getenv('API_YOUTUBE')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        request = Channel.get_service().channels().list(part="snippet,contentDetails,statistics", id=channel_id)
        self.response = request.execute()

        self.__channel_id = channel_id
        self.title = self.response["items"][0]["snippet"]["title"]
        self.description = self.response["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.subscriber_count = self.response["items"][0]["statistics"]["subscriberCount"]
        self.view_count = self.response["items"][0]["statistics"]["viewCount"]
        self.video_count = self.response["items"][0]["statistics"]["videoCount"]

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    @property
    def channel_id(self):
        return self.__channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.response, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """
        Возвращает объект для работы с YouTube API
        """
        return build("youtube", "v3", developerKey=API_YOUTUBE)

    def to_json(self, file_name) -> None:
        """
        Сохраняет данные в JSON-файл
        """
        data = {
            "title": self.title,
            "url": self.url,
            "description": self.description,
            "subscriber_count": self.subscriber_count,
            "video_count": self.video_count,
            "view_count": self.view_count,
        }

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
