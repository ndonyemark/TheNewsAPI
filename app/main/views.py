from . import main
from flask import render_template, request, redirect

@main.route("/")
def index():

    title="News Api app"
    return render_template("index.html", title=title)