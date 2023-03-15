from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def index():
    title = "Hello World!"
    return render_template("index.html",title = title)

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and it's data
    '''
    pass

@app.route('/series')
def series():
    return render_template("series.html")