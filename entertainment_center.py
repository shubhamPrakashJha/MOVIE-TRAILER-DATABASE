import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy AND his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral unobtanium,[9][10] a room-temperature superconductor",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_night = media.Movie("The Dark Knight",
                     "The Dark Knight is a 2008 superhero film directed, co-produced, and co-written by Christopher Nolan. Featuring the DC Comics character Batman, the film is the second part of Nolan's The Dark Knight Trilogy and a sequel to 2005's Batman Begins",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                     "https://www.youtube.com/watch?v=EXeTwQWrcwY")

school_of_rock = media.Movie("School of Rock",
                     "Down and out rock star Dewey Finn gets fired from his band, and he faces a mountain of debts and depression. He takes a job as a 4th grade substitute teacher at an uptight private school where his attitude and hijinx have a powerful effect on his students. He also meets Zack, a 10-year-old guitar prodigy, who could help Dewey win a battle of the bands competition, which would solve his financial problems and put him back in the spotlight",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                     "Remy is an idealistic and ambitious young rat, gifted with highly developed senses of taste and smell",
                     "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                     "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "a midnight in paris",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://www.youtube.com/watch?v=FAfR8omt-CY")

the_hunger_games = media.Movie("The Hunger Games",
                     "As punishment for a past rebellion, each of the 12 districts of Panem is forced by the Capitol to select two tributes, one boy and one girl between the ages of 12 and 18, to fight to the death in the annual Hunger Games",
                     "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                     "https://www.youtube.com/watch?v=mfmrPu43DF8")

# print(toy_story.storyline)
# print(avatar.storyline)
# avatar.show_trailer()
# print(the_dark_night.storyline)
# the_dark_night.show_trailer()

movies = [toy_story,avatar,the_dark_night,school_of_rock,ratatouille,midnight_in_paris,the_hunger_games]
fresh_tomatoes.open_movies_page(movies)