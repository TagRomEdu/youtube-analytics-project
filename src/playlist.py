from src.channel import Channel


class PlayList(Channel):
    def __init__(self, playlist_id):
        """
        Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API.
        """
        request = self.get_service().playlistItems().list(playlistId=playlist_id,
                                                          part='contentDetails, snippet',
                                                          maxResults=50,
                                                          )
        self.response = request.execute()

        self.playlist_id = playlist_id
        self.title = self.response["items"][0]["snippet"]["title"]
        self.url = f'https://www.youtube.com/playlist?list={playlist_id}'

