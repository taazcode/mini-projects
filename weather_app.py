import requests


def get_weather(city) :
    """Fetch current temperature (°C) for a city via OpenWeatherMap."""
    api_key = "906e3b0a61da2d483355900ca883a121"
    if not api_key:
        print("Error: set the OPENWEATHER_API_KEY environment variable.")
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        r = requests.get(url, params=params, timeout=15)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

    if r.status_code == 200:
        data = r.json()
        temp=data["main"]["temp"]
        print(f"{city}: {temp}°C")
        return temp




get_weather("tripura")