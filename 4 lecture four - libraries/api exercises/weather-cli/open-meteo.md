# 🌤️ Open-Meteo + `openmeteo_requests` — Complete Reference Note

> **Purpose:** Understand how the Open-Meteo API and the `openmeteo_requests` Python library work, especially requests, parameters, response objects, metadata, weather-data sections, and navigating the returned data.

---

# 1. The Big Picture

There are several layers involved:

```text
Your Python Program
        ↓
openmeteo_requests
        ↓
Open-Meteo HTTP API
        ↓
Weather Data
```

The important distinction is:

* **Open-Meteo** = the actual weather API/service
* **`openmeteo_requests`** = a Python client/library that makes it easier to communicate with Open-Meteo
* **Your Python program** = uses the client and processes the returned data

---

# 2. Importing the Library

```python
import openmeteo_requests
```

This imports the `openmeteo_requests` Python module.

At this point:

```text
openmeteo_requests
```

refers to the **module**.

It contains things such as the `Client` class.

---

# 3. Creating a Client

```python
client = openmeteo_requests.Client()
```

This creates a **Client object**.

The distinction is:

```text
openmeteo_requests
        ↓
      Client
        ↓
   Client object
```

### Module

```python
openmeteo_requests
```

### Class

```python
openmeteo_requests.Client
```

### Object/instance

```python
openmeteo_requests.Client()
```

### Stored object

```python
client = openmeteo_requests.Client()
```

Now `client` refers to the Client object.

---

# 4. Calling `weather_api()`

Once the client exists:

```python
responses = client.weather_api(url, params=params)
```

The `weather_api()` method belongs to the Client object.

You can think of the chain as:

```text
openmeteo_requests
        ↓
      Client
        ↓
    client object
        ↓
   weather_api()
        ↓
   API response
```

You could technically write:

```python
responses = openmeteo_requests.Client().weather_api(
    url,
    params=params
)
```

but normally you create the client separately:

```python
client = openmeteo_requests.Client()

responses = client.weather_api(
    url,
    params=params
)
```

This is easier to read and lets you reuse the client.

---

# 5. The API URL

For the standard Open-Meteo forecast API:

```python
url = "https://api.open-meteo.com/v1/forecast"
```

The URL tells the client which API endpoint you are communicating with.

Conceptually:

```text
https://api.open-meteo.com
        ↓
Open-Meteo server

/v1/forecast
        ↓
Forecast endpoint
```

Different endpoints can have different parameters and capabilities.

---

# 6. Parameters (`params`)

The `params` dictionary contains instructions that you send to the API.

Example:

```python
params = {
    "latitude": 10.5,
    "longitude": -61.4,
    "current": ["temperature_2m"]
}
```

Think of the parameters as answering questions:

```text
WHERE?
    latitude
    longitude

WHAT WEATHER DATA?
    current

WHICH VARIABLES?
    temperature_2m
```

---

# 7. Parameters and HTTP Requests

This is closely related to the `requests` library.

With `requests`, you might do:

```python
response = requests.get(
    url,
    params=params
)
```

The parameters are conceptually turned into query parameters in the URL.

For example:

```python
params = {
    "latitude": 10.5,
    "longitude": -61.4
}
```

is conceptually similar to:

```text
https://api.open-meteo.com/v1/forecast
?latitude=10.5
&longitude=-61.4
```

You don't normally construct that URL manually.

The library handles the request.

---

# 8. Required Location Parameters

For the normal forecast endpoint, the basic location information is:

```python
"latitude"
"longitude"
```

Example:

```python
params = {
    "latitude": 10.5,
    "longitude": -61.4
}
```

These coordinates tell Open-Meteo **where** you want weather information.

---

# 9. Location Names vs Coordinates

Open-Meteo primarily works with coordinates.

You might start with:

```text
"Chaguanas"
```

and use a geocoding service/API to turn it into:

```text
latitude
longitude
```

Then send those coordinates to Open-Meteo.

The overall workflow can therefore be:

```text
Place name
    ↓
Geocoding API
    ↓
Latitude + Longitude
    ↓
Open-Meteo
    ↓
Weather data
```

This is a common real-world API workflow.

---

# 10. The `current` Parameter

Example:

```python
"current": [
    "temperature_2m",
    "relative_humidity_2m"
]
```

