import requests


API_KEY = "0dde44cb02ed667850275cf6b3d92cd3"

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': 'city',
            'appid': API_KEY,
            'units': 'metric'
            }
    try:

        temperature = requests.get(base_url, params=params)
        temperature.raise_for_status()

        weather_data = temperature.json()
        print(f"\nWeather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")


    except requests.exceptions.RequestException as e:
        print(f"Request failed {e}")
    except KeyError:
        print("Error:  Invalid API response format.")

        
get_weather("Tashkent")