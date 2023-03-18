from show import Show
class Movie(Show):
    '''
    Movie class to define movie objects
    '''
    def __init__(self, id, genre, title, language, imageurl, media_type, release_date, popularity, overview, rating) -> None:
        super().__init__(id, genre, title, language, imageurl, media_type, release_date, popularity, overview, rating)

