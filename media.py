import webbrowser

class Movie():
    """
    This sets the structure for the `movie tiles` on the webpage.
    Each argument in the __init__ function is an attribute of the movie.

    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, genre, language, release_date, runtime):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.genre = genre
        self.language = language
        self.release_date = release_date
        self.runtime = runtime

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
