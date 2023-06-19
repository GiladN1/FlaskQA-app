from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    response = jsonify("server is up")
    return response


if __name__ == "__main__":
    app.run(debug=True)