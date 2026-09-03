# ----------------------------TASK 3---------------------------------------

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
city = input("Enter City Name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\nWeather Report")
        print("-" * 30)
        print("City        :", city_name)
        print("Country     :", country)
        print("Temperature :", temperature, "°C")
        print("Humidity    :", humidity, "%")
        print("Condition   :", description.title())

    elif response.status_code == 404:
        print("City not found.")

    elif response.status_code == 401:
        print("Invalid API Key.")

    else:
        print("Error:", response.status_code)



except requests.exceptions.ConnectionError:
    print("No Internet Connection.")
except Exception as e:
    print("Something went wrong:", e)
