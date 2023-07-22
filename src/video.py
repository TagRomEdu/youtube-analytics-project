from src.channel import Channel


class Video(Channel):
    def __init__(self, video_id):
        request = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id)
        self.response = request.execute()

        self.__video_id = video_id
        self.title = self.response["items"][0]["snippet"]["title"]
        self.url = f'https://youtu.be/{video_id}'
        self.like_count = self.response["items"][0]["statistics"]["likeCount"]
        self.view_count = self.response["items"][0]["statistics"]["viewCount"]



video1 = Video('AWX4JnAnjBE')
print(video1.title)