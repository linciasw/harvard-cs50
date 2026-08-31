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


# TO DO 
# put in try-except error handling
# put in conditionals for cloud cover
# put in conditionals for weather code 



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
        "current": ["weather_code", "cloud_cover", "wind_speed_10m", "temperature_2m"],
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

    print(f"Coordinates: Latitude ({response.Latitude()}°N), Longitude({response.Longitude()}°E)")
    print(f"Elevation: {response.Elevation()}m asl")
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

    if current_weather_code == 0:
        weather_code = "Clear Sky"
    elif current_weather_code in (1, 2, 3):
        weather_code = "Mainly clear, partly cloudy, or overcast"
    elif current_weather_code in (45, 48):
        weather_code = "Fog"
    elif current_weather_code in (51, 53, 55):
        weather_code = "Drizzle"
    elif current_weather_code in (56, 57):
        weather_code = "Freezing drizzle"
    elif current_weather_code in (61, 63, 65):
        weather_code = "Rain"
    elif current_weather_code in (66, 67):
        weather_code = "Freezing rain"
    elif current_weather_code in (71, 73, 75):
        weather_code = "Snow fall"
    elif current_weather_code == 77:
        weather_code = "Snow grains"
    elif current_weather_code in (80, 81, 82):
        weather_code = "Rain showers"
    elif current_weather_code in (85, 86):
        weather_code = "Snow showers"
    elif current_weather_code == 95:
        weather_code = "Thunderstorm"
    elif current_weather_code in (96, 99):
        weather_code = "Thunderstorm with hail"
    else:
        weather_code = "Unknown weather condition"






    if current_cloud_cover > 0 and current_cloud_cover <= 10:
        cloud_cover = "Clear/Sunny Skies"
    elif current_cloud_cover > 10 and current_cloud_cover <= 25:
        cloud_cover = "Few Clouds/Mostly Clear Skies"
    elif current_cloud_cover > 25 and current_cloud_cover <= 50:
        cloud_cover = "Scatted/Partly Cloudly Skies"
    elif current_cloud_cover > 50 and current_cloud_cover <= 90:
        cloud_cover = "Broken/Mostly Cloudly Skies"
    elif current_cloud_cover > 90 and current_cloud_cover <= 100:
        cloud_cover = "Overcast/Coudly Skies"
    else:
        cloud_cover = "No pathces of blue sky or direct sunlight are visible"

        ...







    # write conditionals for weather code 
    # write conditions for cloud cover


    print(f"===== Current Weather === ")
    # print(f"Current time: {current.Time()}")
    print(f"Current weather_code: {weather_code} ")
    print(f"Current cloud cover: {cloud_cover} ")
    print(f"Current wind speed_10m: {current_wind_speed_10m:,.0f}km/h ")
    print(f"Current temperature_2m: {current_temperature_2m:,.0f}°C")






    # wind speed:
    # kmh




def main():
    
    latitude, longitude = get_coordinates()
    get_weather(latitude, longitude)


main()







