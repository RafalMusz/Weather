import time
import requests

#variables
API_KEY = "2c68d091a1efa9b941ccaeac859a2add"
BASE_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
City = "" # clean 
Decision = "" # clean

while Decision != "exit":
    Decision = input("load Your previos serched city ? Y/N:\n") 
        #Decision on load the previos search with loop
    if Decision == "y": 
        with open("city.txt") as file:
            City = file.read()
            print("Twoje miasto to ", City)
    else:
        City = input("Enter a city name: ")
    #Writing a city to the config file
        with open("city.txt", "w") as file: 
            file.write(City)
            
    #making of proper request 
    print("generating links....\n")
    request_url = f"{BASE_WEATHER_URL}?q={City}&appid={API_KEY}&units=metric"
    responses = requests.get(request_url)


    #geting info beck from api
    print("getting informations...\n")
    time.sleep(1)
    if responses.status_code == 200:
        data = responses.json()
        print(f"Weather in {City} is:")
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'])
        
        print("weather", weather)
        print("temperature", temperature, "celcius\n")
        
    else:
        time.sleep(1)
        print("Somthing went wrong with weather ;/")
        time.sleep(1)

# Make more cases if user make a wrong input