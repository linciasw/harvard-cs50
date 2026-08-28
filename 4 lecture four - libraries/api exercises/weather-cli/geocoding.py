


# https://geocoding-api.open-meteo.com/v1/search?name=port+of+spain&count=10&language=en&format=json


import requests


location = input("Location: ")


response = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params = {
        "name": location,
        "language": "en",
        "format": "json",
        "count": 1,
    }
    
)


content = response.json()
# print(content)

for data in content['results']:
    # print(f"{data['latitude']}, {data['longitude']}")
    latitude = data['latitude']
    longitude = data['longitude']
    print(latitude, longitude)
