'''
    This code was based on these repositories,
    so special thanks to:
        https://github.com/datademofun/spotify-flask
        https://github.com/drshrey/spotify-flask-auth-example

'''

from flask import Flask, request, redirect, g, render_template, session
from spotify_requests import spotify
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = 'some key for session'
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://pradhyuman:pradhyuman2002@face-detection.qi24f.mongodb.net/?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
client = MongoClient("mongodb+srv://pradhyuman:pradhyuman2002@face-detection.qi24f.mongodb.net/?retryWrites=true&w=majority")

# ----------------------- AUTH API PROCEDURE -------------------------

@app.route("/auth")
def auth():
    # return {"URL": "{}".format(spotify.AUTH_URL)}
    return redirect(spotify.AUTH_URL)


@app.route("/callback/")
def callback():

    auth_token = request.args['code']
    auth_header = spotify.authorize(auth_token)
    session['auth_header'] = auth_header
    # return {"isAuthenticated": True}
    return profile()    

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


@app.route('/search/<search_type>/<name>')
def search_item(search_type, name):
    return make_search(search_type, name)


def make_search(search_type, name):
    if search_type not in ['artist', 'album', 'playlist', 'track']:
        return render_template('index.html')

    data = spotify.search(search_type, name)
    api_url = data[search_type + 's']['href']
    items = data[search_type + 's']['items']

    return render_template('search.html',
                           name=name,
                           results=items,
                           api_url=api_url,
                           search_type=search_type)


@app.route('/artist/<id>')
def artist(id):
    artist = spotify.get_artist(id)

    if artist['images']:
        image_url = artist['images'][0]['url']
    else:
        image_url = 'http://bit.ly/2nXRRfX'

    tracksdata = spotify.get_artist_top_tracks(id)
    tracks = tracksdata['tracks']

    related = spotify.get_related_artists(id)
    related = related['artists']

    return render_template('artist.html',
                           artist=artist,
                           related_artists=related,
                           image_url=image_url,
                           tracks=tracks)


@app.route('/profile')
def profile():
    if 'auth_header' in session:
        auth_header = session['auth_header']
        # get profile data
        profile_data = spotify.get_users_profile(auth_header)

        # get user playlist data
        playlist_data = spotify.get_users_playlists(auth_header)

        # get user recently played tracks
        recently_played = spotify.get_users_recently_played(auth_header)
        
        if valid_token(recently_played):
            return render_template("profile.html",
                               user=profile_data,
                               playlists=playlist_data["items"],
                               recently_played=recently_played["items"])

    return render_template('profile.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/featured_playlists')
def featured_playlists():
    if 'auth_header' in session:
        auth_header = session['auth_header']
        hot = spotify.get_featured_playlists(auth_header)
        if valid_token(hot):
            return render_template('featured_playlists.html', hot=hot)

    return render_template('profile.html')


@app.route('/genres')
def genres():
    top = spotify.get_available_genres()
    return(top)

if __name__ == "__main__":
    app.run(debug=True, port=spotify.PORT)
