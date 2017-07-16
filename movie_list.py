import imdb_api
import json
import movie

def get_movie_list():
  movies_list_response = imdb_api.get_movies()
  movie_list = create_movie_list(movies_list_response)
  return movie_list

def create_movie_list(movies_json):
  movie_list = []
  for movie in movies_json:
    movie_list.append(create_movie(movie))
  return movie_list

def create_movie(movie_json):
  title = movie_json['title']
  poster_image_url = get_poster_url(movie_json['poster_path'])
  trailer_url = get_trailer_url(movie_json['id'])
  movie_object = movie.Movie(title, trailer_url, poster_image_url)
  return movie_object

def get_poster_url(partial_url):
  poster_url = "http://image.tmdb.org/t/p/w185/" + partial_url
  return poster_url

def get_trailer_url(movie_id):
  trailer_url = "https://www.youtube.com/watch?v=" + imdb_api.get_youtube_key(movie_id)
  return trailer_url
