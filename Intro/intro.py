from flask import Flask

app=Flask(__name__)
@app.route('/')
def intro():
    return 'first app '