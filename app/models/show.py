class Show:
    '''
    Show parent class
    '''
    reviews = []

    def __init__(self, id, genre, title, language, imageurl, media_type, release_date, popularity, overview, rating) -> None:
        self.id = id
        self.genre = genre
        self.title = title
        self.language = language
        self.imageurl = imageurl
        self.media_type = media_type
        self.release_date = release_date
        self.popularity = popularity
        self.overview = overview
        self.rating = rating

    