import webbrowser
class Movie():
    """
    This class creates a new movie instance that has a title,
    storyline, poster_image_url, and trailer_youtube_url. It also
    has a method show_trailer() to open webbrowser to youtube trailer.
    """
    def __init__(self, moive_title, movie_storyline, poster_image, trailer_youtube):
        self.title = moive_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
