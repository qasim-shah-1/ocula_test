import requests
from datetime import datetime

API_KEY = '524f6e593d3def171e93835101352afa'
BASE_URL_DAY_SUMMARY = 'https://api.openweathermap.org/data/3.0/onecall/day_summary'


def get_coordinates(city: str):
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct', params={
        'q': city,
        'appid': API_KEY
    })
    data = response.json()
    print(data)

    if response.status_code != 200:
        raise Exception(f"City '{city}' not found or API error: {data}")

    return data[0]['lat'], data[0]['lon']


def get_day_summary_data(lat: float, lon: float, date: str):
    # Fetch daily summary weather data
    response = requests.get(BASE_URL_DAY_SUMMARY, params={
        'lat': lat,
        'lon': lon,
        'date': date,
        'appid': API_KEY
    })
    data = response.json()
    print(data)

    if 'temperature' not in data or 'humidity' not in data:
        raise Exception(f"Weather data not found or API error: {data}")

    temperature = data['temperature']
    humidity = data['humidity']

    min_temp = round(temperature.get('min') - 273.15, 1)
    max_temp = round(temperature.get('max') - 273.15, 1)
    avg_temp = round(temperature.get('afternoon') - 273.15, 1)

    return {
        'min_temp': min_temp,
        'max_temp': max_temp,
        'avg_temp': avg_temp,
        # Assuming 'afternoon' is a representative average
        'avg_humidity': round(humidity.get('afternoon'), 1)
    }


def get_weather_data(city: str, date: str):
    date_obj = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')

    # Get coordinates for the city
    lat, lon = get_coordinates(city)

    # Fetch daily summary weather data
    weather_data = get_day_summary_data(lat, lon, date_obj)

    return {
        'city': city,
        'date': date,
        **weather_data
    }
