from http.client import responses
import requests

API_KEY = "2c68d091a1efa9b941ccaeac859a2add"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

City = input("Enter a city name: ")

print("generating links....\n")
request_url = f"{BASE_WEATHER_URL}?q={City}&appid={API_KEY}&units=metric"
responses = requests.get(request_url)

print("getting informations...\n")
if responses.status_code == 200:
    data = responses.json()
    print(f"Weather in {City} is:")
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'])
    
    print("weather", weather)
    print("temperature", temperature, "celciusza\n")
    
else:
    print("Somthing went wrong with weather ;/")
