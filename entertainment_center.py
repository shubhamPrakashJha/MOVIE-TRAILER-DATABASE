import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1hr 21min")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "2h 42min")

the_dark_night = media.Movie("The Dark Knight",
                            "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                             "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                             "2h 32min")

school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "1h 48min")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU",
                          "1h 51min")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiance/'s family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY",
                     "1h 34min")

the_hunger_games = media.Movie("The Hunger Games",
                               "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death",
                                "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                                "https://www.youtube.com/watch?v=mfmrPu43DF8",
                                "2h 22min")


movies = [toy_story,avatar,the_dark_night,school_of_rock,ratatouille,midnight_in_paris,the_hunger_games]
fresh_tomatoes.open_movies_page(movies)


# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
# print(the_dark_night.storyline)
# the_dark_night.show_trailer()
# print(the_hunger_games.duration)


# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# print(avatar.__module__)
# print(__name__)
# avatar.do()