This tells Open-Meteo:

> Return the current values for these weather variables.

For example:

```python
params = {
    "latitude": 10.5,
    "longitude": -61.4,

    "current": [
        "temperature_2m",
        "relative_humidity_2m"
    ]
}
```

---

# 11. What Does `temperature_2m` Mean?

```text
temperature_2m
             ↑
             2 metres
```

The `2m` refers to the reference height of the temperature measurement/model.

It does **not** mean the unit.

The unit is something such as:

```text
°C
°F
```

Similarly:

```text
wind_speed_10m
             ↑
             10 metres
```

means wind speed at 10 metres above the ground.

---

# 12. Common Current Weather Variables

Open-Meteo provides many possible variables.

Some useful categories include:

## Temperature

```text
temperature_2m
apparent_temperature
```

`temperature_2m`:

> Air temperature at 2 metres.

`apparent_temperature`:

> The "feels like" temperature.

---

## Humidity / Moisture

```text
relative_humidity_2m
dew_point_2m
```

Relative humidity:

> How close the air is to being saturated with water vapor.

Dew point:

> Temperature at which condensation begins under the relevant conditions.

---

## Precipitation

Examples include:

```text
precipitation
rain
showers
snowfall
```

---

## Clouds / Weather Conditions

```text
weather_code
cloud_cover
```

`weather_code` represents the weather condition using a numerical code.

The numerical code can represent conditions such as:

```text
Clear
Cloudy
Fog
Rain
Snow
Thunderstorm
```

---

## Wind

```text
wind_speed_10m
wind_direction_10m
wind_gusts_10m
```

Again:

```text
10m
```

refers to the reference height.

---

## Pressure

Example:

```text
surface_pressure
```

---

## Radiation / Solar Variables

Open-Meteo also provides variables related to solar radiation, such as:

```text
shortwave_radiation
direct_radiation
diffuse_radiation
direct_normal_irradiance
terrestrial_radiation
```

These become particularly useful for applications involving solar energy.

---

## Soil Variables

Open-Meteo also provides soil-related measurements at different depths.

These can be useful for:

```text
Agriculture
Irrigation
Environmental analysis
```

---

## Evapotranspiration

Open-Meteo provides evapotranspiration-related variables.

This is broadly concerned with water moving into the atmosphere through:

```text
Evaporation
+
Plant transpiration
```

---

# 13. `current` vs `hourly` vs `daily`

This is one of the most important concepts.

## Current

```python
"current": [
    "temperature_2m"
]
```

means:

> Give me the current temperature.

Conceptually:

```text
Current
   ↓
ONE current value
```

---

## Hourly

```python
"hourly": [
    "temperature_2m",
    "precipitation"
]
```

means:

> Give me a time series of these variables by hour.

Conceptually:

```text
Hourly
│
├── 08:00 → 27°C
├── 09:00 → 28°C
├── 10:00 → 29°C
├── 11:00 → 30°C
└── ...
```

Hourly data contains many values associated with different times.

---

## Daily

```python
"daily": [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum"
]
```

means:

> Give me daily summary/aggregate values.

Conceptually:

```text
Date       Max     Min     Rain

Aug 28     31°C    24°C    2.3 mm
Aug 29     30°C    24°C    7.1 mm
Aug 30     32°C    25°C    0.0 mm
```

---

# 14. Combining Current, Hourly and Daily

You can request multiple sections in one request.

Example:

```python
params = {
    "latitude": 10.5,
    "longitude": -61.4,

    "current": [
        "temperature_2m",
        "relative_humidity_2m"
    ],

    "hourly": [
        "temperature_2m",
        "precipitation"
    ],

    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum"
    ]
}
```

This asks for:

```text
CURRENT
    ↓
What is happening now?

HOURLY
    ↓
What is happening hour by hour?

DAILY
    ↓
What happens each day?
```

---

# 15. Units

You can specify units using parameters.

## Temperature

```python
"temperature_unit": "celsius"
```

or:

```python
"temperature_unit": "fahrenheit"
```

---

## Wind

For example:

```python
"wind_speed_unit": "kmh"
```

or:

```python
"wind_speed_unit": "mph"
```

---

## Precipitation

For example:

```python
"precipitation_unit": "mm"
```

or:

```python
"precipitation_unit": "inch"
```

