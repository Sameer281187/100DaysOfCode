import requests
import wikipedia


class CommonUtils:
    def __init__(self):
        pass

    def get_image(self, query):
        page = wikipedia.page(query)
        return page.images[0]

    def download_image(self, url):
        headers = {
            'User-Agent': 'MyWikipediaDataFetcher/1.0 (contact@example.com)'
        }
        response = requests.get(url=url, headers=headers)
        with open("files/output_file.jpg", "wb") as file:
            file.write(response.content)
