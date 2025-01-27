import isodate as isodate
import datetime

from src.channel import Channel
from src.video import Video


class PlayList(Channel):
    def __init__(self, playlist_id):
        """
        Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API.
        """
        request = self.get_service().playlistItems().list(playlistId=playlist_id, part='contentDetails, snippet')
        self.response = request.execute()
        snippet = self.get_service().playlists().list(id=playlist_id, part='snippet').execute()

        self.playlist_id = playlist_id
        self.title = snippet["items"][0]["snippet"]["title"]
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'
        self.video_ids = [video['contentDetails']['videoId'] for video in self.response['items']]

    def total_duration(self):
        """
        Метод для определения общей длительности.
        """
        video_response = self.get_service().videos().list(part='contentDetails,statistics', bid=','.join(self.video_ids)
                                                          ).execute()
        delta = datetime.timedelta()
        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            delta += duration
        return delta

    def show_best_video(self):
        """
        Метод для выявления лучшего из видео по лайкам.
        """
        vid_lst = [Video(video) for video in self.video_ids]
        for v in vid_lst:
            sorted(v.like_count)
        return vid_lst[-1].url
