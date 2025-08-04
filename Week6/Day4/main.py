from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
flight_search = FlightSearch()
sheet_data = data.get_prices()

for item in sheet_data:
    item["iataCode"] = flight_search.get_iata_code(item["city"])
    request_body = {
        "iataCode" : item["iataCode"],
    }
    data.update_rows(item["id"], request_body)
