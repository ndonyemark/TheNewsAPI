import os

class Config():

    SECRET_KEY = os.environ.get("SECRET_KEY")
    NEWS_BASE_URL = "https://newsapi.org/v2/sources?apiKey={}"
    NEWS_ARTICLES_URL = "https://newsapi.org/v2/everything?q={}&apiKey={}"
    API_KEY = os.environ.get("API_KEY")

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig
}