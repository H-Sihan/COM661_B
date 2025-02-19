import requests

api_key = "0b3bdd00fa307fd362a0bce74e85ccf7"

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q':city, 'appid':api_key,'units': 'metric'}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found")

def get_weather_forecast(city):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {'q':city, 'appid':api_key,'units': 'metric'}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print("Weather forecast for " + data['city']['name'])
        print(f"{data['cnt']} forecast retrieve")
        
        for forecast in data['list'][:4]:
            Temperature = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"Temp: {Temperature},Desc: {description}")
    else:
        print("City not found")   
    
city = input("Enter a City: ")
get_weather(city)
get_weather_forecast(city)