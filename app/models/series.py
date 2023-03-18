from show import Show
class Series(Show):
    '''
    Series child class to create series objects
    '''
    def __init__(self, id, genre, title, language, imageurl, media_type, release_date, popularity, overview, rating) -> None:
        super().__init__(id, genre, title, language, imageurl, media_type, release_date, popularity, overview, rating)