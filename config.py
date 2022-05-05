import os


class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class Config:
    '''
    General configuration parent class
    '''
    pass

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '<Movie API Key>'
    SECRET_KEY = '<Flask WTF Secret Key>'
    MOVIE_API_KEY = '037c55d6b0ab6774fd8dcb27d1eaca9a'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:New password@localhost/watchlist'
    


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

config_options = {
'development':DevConfig,
'production':ProdConfig
}