The API performs the unit selection/conversion according to the parameter.

---

# 16. Timezone

You can specify the timezone:

```python
"timezone": "America/Port_of_Spain"
```

This is especially important for hourly and daily data.

Weather data is associated with timestamps, so you need to know what timezone those timestamps represent.

---

# 17. Forecast Days

You can control how many forecast days are requested.

Example:

```python
"forecast_days": 7
```

Conceptually:

```text
Today
Tomorrow
Day 3
Day 4
Day 5
Day 6
Day 7
```

---

# 18. Past Days

You can also request past days when supported:

```python
"past_days": 3
```

This means you can include previous days alongside forecast information.

---

# 19. The API Response

After making the request:

```python
responses = client.weather_api(
    url,
    params=params
)
```

you receive a collection of response objects.

The important point is:

```text
responses
```

is not necessarily one individual response object.

It is a collection capable of containing responses for multiple locations.

---

# 20. Why `responses[0]`?

You may see:

```python
response = responses[0]
```

This is standard Python indexing.

Python starts counting at zero:

```python
responses[0]   # first item
responses[1]   # second item
responses[2]   # third item
```

Therefore:

```python
response = responses[0]
```

means:

> Take the first response from the collection and store it in the variable `response`.

---

# 21. Why Is There a Collection If I Only Requested One Location?

If you provide:

```python
"latitude": 10.5,
"longitude": -61.4
```

you requested one location.

Conceptually, the result can still be represented as:

```text
responses
│
└── [0]
      ↓
   Response
```

Therefore:

```python
response = responses[0]
```

gets the one response.

The collection structure also allows the library/API to handle multiple locations.

---

# 22. Multiple Locations

You can conceptually request multiple locations by providing multiple coordinates.

For example:

```python
params = {
    "latitude": [10.5, 10.65],
    "longitude": [-61.4, -61.5],
    "current": ["temperature_2m"]
}
```

Conceptually:

```text
responses
│
├── [0] → Location 1
└── [1] → Location 2
```

Therefore:

```python
responses[0]
```

is the first response.

And:

```python
responses[1]
```

is the second response.

---

# 23. The Response Object

After:

```python
response = responses[0]
```

you now have one Open-Meteo response object.

You can inspect it:

```python
print(type(response))
```

You can also inspect its available methods/attributes:

```python
print(dir(response))
```

---

# 24. Your Actual `dir(response)` Output

You printed:

```text
[
    'Current',
    'Daily',
    'Elevation',
    'GenerationTimeMilliseconds',
    'GetRootAs',
    'GetRootAsWeatherApiResponse',
    'Hourly',
    'Init',
    'Latitude',
    'LocationId',
    'Longitude',
    'Minutely15',
    'Model',
    'Monthly',
    'Timezone',
    'TimezoneAbbreviation',
    'UtcOffsetSeconds',
    'Weekly',
    '__class__',
    '__delattr__',
    '__dir__',
    '__doc__',
    '__eq__',
    '__firstlineno__',
    '__format__',
    '__ge__',
    '__getattribute__',
    '__getstate__',
    '__gt__',
    '__hash__',
    '__init__',
    '__init_subclass__',
    '__le__',
    '__lt__',
    '__module__',
    '__ne__',
    '__new__',
    '__reduce__',
    '__reduce_ex__',
    '__repr__',
    '__setattr__',
    '__sizeof__',
    '__slots__',
    '__static_attributes__',
    '__str__',
    '__subclasshook__',
    '_tab'
]
```

This is extremely useful because it shows the actual structure exposed by your installed library.

---

# 25. The Important Parts of `dir(response)`

Ignore most of the Python internal methods for now.

Focus on:

```text
Current
Daily
Hourly
Minutely15
Monthly
Weekly
```

These are weather-data sections.

Also focus on:

```text
Latitude
Longitude
Elevation
LocationId
Timezone
TimezoneAbbreviation
UtcOffsetSeconds
Model
GenerationTimeMilliseconds
```

These are primarily metadata/information about the response.

---

# 26. Response Structure

A useful mental model is:

