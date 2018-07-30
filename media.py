class Movie():
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        :param title: str(Movie title)
        :param poster_image_url: str(url to image)
        :param trailer_youtube_url: str(url to trailer)
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
