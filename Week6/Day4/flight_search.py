import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:
    def __init__(self):
        self._api_key = "7VUuD8wu3FHKmcgzd2iR6NpgPV1x6WXe"
        self._api_secret = "wQsVU96TPehu1oIE"
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        data = response.json()
        return data["access_token"]

    def get_city_information(self, city):
        parameter = {
            "keyword" : city
        }

        headers = {
            "Authorization": f"Bearer {self._token}"
        }

        res = requests.get(url=CITY_SEARCH_ENDPOINT, headers=headers, params=parameter)
        return res.json()["data"]

    def get_iata_code(self, city):
        value = self.get_city_information(city)
        return value[0]["iataCode"]