```text
RESPONSE
│
├── METADATA
│   │
│   ├── Latitude
│   ├── Longitude
│   ├── Elevation
│   ├── LocationId
│   ├── Timezone
│   ├── TimezoneAbbreviation
│   ├── UtcOffsetSeconds
│   ├── Model
│   └── GenerationTimeMilliseconds
│
└── WEATHER DATA
    │
    ├── Current
    ├── Minutely15
    ├── Hourly
    ├── Daily
    ├── Weekly
    └── Monthly
```

The exact sections available can depend on the API/client version and endpoint.

---

# 27. Metadata

Metadata is information **about the response/location/model**, rather than a weather measurement itself.

Examples:

```python
response.Latitude()
response.Longitude()
response.Elevation()
response.LocationId()
response.Timezone()
response.TimezoneAbbreviation()
response.UtcOffsetSeconds()
response.Model()
response.GenerationTimeMilliseconds()
```

For example:

```python
print("Latitude:", response.Latitude())
print("Longitude:", response.Longitude())
print("Elevation:", response.Elevation())
print("Location ID:", response.LocationId())
print("Timezone:", response.Timezone())
print("Timezone abbreviation:", response.TimezoneAbbreviation())
print("UTC offset:", response.UtcOffsetSeconds())
print("Model:", response.Model())
print("Generation time:", response.GenerationTimeMilliseconds())
```

---

# 28. Metadata vs Weather Data

This distinction is extremely important.

Think:

```text
RESPONSE
│
├── INFORMATION ABOUT THE RESPONSE
│       ↓
│   Metadata
│
└── INFORMATION ABOUT THE WEATHER
        ↓
    Weather data
```

For example:

```text
Latitude
Longitude
Elevation
Timezone
```

describe the location/response.

While:

```text
Temperature
Humidity
Wind
Rain
```

describe the weather.

---

# 29. `Current()`

To access current weather:

```python
current = response.Current()
```

Now:

```text
response
    ↓
Current()
    ↓
current object
```

You can inspect the current object:

```python
print(type(current))
print(dir(current))
```

You may see methods such as:

```text
Time
Interval
Variables
```

---

# 30. Current Response Structure

Conceptually:

```text
response
   │
   └── Current()
          │
          ├── Time()
          ├── Interval()
          └── Variables()
```

The actual weather variables you requested are accessed through `Variables()`.

---

# 31. `Variables(0)`

Suppose your request contains:

```python
"current": [
    "temperature_2m",
    "relative_humidity_2m"
]
```

The variables are ordered:

```text
0 → temperature_2m
1 → relative_humidity_2m
```

Therefore:

```python
current.Variables(0)
```

refers to the first requested variable.

And:

```python
current.Variables(1)
```

refers to the second.

---

# 32. Getting the Actual Value

You can then use:

```python
current.Variables(0).Value()
```

Conceptually:

```text
Current
   ↓
Variables
   ↓
Variable #0
   ↓
Value
```

For example:

```python
temperature = current.Variables(0).Value()
```

might produce:

```text
29.4
```

If:

```python
current.Variables(1).Value()
```

represents humidity, it might produce:

```text
78
```

---

# 33. Why the Order Matters

If you request:

```python
"current": [
    "temperature_2m",
    "relative_humidity_2m",
    "wind_speed_10m"
]
```

then:

```text
Variables(0) → temperature_2m
Variables(1) → relative_humidity_2m
Variables(2) → wind_speed_10m
```

But if you change the request to:

```python
"current": [
    "wind_speed_10m",
    "temperature_2m",
    "relative_humidity_2m"
]
```

then:

```text
Variables(0) → wind_speed_10m
Variables(1) → temperature_2m
Variables(2) → relative_humidity_2m
```

The indexes correspond to the order of the requested variables.

---

# 34. Hourly Structure

If you request:

```python
"hourly": [
    "temperature_2m",
    "precipitation"
]
```

the response contains a time series.

Conceptually:

```text
HOURLY
│
├── Time
│   ├── 08:00
│   ├── 09:00
│   ├── 10:00
│   └── ...
│
├── Temperature
│   ├── 27
│   ├── 28
│   ├── 29
│   └── ...
│
└── Precipitation
    ├── 0.0
    ├── 0.2
    ├── 1.1
    └── ...
```

Hourly data therefore represents:

```text
Many values
+
Their corresponding times
```

---

# 35. Daily Structure

Daily data works similarly but at a daily level.

Example:

```python
"daily": [
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum"
]
```

