import webbrowser

class Video():
    def __init__(self,movie_title,duration):
        self.title = movie_title
        self.duration = duration

class Movie(Video):#class
    """ This calass provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,duration):
        Video.__init__(self,movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):#instanceMethod
        webbrowser.open(self.trailer_youtube_url)

    # def do(self):
    #     print(__name__)