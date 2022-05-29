from turtle import home
from flask import Flask, request, redirect, g, render_template, session
from spotify_requests import spotify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.secret_key = 'some key for session'
CORS(app, support_credentials=True)


# ----------------------- AUTH API PROCEDURE -------------------------

@app.route("/auth")
def auth():
    return {"URL": "{}".format(spotify.AUTH_URL)}


@app.route("/callback/")
def callback():

    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header

    return redirect("http://localhost:3000/homepage")

def valid_token(resp):
    return resp is not None and not 'error' in resp

# -------------------------- API REQUESTS ----------------------------


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/search/')
def search():
    try:
        search_type = request.args['search_type']
        name = request.args['name']
        return make_search(search_type, name)
    except:
        return render_template('search.html')
