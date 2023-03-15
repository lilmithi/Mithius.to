class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    TV_API_BASE_URL = 'https://api.themoviedb.org/3/tv/{}?api_key={}'
    
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development Configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True