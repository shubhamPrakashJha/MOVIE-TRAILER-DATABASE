#importing webbrowser library to control functionality of webbrowser
import webbrowser

class Video():
    '''This class provides a way to create other subclass like movies and TV-Series '''
    def __init__(self,movie_title,duration):
        self.title = movie_title
        self.duration = duration

    def show_trailer(self):
        '''opens new tab in web browser with the URL passed to it as an argument'''
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    """ This class provides a way to store movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,duration,year):
        Video.__init__(self,movie_title,duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

