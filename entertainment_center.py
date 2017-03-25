#import the media module with the blueprint of the Movie class

import media

#import the fresh_tomatoes modules with the HTML code needed to generate the webpage

import fresh_tomatoes

print "---------------------Entertainment Center Setup---------------------"
print ""
print "Welcome to the Movie website creation wizard. Please follow the instructions on the screen."

# initiate an empty list that will serve as a placeholder for all the movies
    
movies = []

ans = raw_input("Would you like to add a movie? [y/n]: ")

# ask the users whether they want to add details of the movies
# repeat the question if the answear is neither "YES" nor "NO"

while ans not in ["y", "n"]:
    print "*****"
    print "Please answer yes [y] or no [n]"
    ans = raw_input("Would you like to add a movie? [y/n]: ")
while ans != "n":

    # ask the user for movie details
    print ""
    print "Please enter a valid movie title: "    
    movie_title = raw_input()
    print ""
    print "Please enter a short storyline: "
    storyline = raw_input()
    print ""
    print "Please enter a url of the poster image: "
    poster_url = raw_input()
    print ""
    print "Please enter a url of the movie trailer: "
    movie_url = raw_input()
        
    # modify the input name so that it can be used as a variable name
        
    title = movie_title.lower()
    title = title.replace(" ", "_")

    # create an instance of a Movie class
        
    title = media.Movie(movie_title, 
                        storyline,
                        poster_url,
                        movie_url)
        
    # add this instance to the movies list
        
    movies.append(title)
    
    # ask the user whether they would like to include an additional movie
    
    print ""
    
    ans = raw_input("Would you like to add a movie? [y/n]: ")
    while ans not in ["y", "n"]:
        print "*****"
        print "Please answer yes [y] or no [n]"
        ans = raw_input("Would you like to add a movie? [y/n]: ")
        
print "Application will try to generate a webpage."
    

if len(movies) > 0:
                                                        
    fresh_tomatoes.open_movies_page(movies)
    
else:
    print "*****"
    print "The user did not provide any details. The application will close."
    print "Have a nice day!"
