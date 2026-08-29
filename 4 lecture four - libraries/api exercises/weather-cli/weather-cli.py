'''
1. 🌤️ Weather CLI
API: Open-Meteo
API Key: Not required
Difficulty: ⭐⭐

Goal
Build a command-line weather program.

python weather.py Port_of_Spain

Example output:
Port of Spain
Temperature: 29°C
Wind: 18 km/h
Weather: Partly cloudy

Practice:
    requests.get()
    Query parameters with params=
    JSON
    Dictionaries
    Lists
    Command-line arguments
    Reading API documentation


    
WEATHER API
https://open-meteo.com/en/docs?hourly=&location_mode=csv_coordinates


GOECODING API (NEEDED TO CHANGE NAMES TO COORDINATES FOR THE WEATHER API)
https://open-meteo.com/en/docs/geocoding-api


RANDOM
https://www.geopythontutorials.com/notebooks/openmeteo_weather_forecast.html#get-daily-forecast



The API client is initialized with openmeteo_requests.Client, 
often wrapped with caching and retry logic. 
A query is then executed using weather_api(), which takes the URL and a parameter dictionary 
containing coordinates (latitude, longitude) and desired metrics (current, hourly)
'''



def get_coordinates():

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
        # print(latitude, longitude)


    return latitude, longitude



def get_weather(latitude, longitude):


    import openmeteo_requests


    # create a client object
    openmeteo = openmeteo_requests.Client()

    # open-meteo endpoint
    # the /v1/forecast endpoint is the normal weather forecast API
    url = "https://api.open-meteo.com/v1/forecast"



    # where, what data, which weather measurements
    # latitude, longitude are the only required parameters
    # current, hourly and daily are the different dictionaries here; it matches
    # with the checkboxes on the api site 
    # 2m means 2 metres above ground
    params = {
        "latitude": float(latitude),
        "longitude": float(longitude),
        "current": ["weather_code", "cloud_cover", "wind_speed_10m"],
    }

    # returns a list of responses
    # open-meteo can handle multiple locations in one request
    responses = openmeteo.weather_api(url, params = params)



    # DEBUGGING 
    # print(responses)
    # this outputs:
    # [<openmeteo_sdk.WeatherApiResponse.WeatherApiResponse object at 0x000001EE26A0CB80>]
    # to access the data inside this object,
    # you must use its specific FlatBuffers getter methods rather than printing the object directly. 
    # Because the data is encoded in a binary format, 
    # printing the object only shows its memory address.


    # print(type(responses))
    # this outputs:
    # <class 'list'>
    # you have the type of object you're interacting with


    # print(dir(response))
    # this outputs:
    # you can drill into the object a little more
    # ['Current', 'Daily', 'Elevation', 'GenerationTimeMilliseconds', 'GetRootAs', 'GetRootAsWeatherApiResponse', 
    # 'Hourly', 'Init', 'Latitude', 'LocationId', 'Longitude', 'Minutely15', 'Model', 'Monthly', 'Timezone', 'TimezoneAbbreviation', 
    # 'UtcOffsetSeconds', 'Weekly', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
    # '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
    # '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
    # '__setattr__', '__sizeof__', '__slots__', '__static_attributes__', '__str__', '__subclasshook__', '_tab']



    # help(responses)
    # help on particular object
    # shows the methods/functions you can use on it



    # view location metadata
    # response is equal to the first list
    # even if there is only one location in the list, we still need to initialize it 
    response = responses[0]

    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
    print()


    # put in temperature variable
    # view current weather data (if requested in params)
    # be mindful of the order
    current = response.Current()
    current_weather_code = current.Variables(0).Value()
    current_cloud_cover = current.Variables(1).Value()
    current_wind_speed_10m = current.Variables(2).Value()
    current_temperature_2m = current.Variables(3).Value()


    # write conditionals for weather code 
    # write conditions for cloud cover


    print(f"===== Current Weather === ")
    # print(f"Current time: {current.Time()}")
    print(f"Current weather_code: {current_weather_code} ")
    print(f"Current cloud cover: {current_cloud_cover:,.0f} ")
    print(f"Current wind speed_10m: {current_wind_speed_10m:,.0f}km/h ")
    print(f"Current temperature_2m: {current_temperature_2m:,.0f} ")



    # cloud cover:
    # %
    # Total cloud cover as an area fraction 
    # Cloud Cover Categories and Percentages0% to 10% (Clear / Sunny): The sky is mostly or completely free of clouds. You will see bright, uninterrupted sunshine.
    # 10% to 25% (Few / Mostly Clear): Only a few small clouds are visible. Most of the sky remains open and clear.
    # 25% to 50% (Scattered / Partly Cloudy): Clouds cover up to half of the sky. You get a mix of bright sunshine and passing cloud patches.
    # 50% to 90% (Broken / Mostly Cloudy): Most of the sky is hidden by a heavy layer of clouds. Sunlight only breaks through occasionally.
    # 90% to 100% (Overcast / Cloudy): The entire sky is completely filled with a solid blanket of clouds. 
    # No patches of blue sky or direct sunlight are visible.


    # weather code:
    # WMO Weather interpretation codes (WW):
    # Code	Description
    # 0	Clear sky
    # 1, 2, 3	Mainly clear, partly cloudy, and overcast
    # 45, 48	Fog and depositing rime fog
    # 51, 53, 55	Drizzle: Light, moderate, and dense intensity
    # 56, 57	Freezing Drizzle: Light and dense intensity
    # 61, 63, 65	Rain: Slight, moderate and heavy intensity
    # 66, 67	Freezing Rain: Light and heavy intensity
    # 71, 73, 75	Snow fall: Slight, moderate, and heavy intensity
    # 77	Snow grains
    # 80, 81, 82	Rain showers: Slight, moderate, and violent
    # 85, 86	Snow showers slight and heavy
    # 95 *	Thunderstorm: Slight or moderate
    # 96, 99 *	Thunderstorm with slight and heavy hail


    # wind speed:
    # kmh




def main():
    
    latitude, longitude = get_coordinates()
    get_weather(latitude, longitude)


main()







