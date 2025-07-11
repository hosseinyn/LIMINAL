import os
from flask import Flask, render_template, url_for, redirect , request , render_template_string
import json
import random
import string

from getpass import getuser

app = Flask(__name__)

app.jinja_env.globals["random"] = random

def randomString(range1, range2):
    length = random.randint(range1, range2)
    return str(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase +
                             string.digits, k=length)))

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("desktop"))

@app.route("/desktop", methods=["GET"])
def desktop():
    with open("data.json") as f:
        data = f.read()
    spaces = json.loads(data)
    random.shuffle(spaces)

    path = "static/styles/audios/songs"
    files = os.listdir(path)
    songs = [file for file in files]
    random.shuffle(songs)

    user_username = getuser()
  
    return render_template("desktop.html", spaces=spaces, songs=songs, randomString=randomString , username=user_username)

@app.route("/search")
def search():
    query = request.args.get("query")

    if not query:
        return render_template_string("<html><body><h1 style='color:#ec44ba'>You have to search!</h1></body></html>")

    with open("data.json") as f:
        data = f.read()
    spaces = json.loads(data)
    random.shuffle(spaces)

    return render_template("search.html" , query=query , results=spaces)

if __name__ == '__main__':
    app.run(debug=False)

