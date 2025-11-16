import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAuthentication():
    def __init__(self):
        redirect_uri = "https://example.com"

    def authenticate(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="6bf212c58a984eeb93c5f317f6e7a6d2",
                                               client_secret= "6595abb9bdd8428581395f4ecb6b7a90",
                                               redirect_uri= self.redirect_uri,
                                               scope="playlist-modify-private"))