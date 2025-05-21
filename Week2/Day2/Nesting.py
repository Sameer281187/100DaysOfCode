travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

for country in travel_log:
    for city in travel_log[country]:
        if city == "Lille":
            print(city)