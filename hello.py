from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("Visit the hello page")
    return "Hello World!"

