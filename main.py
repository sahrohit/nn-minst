from os import environ
from flask import Flask
from flask_cors import CORS

app = Flask("nn-minst")
CORS(app)


@app.route("/", methods=["GET"])
def ping():
    return f"Pinging Model Application {environ.get('ENVIRONMENT')}"


if __name__ == "__main__":
    app.run(debug=True, port=9696)
