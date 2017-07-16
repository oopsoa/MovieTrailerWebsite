## Movie Trailer Website using Python ##

This project showcases using classes in python to create a simple movie trailer website.

### movie.py ###

This file has the code for a Movie class which has the following three attributes. 

1. Title
2. Trailer Url
3. Poster Image

The class also has a `show_trailer()` function that plays the trailer video. 

### movie_site.py ###

This file has the code to create a list of movie instances that uses the Movie class in `movie.py` to create instances of the movie class. The movie instance is created by passing the values to the `__init__` constructor of the Movie class.
   
### fresh_tomatoes.py ###

This file has the code to create the html page and render the movie trailers. The movie list is passed to the `open_movies_page` function.

### movie_trailer.html ###

The `open_movies_page` function call creates an html page that renders the movie trailers.

![alt text](/movie_trailer_html.png "Movie Trailer Website")

