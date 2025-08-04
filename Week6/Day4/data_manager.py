import requests
import os

SHEETY_API_TOKEN_FLIGHTS = os.environ.get("SHEETY_API_TOKEN_FLIGHTS")
RETRIEVE_API = "https://api.sheety.co/844d953279ababaa2f68f0dafcd4cd8c/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.header = {
            "Authorization" : SHEETY_API_TOKEN_FLIGHTS,
        }

    def read_data(self):
        response = requests.get(RETRIEVE_API, headers=self.header)
        return response

    def update_rows(self, row_id, request_body):
        body = {
            "price" : request_body,
        }
        api_url = f"{RETRIEVE_API}/{row_id}"
        requests.put(url=api_url, json=body, headers=self.header)

    def get_prices(self):
        api_response = self.read_data()
        return api_response.json()["prices"]
