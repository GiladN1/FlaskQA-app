from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")