import os

class Config():

    SECRET_KEY = os.environ.get("SECRET_KEY")
    NEWS_BASE_URL = ""
    NEWS_ARTICLES_URL = ""
    API_KEY = os.environ.get("API_KEY")

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig
}