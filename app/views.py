from app import app
from flask import render_template

@app.route('/')
def index():
    title = "Hello World!"
    return render_template("index.html",title = title)

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route('/series')
def series():
    return render_template("series.html")