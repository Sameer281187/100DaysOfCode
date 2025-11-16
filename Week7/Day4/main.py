from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def create_song_artist_dict(songs, artists):
    song_artist_list = []
    for i in range(len(songs)):
        item = {"song": songs[i],
                "artist": artists[i]}
        song_artist_list.append(item)
    return song_artist_list

date = input("Which year do you want to travel to? Enter the date in the format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")
songs = soup.select("li h3#title-of-a-story")
artists = soup.select("li h3#title-of-a-story+span")
top_songs = [item.text.strip() for item in songs]
top_artists = [item.text.strip() for item in artists]

top_songs_with_artists = create_song_artist_dict(top_songs, top_artists)

print(top_songs_with_artists)