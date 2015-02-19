import movie_class
import fresh_tomatoes

''' Instantiate movies with corresponding data
    object_name = movie_class.Movie(
                  movie_name,
                  tag_line,
                  url_for_poster,
                  url_for_youtube_trailer,
                  [tags list]  )
'''

the_godfather = movie_class.Movie(
                "The Godfather",
                "One of the greatest films in world cinema",
                "http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                "https://www.youtube.com/watch?v=sY1S34973zA",
                ["gangster", "mafia", "crime", "classic", "violence", "drama"])

raging_bull = movie_class.Movie(
                "Raging Bull",
                "Jake LaMotta is a ticking time bomb",
                "http://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg",
                "https://www.youtube.com/watch?v=mHhzOM4gBIA",
                ["boxer", "violence", "rage", "biopic"])

taxi_driver = movie_class.Movie(
                "Taxi Driver",
                "A nobody dreams of being a somebody",
                "http://upload.wikimedia.org/wikipedia/en/c/c9/Taxi_Driver_poster.JPG",
                "https://www.youtube.com/watch?v=sLpMx8_TYOo",
                ["drama", "crime", "loner", "vigilante", "new york"])

rocky = movie_class.Movie(
                "Rocky",
                "A true hero goes all the way!",
                "http://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                "https://www.youtube.com/watch?v=YApt5kJhfdo",
                ["boxer", "training", "champion", "pennsylvania"])

the_good_the_bad_the_ugly = movie_class.Movie(
                "The Good, the Bad and the Ugly",
                "A classic western!",
                "http://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                "https://www.youtube.com/watch?v=FUsmGOlyOUc",
                ["western", "shootout", "gold", "hitman", "battle"])

star_wars_empire_strikes_back = movie_class.Movie(
                "Star Wars: Episode V - The Empire Strikes Back",
                "The Adventure Continues...",
                "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                "https://www.youtube.com/watch?v=mz_YWNhKOkM",
                ["scifi", "rescue", "force", "jedi", "war", "battle"])

toy_story = movie_class.Movie(
                "Toy Story",
                "A story of a boy and his toys that come to life",
                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                "https://www.youtube.com/watch?v=vwyZH85NQC4",
                ["animation", "rescue", "friends", "toys"])

avatar = movie_class.Movie(
                "Avatar",
                "A marine on an alien planet",
                "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                "https://www.youtube.com/watch?v=EgHI4YBXhxM",
                ["scifi", "alien", "war", "battle"])

school_of_rock = movie_class.Movie(
                "School of Rock",
                "If this school's a rockin...",
                "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                "http://www.youtube.com/watch?v=3PsUJFEBC74",
                ["rock", "music", "comedy", "school", "teacher"])

ratatouille = movie_class.Movie(
                "Ratatouille",
                "Waiter there is a rat making my soup!",
                "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                "http://www.youtube.com/watch?v=c3sBBRxDAqk",
                ["cook", "rat", "animation", "comedy", "paris"])

midnight_in_paris = movie_class.Movie(
                "Midnight in Paris",
                "Story Line",
                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                "https://www.youtube.com/watch?v=5nOF93SzX6s",
                ["romance", "comedy", "paris"])

hunger_games = movie_class.Movie(
                "Hunger Games",
                "May the odds be ever in your favor",
                "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                "http://www.youtube.com/watch?v=PbA63a7H0bo",
                ["drama", "battle", "weapon", "scifi"])


# Create a list of all the movie objects
# Required for the webpage creation code
movies = [  the_godfather, raging_bull, taxi_driver,
            rocky, the_good_the_bad_the_ugly, star_wars_empire_strikes_back,
            toy_story, avatar, school_of_rock,
            ratatouille, midnight_in_paris, hunger_games]
#movies = [the_godfather, raging_bull]

# We will now go through all the movie tags and see which movies are similar
for movie in movies:
    movie.find_similar_movies(movies)

# Call the function in the fresh_tomatoes module to create the HTML code
fresh_tomatoes.open_movies_page(movies)




