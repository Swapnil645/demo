from flask import Flask
from six.moves import xrange

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()

