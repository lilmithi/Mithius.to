class Show:
    '''
    Show parent class
    '''
    reviews = []

    def __init__(self, id, genre, title, language, imageurl, release_date, popularity, overview, rating) -> None:
        self.id = id
        self.genre = genre
        self.title = title
        self.language = language
        self.imageurl = 'https://image.tmdb.org/t/p/w500/'+ imageurl
        self.release_date = release_date
        self.popularity = popularity
        self.overview = overview
        self.rating = rating

    