import requests
from datetime import datetime

API_KEY = 'API_KEY'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'
CITY = "London"

response1 = requests.get('http://api.openweathermap.org/geo/1.0/direct', params={
    'q': CITY,
    'appid': API_KEY
})

# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

x = response1.json()

print(response)
print("")
print(x)
print("")
print(x[0]["lat"])
print(x[0]["lon"])
