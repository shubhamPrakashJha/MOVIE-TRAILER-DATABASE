import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1hr 21min",
                        "1995")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     "2h 42min",
                     "2009")

the_dark_night = media.Movie("The Dark Knight",
                            "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
                             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                             "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                             "2h 32min",
                             "2008")

school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             "1h 48min",
                             "2003")

ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with a young kitchen worker at a famous restaurant.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=niD-jahFURU",
                          "1h 51min",
                          "2007")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiance/'s family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY",
                     "1h 34min",
                      "2011")

the_hunger_games = media.Movie("The Hunger Games",
                               "Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death",
                                "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                                "https://www.youtube.com/watch?v=mfmrPu43DF8",
                                "2h 22min",
                                "2012")

titanic = media.Movie("TITANIC",
                      "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                      "3h 14min",
                      "1997")

jurassic_park = media.Movie("Jurassic Park",
                            "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
                            "https://www.youtube.com/watch?v=pUc-cBjh11Y",
                            "2h 7min",
                            "1993")

movies = [titanic,avatar,the_dark_night,jurassic_park,ratatouille,midnight_in_paris,the_hunger_games,toy_story,school_of_rock]
fresh_tomatoes.open_movies_page(movies)

