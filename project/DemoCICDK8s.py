from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "MSS4.0 MENTORING SUPPORT SYSTEM"
