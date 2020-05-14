from . import main
from flask import render_template, request, redirect
from ..requests import get_sources, get_articles

@main.route("/", methods=["GET", "POST"])
def index():

    general = get_sources('general')
    business_source_data = get_sources('business')
    sports_source_data = get_sources('sports')
    entertainment_source_data = get_sources('entertainment')
    title = "The Times"
    return render_template("index.html", title = title, business_news_sources = business_source_data, sports_news_sources = sports_source_data, general_news_sources = general, entertainment_news_sources = entertainment_source_data)

@main.route("/business", methods=["GET", "POST"])
def business_articles():
    business_articles = get_articles("business")
    print(business_articles)
    return render_template("business.html", business = business_articles)

@main.route("/sports", methods=["GET", "POST"])
def sports_articles():
    sports_articles = get_articles("sports")
    print(sports_articles)
    return render_template("sports.html", sports = sports_articles)

@main.route("/entertainment", methods=["GET", "POST"])
def entertainment_articles():
    entertainment_articles = get_articles("entertainment")
    print(entertainment_articles)
    return render_template("entertainment.html", entertainment = entertainment_articles)