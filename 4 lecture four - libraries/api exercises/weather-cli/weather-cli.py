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


https://open-meteo.com/en/docs?hourly=&location_mode=csv_coordinates
https://www.geopythontutorials.com/notebooks/openmeteo_weather_forecast.html#get-daily-forecast


need to use geocoding to get the latitude and longitude from place name
https://nominatim.org/release-docs/latest/library/Getting-Started/#__tabbed_1_2


The API client is initialized with openmeteo_requests.Client, 
often wrapped with caching and retry logic. 
A query is then executed using weather_api(), which takes the URL and a parameter dictionary 
containing coordinates (latitude, longitude) and desired metrics (current, hourly)
'''


def main():


    import openmeteo_requests
    import sys



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
        "latitude": 52.52,
        "longitude": 13.41,
        "current": ["temperature_2m", "cloud_cover", "wind_speed_10m"],
    }

    # returns a list of responses
    # open-meteo can handle multiple locations in one request
    responses = openmeteo.weather_api(url, params = params)


    print(responses)
    # this outputs:
    # [<openmeteo_sdk.WeatherApiResponse.WeatherApiResponse object at 0x000001EE26A0CB80>]
    # to access the data inside this object,
    # you must use its specific FlatBuffers getter methods rather than printing the object directly. 
    # Because the data is encoded in a binary format, 
    # printing the object only shows its memory address.



    # view location metadata
    # 
    response = responses[0]

    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")


    # view current weather data (if requested in params)
    # be mindful of the order
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_cloud_cover = current.Variables(1).Value()
    current_wind_speed_2m = current.Variables(1).Value()

    # print(f"Current time: {current.Time()}")
    print(f"Current temperature_2m: {current_temperature_2m} ")
    print(f"Current cloud cover: {current_cloud_cover} ")
    print(f"Current wind speed_2m: {current_wind_speed_2m} ")


main()




"""
METADATA PRINTED OUT
print(dir(response))

['Current', 'Daily', 'Elevation', 'GenerationTimeMilliseconds', 'GetRootAs', 'GetRootAsWeatherApiResponse', 
 'Hourly', 'Init', 'Latitude', 'LocationId', 'Longitude', 'Minutely15', 'Model', 'Monthly', 'Timezone', 'TimezoneAbbreviation', 
 'UtcOffsetSeconds', 'Weekly', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', 
 '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__setattr__', '__sizeof__', '__slots__', '__static_attributes__', '__str__', '__subclasshook__', '_tab']
 """