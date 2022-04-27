from flask import Flask
from daily import *

app=Flask(__name__)
@app.route('/')
def intro():
    #home.html
    return get_all_to_do()
@app.route("/about")
def about():
    return "<h1>about my flask app</h1>"


if __name__=="_main_":
    app.run(debug=True)