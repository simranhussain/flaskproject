from flask import Flask, render_template, request
from datetime import datetime

app = Flask (__name__)


# @app.route("/")

# def welcome():
# return "welcome to flask"

# @app.route("/date")

# def date():
# return "welcome to flask " + str(datetime.now())

# counter = 0

# @app.route("/count_views")

# def count_viewss():
# global counter
# counter+=1
# return "the page has been viewed " + str(counter) + ' times'

@app.route("/add_card", methods = ["GET", "POST"])
def add_card():
    #if request.method == "POST":
   # else:
    return render_template("add_card.html")
