#import the webbrowser module 
import webbrowser

#define the movie class as a blueprint for all the movies

class Movie(object): 
    """This class stores information about movies such as:
       * title
       * short storyline
       * url of the movie poster
       * url of the movie trailer """
       
    #create a class variable storing all the possible ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    #create an instance of a movie object by providing the required parameters
    def __init__(self, title, story_line, poster_image_url, trailer_youtube_url):
        
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    #create a new method in order to open the trailer url in the default browser
    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        