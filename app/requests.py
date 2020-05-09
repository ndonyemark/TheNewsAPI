import urllib.request, json
from .models import News

api_key = None
base_url = None
articles_url =None

def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_URL']