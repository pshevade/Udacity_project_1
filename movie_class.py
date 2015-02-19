# class movie
#   attributes: title, reviews, trailer, poster image
#   methods:    show_trailer()  opens movie trailer on youtube.com
import webbrowser


class Movie():
    """ This class provides a way to store movie information """
    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube, tag_list):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.tag_list = tag_list
        self.similar = []               #this will be used to create a list of
                                        #movies similar to this one (based on tags)


    def show_trailer(self):
        ''' This function will open the youtube trailer url in a browser '''
        webbrowser.open(self.trailer_youtube_url)

    def find_similar_movies(self, movie_list):
        ''' This function will loop through the movie's tag list to find other
            movies in the passed attribute movie_list to find which movies are
            similar to this one '''
        for movie in movie_list:
            if movie.title is not self.title:
                for tag_name in self.tag_list:
                    # We want to make sure to add the movie's title to the
                    # similar list, so long as the movie's title isn't the same
                    # as this object's movie title
                    if tag_name in movie.tag_list and movie.title not in self.similar:
                        self.similar.append(movie.title)

