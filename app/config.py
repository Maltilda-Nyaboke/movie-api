class Config:
    '''
    General configuration parent class
    '''
    pass

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_KEY = '037c55d6b0ab6774fd8dcb27d1eaca9a'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=037c55d6b0ab6774fd8dcb27d1eaca9a'


class ProdConfig(Config):
    '''
    Pruduction  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    DEBUG = True





