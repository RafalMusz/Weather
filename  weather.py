from urllib import request, response
import requests

API_KEY = "2c68d091a1efa9b941ccaeac859a2add"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

City = input("Enter a city name: ")
request_url = f"{BASE_URL}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"]
    print(weather)

else:
    print("Somthing went wrong ;/ ")