Conceptually:

```text
DAILY
│
├── Date
│
├── Maximum temperature
│
├── Minimum temperature
│
└── Total precipitation
```

Example:

```text
Date       Max     Min     Rain

Aug 28     31°C    24°C    2.3 mm
Aug 29     30°C    24°C    7.1 mm
Aug 30     32°C    25°C    0.0 mm
```

---

# 36. Other Sections in Your Library

Your `dir(response)` showed:

```text
Current
Minutely15
Hourly
Daily
Weekly
Monthly
```

Conceptually:

```text
Current
    ↓
Current conditions

Minutely15
    ↓
15-minute interval data

Hourly
    ↓
Hourly time series

Daily
    ↓
Daily data

Weekly
    ↓
Weekly data

Monthly
    ↓
Monthly data
```

Do not assume every section automatically contains data.

The data available depends on:

* The endpoint
* Your requested parameters
* The API/client version
* The type of data being requested

---

# 37. FlatBuffers

One reason `openmeteo_requests` looks different from a simple JSON API is that it uses a **FlatBuffers-based response representation**.

This is why you see methods such as:

```python
response.Latitude()
response.Current()
current.Variables(0)
current.Variables(0).Value()
```

Instead of something more familiar like:

```python
data["current"]["temperature_2m"]
```

You are navigating an object generated from the FlatBuffers schema.

---

# 38. JSON vs `openmeteo_requests`

With a normal JSON API using `requests`, you might do:

```python
import requests

response = requests.get(url, params=params)

data = response.json()
```

and then access:

```python
data["current"]["temperature_2m"]
```

Conceptually:

```text
HTTP response
      ↓
JSON
      ↓
Python dictionary
      ↓
data["current"]
      ↓
["temperature_2m"]
```

With `openmeteo_requests`:

```text
HTTP response
      ↓
FlatBuffers representation
      ↓
Open-Meteo response object
      ↓
Current()
      ↓
Variables()
      ↓
Value()
```

This is why the syntax feels different.

---

# 39. Object Navigation

A useful mental model is:

```text
response
   │
   ├── Metadata
   │
   └── Weather-data section
          │
          └── Variables
                 │
                 └── Value
```

For example:

```python
response.Current().Variables(0).Value()
```

can be read in English as:

> From the response, get the current-weather section, get variable number 0, then get its value.

---

# 40. Inspecting Objects Yourself

Python provides useful tools for exploring unfamiliar objects.

## `type()`

Use:

```python
print(type(response))
```

to find out what type of object something is.

Example:

```text
<class '...WeatherApiResponse...'>
```

---

## `dir()`

Use:

```python
print(dir(response))
```

to see the object's available methods/attributes.

This is especially useful when learning an unfamiliar library.

---

## `help()`

You can also use:

```python
help(response)
```

or:

```python
help(response.Current)
```

to get information about the object/method.

---

# 41. A Good Exploration Workflow

When you encounter a new API/library, don't immediately try to memorize everything.

Instead:

```text
1. Make request
      ↓
2. Check type()
      ↓
3. Check dir()
      ↓
4. Pick something interesting
      ↓
5. Explore that object
      ↓
6. Check its type()
      ↓
7. Check its dir()
      ↓
8. Retrieve a value
```

For Open-Meteo:

```python
responses = client.weather_api(url, params=params)

print(type(responses))

response = responses[0]

print(type(response))
print(dir(response))

current = response.Current()

print(type(current))
print(dir(current))

variable = current.Variables(0)

print(type(variable))
print(dir(variable))

print(variable.Value())
```

---

# 42. Complete Beginner Example

```python
import openmeteo_requests

client = openmeteo_requests.Client()

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 10.5,
    "longitude": -61.4,

    "current": [
        "temperature_2m",
        "relative_humidity_2m"
    ],

    "temperature_unit": "celsius",

    "timezone": "America/Port_of_Spain"
}

responses = client.weather_api(
    url,
    params=params
)

response = responses[0]

current = response.Current()

temperature = current.Variables(0).Value()
humidity = current.Variables(1).Value()

print("Temperature:", temperature)
print("Humidity:", humidity)
```

Conceptually:

