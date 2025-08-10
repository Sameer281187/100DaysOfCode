from bs4 import BeautifulSoup
import requests

def write_to_file(item):
    with open("movies.txt", 'a') as file:
        file.write(f"{item} \n")

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
top_movies = soup.select("h2>strong")

top_rated_movies = [item.text for item in top_movies]
top_rated_movies = top_rated_movies[::-1]

for item in top_rated_movies:
    write_to_file(item)
