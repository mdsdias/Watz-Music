from flask import render_template, Flask, request
import client
import json
ap = Flask("Watz Music", template_folder="/pages")


@ap.route("/")
def index():
    return render_template("index.html")


@ap.route("/search/<query>")
def search(query):
    musics, playlists = client.search(query)
    mscs = musics
    plyts = playlists
    a = type(mscs)
    b = type(plyts)
    print(a, '\n', b)
    data = {
        "musics":{
            **mscs
        },
        "playlists": {
            **plyts
        },
    }
    return render_template("index.html", **data)
@ap.errorhandler(404)
def error404():
    return render_template("error.html")
ap.run()