```text
CREATE CLIENT
      ↓
DEFINE URL
      ↓
DEFINE PARAMETERS
      ↓
SEND REQUEST
      ↓
GET RESPONSES
      ↓
GET FIRST RESPONSE
      ↓
GET CURRENT WEATHER
      ↓
GET VARIABLES
      ↓
GET VALUES
      ↓
PRINT DATA
```

---

# 43. The Most Important Mental Model

When looking at Open-Meteo, think:

```text
                    RESPONSE
                       │
        ┌──────────────┴──────────────┐
        │                             │
     METADATA                    WEATHER DATA
        │                             │
        │                  ┌──────────┼───────────┐
        │                  │          │           │
   Latitude             Current    Hourly       Daily
   Longitude               │          │           │
   Elevation               │          │           │
   Timezone                │          │           │
   Model                   │          │           │
                           ↓          ↓           ↓
                       Variables   Time series  Summaries
                           │
                           ↓
                         Value
```

Your parameters determine what weather data you receive.

---

# 44. Don't Try to Memorize Every Open-Meteo Variable

Open-Meteo has a large catalogue of weather variables.

You don't need to memorize them.

Treat the documentation as a **catalogue/reference**.

When you need something:

```text
"I need wind speed."
        ↓
Look at documentation.
        ↓
Find variable name.
        ↓
Add it to params.
        ↓
Request it.
        ↓
Retrieve it from response.
```

For example:

```python
"current": [
    "temperature_2m",
    "wind_speed_10m"
]
```

The transferable skill is understanding:

```text
Documentation
      ↓
Parameters
      ↓
HTTP request
      ↓
Response
      ↓
Object structure
      ↓
Extract data
```

---

# 45. The Five Concepts to Master First

You do **not** need to master every Open-Meteo feature immediately.

Focus on these five:

## 1. Parameters

```python
params = {
    "latitude": ...,
    "longitude": ...,
    "current": [...]
}
```

Understand:

> What am I asking the API for?

---

## 2. Response

```python
responses = client.weather_api(...)
```

Understand:

> What did the API give me?

---

## 3. Collection/list

```python
responses[0]
```

Understand:

> Why am I indexing the response?

---

## 4. Response object

```python
response = responses[0]
```

Understand:

> What methods/data does this object expose?

Use:

```python
dir(response)
```

---

## 5. Navigating the data

```python
response.Current().Variables(0).Value()
```

Understand:

> How do I move through the response object to get the value I want?

---

# 46. The Core Idea

The most important thing to remember is:

```text
PARAMETERS
    ↓
Tell the API what you want

RESPONSE
    ↓
Contains what the API returned

METADATA
    ↓
Information about the response/location

CURRENT
    ↓
Current weather

HOURLY
    ↓
Hourly time series

DAILY
    ↓
Daily summaries

VARIABLES
    ↓
Specific requested weather measurements

VALUE
    ↓
The actual numerical value
```

Once this structure makes sense, the individual Open-Meteo variable names become much easier to learn.

---

# 47. Quick Cheat Sheet

```python
# Import
import openmeteo_requests

# Create client
client = openmeteo_requests.Client()

# Endpoint
url = "https://api.open-meteo.com/v1/forecast"

# Request parameters
params = {
    "latitude": 10.5,
    "longitude": -61.4,

    "current": [
        "temperature_2m",
        "relative_humidity_2m"
    ],

    "timezone": "America/Port_of_Spain"
}

# Send request
responses = client.weather_api(
    url,
    params=params
)

# Get first response
response = responses[0]

# Metadata
latitude = response.Latitude()
longitude = response.Longitude()
elevation = response.Elevation()
timezone = response.Timezone()

# Current weather
current = response.Current()

# First requested variable
temperature = current.Variables(0).Value()

# Second requested variable
humidity = current.Variables(1).Value()
```

---

# 48. Final Mental Model

When you see:

```python
response = responses[0]
```

think:

> "I received a collection of response objects. Give me the first one."

When you see:

```python
current = response.Current()
```

think:

> "From that response, give me the current-weather section."

When you see:

```python
current.Variables(0)
```

think:

> "Give me the first weather variable I requested."

When you see:

```python
current.Variables(0).Value()
```

think:

> "Give me the actual value of that variable."

And when you see:

```python
params = {...}
```

think:

> **"This is my set of instructions to the API."**

That is the foundation you need before worrying about all the advanced Open-Meteo variables.
