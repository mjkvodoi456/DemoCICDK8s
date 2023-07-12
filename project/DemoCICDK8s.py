from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "Devil may cry s5"
