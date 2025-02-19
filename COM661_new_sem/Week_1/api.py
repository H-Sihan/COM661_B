import requests

def get_weather(city):
    api_key = "0b3bdd00fa307fd362a0bce74e85ccf7"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found or API error!")
        
city = input("Enter a city: ")
get_weather(city)
