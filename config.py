import os
import instance
# import app 
# import main

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'

    MOVIE_API_KEY = os.environ.get("MOVIE_API_KEY")

    SECRET_KEY = os.environ.get("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://victoria:pass@localhost/watchlist'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProdConfig(Config):
    '''
    Production  configuration child class

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