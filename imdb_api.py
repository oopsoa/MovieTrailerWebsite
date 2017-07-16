import requests

API_URL = 'https://api.themoviedb.org/3'
API_KEY = '23da819564151522ea34dec29e90d954'

def get_movies(URL = 'https://api.themoviedb.org/3/discover/movie?api_key=63deb316427624bb95cf1d828e19b7a2&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'): # noqa
	response = requests.get(URL)
	return response.json()['results']

def get_movie_api_url():
	return API_URL + '/movie?api_key=' + API_KEY + '&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'

def get_youtube_key(movie_id):
	trailerURL = API_URL + '/movie/' + str(movie_id) + '/videos?api_key='+ API_KEY + '&language=en-US'
	response = requests.get(trailerURL)
	return response.json()['results'][0]['key']
