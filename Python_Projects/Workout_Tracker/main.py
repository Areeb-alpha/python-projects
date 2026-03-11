import requests
import datetime as dt
import os

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")
USER_PASS = os.environ.get("USER_PASS")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
workout_api = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
workout_params = {
    "query": input("How many miles did you run? "),
    "weight_kg":"61",
    "height_cm":"167",
    "age":"22"
}
response = requests.post(url=workout_api,json=workout_params,headers=headers)
result = response.json()
print(result)
auhthentication_header ={
    "Authorization": USER_PASS
}
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

#
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs,headers=auhthentication_header)
    print(sheet_response.text)
# print(result)

