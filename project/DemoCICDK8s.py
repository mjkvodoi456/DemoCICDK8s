from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "Demo CICD with K8s!"
