import webbrowser
class Movie():#class
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title#instanceVariable
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):#instanceMethod
        webbrowser.open(self.trailer_youtube_url)