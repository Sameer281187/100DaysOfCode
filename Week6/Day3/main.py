import datetime
import requests
import os

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_API_KEY")
SHEETY_USERNAME = "844d953279ababaa2f68f0dafcd4cd8c"

nutritionix_api_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api_url = f"https://api.sheety.co/{SHEETY_USERNAME}/myWorkouts/workouts"



user_query = input("Tell me what execrcise you did? ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
parameters = {
    "query" : user_query,
}

response = requests.post(url=nutritionix_api_url, json=parameters, headers=headers)
response.raise_for_status()

exercise_data = response.json()

date = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
exercise = [item["user_input"].title() for item in exercise_data["exercises"]]
duration = [item["duration_min"] for item in exercise_data["exercises"]]
calories = [item["nf_calories"] for item in exercise_data["exercises"]]

head = {
    "Authorization" : os.environ.get("SHEETY_API_KEY")
}

for i in range(len(exercise)):
    body = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" : exercise[i],
            "duration" : duration[i],
            "calories" : calories[i]
        }
    }

    workout_data = requests.post(url=sheety_api_url, json=body, headers=head)
    workout_data.raise_for_status()