import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_trailer, movie_image):
        self.title = movie_title
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_image

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
