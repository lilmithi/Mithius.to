from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    title = "Hello World!"
    return render_template("index.html",title = title)

# Movies

@app.route('/movies')
def movies():
    return render_template("show-main.html", type = "movies")

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and it's data
    '''
    pass

@app.route('/movies-popular')
def popular_movies():
    '''
    View movie function that returns popular movies
    '''
    return render_template("popular.html", type = "movies")

@app.route('/movies-az')
def az_movies():
    '''
    View movie function that returns A-Z page
    '''
    return render_template("az.html", type = "movies")

@app.route('/movies-genre')
def genre_movies():
    '''
    View movie function that returns movies based on genre
    '''
    return render_template("genre.html", type = "movies")

@app.route('/movies-language')
def movies_language():
    '''
    View movie function that returns movies based on language
    '''
    return render_template("language.html", type = "movies")

@app.route('/movies-year')
def movies_year():
    '''
    View movie function that returns movies based on year
    '''
    return render_template("year.html", type = "movies")

# Series

@app.route('/series')
def series():
    return render_template("show-main.html", type = "series")

@app.route('/series/<int:tv_id>')
def tv_show(tv_id):
    '''
    View tv show page function that returns the tv details page and it's data
    '''
    pass


@app.route('/series-popular')
def popular_series():
    '''
    View series function that returns popular series
    '''
    return render_template("popular.html", type = "series")

@app.route('/series-az')
def az_series():
    '''
    View series function that returns A-Z page
    '''
    return render_template("az.html", type = "series")

@app.route('/series-genre')
def genre_series():
    '''
    View series function that returns series based on genre
    '''
    return render_template("genre.html", type = "series")

@app.route('/series-language')
def series_language():
    '''
    View series function that returns series based on language
    '''
    return render_template("language.html", type = "series")

@app.route('/series-year')
def series_year():
    '''
    View series function that returns series based on year
    '''
    return render_template("year.html", type = "series")
