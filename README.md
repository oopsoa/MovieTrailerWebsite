## Movie Trailer Website using Python ##

This project showcases using classes in python to create a simple movie trailer website.

### About the Code ###

#### movie.py ####

This file has the code for a Movie class which has the following three attributes. 

1. Title
2. Youtube Trailer URL
3. Poster Image URL

The class also has a `show_trailer()` function that plays the trailer video. 

#### imdb_api.py ####

This file has the code for to call the imdb serivce to get a list of movies. 

#### movie_list.py ####

This calls the `imdb_api.py` to get a list of movies. The json response is converted into a list of movie objects.
The movie instance is created by passing the values to the `__init__` constructor of the Movie class in `movie.py`.

#### movie_site.py ####

This file has the code to call `movie_list.py` to create a list of movies. 

#### fresh_tomatoes.py ####

This file has the code to create the html page and render the movie trailers. The movie list is passed to the `open_movies_page` function.

### Installation, Setup and running the website ###

1. Install and setup python 3.6 or above
2. Download or Clone the project from the [MovieTrailerWebsite](https://github.com/oopsoa/MovieTrailerWebsite) github repository 
3. Run the following python script to launch the website `python movie_site.py`
4. `movie_trailer.html` file will be generated and launched with a list of movies received from imdb

### Rendered movie_trailer.html ###

The `open_movies_page` function call creates an html page that renders the movie trailers.

![alt text](/movie_trailer_html.png "Movie Trailer Website")



