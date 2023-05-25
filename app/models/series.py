# from show import Show
from app.models.show import Show

class Series(Show):
    '''
    Series child class to create series objects
    '''
    def __init__(self, id, genre, title, origin_country, language, imageurl, release_date, popularity, overview, rating) -> None:
        super().__init__(id, genre, title, language, imageurl, release_date, popularity, overview, rating)
        self.origin_country = origin_country