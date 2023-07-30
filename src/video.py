from src.channel import Channel


class Video(Channel):

    def __init__(self, video_id):
        """
        Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API.
        """
        request = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id)
        self.response = request.execute()

        self.__video_id = video_id

        try:
            self.title = self.response["items"][0]["snippet"]["title"]
            self.url = f'https://youtu.be/{video_id}'
            self.like_count = self.response["items"][0]["statistics"]["likeCount"]
            self.view_count = self.response["items"][0]["statistics"]["viewCount"]
        except Exception:
            self.title = None
            self.url = None
            self.like_count = None
            self.view_count = None

            print("Wrong id video!")


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
