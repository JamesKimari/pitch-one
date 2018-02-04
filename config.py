import os

class Config:
    """
    General configuratins parent class
    """
    SECRET_KEY = os.environ.get('SECRET KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasaris:maisiewilliams7@localhost/pitchez'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    """
    Production configuration child class
    """
    pass

class DevConfig(Config):
    """
    Development config child class
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasaris:maisiewilliams7@localhost/pitchez'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

