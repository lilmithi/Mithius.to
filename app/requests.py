from app import app
import urllib.request, json
from .models import movie, series

api_key = app.config["MOVIE_API_KEY"]
Movie = movie.Movie
Series = series.Series
movie_base_url = app.config["MOVIE_API_BASE_URL"]
tv_base_url = app.config["TV_API_BASE_URL"]

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = movie_base_url.format(category, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list, "movies")

        return movie_results
    
def get_series(category):
    '''
    Function that gets the json response to our url request
    '''
    get_series_url = tv_base_url.format(category, api_key)

    with urllib.request.urlopen(get_series_url) as url:
        get_series_data = url.read()
        get_series_response = json.loads(get_series_data)

        series_results = None

        if get_series_response['results']:
            series_results_list = get_series_response['results']
            series_results = process_results(series_results_list, "series")

        return series_results
    
def get_movie(id):
    '''
    Function that returns a movie's details
    Args:
        id: Movie's id whose details are sought after
    '''
    get_movie_url = movie_base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_url) as url:
        get_movie_data = url.read()
        get_movie_response = json.loads(get_movie_data)

        movie_object = None
        if get_movie_response:
            id = get_movie_response.get('id') 
            genre = get_movie_response.get('genre_ids')
            title = get_movie_response.get('original_title')
            language = get_movie_response.get('original_language')
            imageurl = get_movie_response.get('poster_path')
            release_date = get_movie_response.get('release_date')
            popularity = get_movie_response.get('popularity')
            overview = get_movie_response.get('overview')
            rating = round(get_movie_response.get('vote_average'), 1)

            movie_object = Movie(id, genre, title, language, imageurl, release_date, popularity, overview, rating)
        return movie_object
    
def get_tv_show(id):
    '''
    Function that returns a series's details
    Args:
        id: Series's id whose details are sought after
    '''
    get_tv_url = tv_base_url.format(id, api_key)

    with urllib.request.urlopen(get_tv_url) as url:
        get_tv_data = url.read()
        get_tv_response = json.loads(get_tv_data)

        tv_object = None
        if get_tv_response:
            id = get_tv_response.get('id') 
            genre = get_tv_response.get('genre_ids')
            title = get_tv_response.get('name')
            origin_country = get_tv_response.get('origin_country')[0]
            language = get_tv_response.get('original_language')
            imageurl = get_tv_response.get('poster_path')
            release_date = get_tv_response.get('release_date')
            popularity = get_tv_response.get('popularity')
            overview = get_tv_response.get('overview')
            rating = round(get_tv_response.get('vote_average'), 1)

            tv_object = Series(id, genre, title, origin_country, language, imageurl, release_date, popularity, overview, rating)
        return tv_object

    
def process_results(show_list, show_type):
    '''
    Function that processes the show's result and transform them into a list of objects
    Args:
        show_list: A list of dictionaries containing either movie or tv details
        show_type: Type of show; either movies or series
    returns: A list of either movie or series objects
    '''
    show_results = []

    if show_type == "movies":
        for show_item in show_list:
            id = show_item.get('id') 
            genre = show_item.get('genre_ids')
            title = show_item.get('original_title')
            language = show_item.get('original_language')
            imageurl = show_item.get('poster_path')
            release_date = show_item.get('release_date')
            popularity = show_item.get('popularity')
            overview = show_item.get('overview')
            rating = round(show_item.get('vote_average'), 1)

            if imageurl:
                movie_object = Movie(id, genre, title, language, imageurl, release_date, popularity, overview, rating)
                show_results.append(movie_object)
    else:
        for show_item in show_list:
            id = show_item.get('id') 
            genre = show_item.get('genre_ids')
            title = show_item.get('name')
            origin_country = show_item.get('origin_country')[0]
            language = show_item.get('original_language')
            imageurl = show_item.get('poster_path')
            release_date = show_item.get('release_date')
            popularity = show_item.get('popularity')
            overview = show_item.get('overview')
            rating = round(show_item.get('vote_average'), 1)

            if imageurl:
                series_object = Series(id, genre, title, origin_country, language, imageurl, release_date, popularity, overview, rating)
                show_results.append(series_object)

    return show_results