# FROM LECTURE
# APIs, REQUESTS, JSON 
# FROM 53:26


import json
import requests 
import sys 



# API
# application programming interface
# third-party services that our code can talk to.
# most APIs live on the internet.
# you can write code that pretends to be a browser, connects to a 
# third-part api on a server, and download some data that you can then incorporate
# into your program.


# requests library
# one of the most popular and commonly used lirabries. 
# can install via pip 
# allows you to make web requests, internet requests using python code 
# as though you were a browser yourself.
# you can automate the retrieval of URLs that start with HTTP, HTTPS.
# documentation: pypi.org/project/requests


# read the documentation on the itunes API
# you have to edit the URL a specific way on itunes.com to get a JSON file


# JSON
# JavaScript Object Notation 
# text-based format 
# a text file containing a bunch of key-value pairs, formatted similarly to a dictionary
# a language agnostic format, for exchanging data between computers 
# JSON uses the same formatting as python dictionaries 


if len(sys.argv) != 2:
    sys.exit()


# concatenates the name of the band to the API URL 
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # to print one song
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # to print 50 songs
# print(response.json())
# print(json.dumps(response.json(), indent=2))

# output for one song:
'''
{
  "resultCount": 1,
  "results": [
    {
      "wrapperType": "track",
      "kind": "song",
      "artistId": 115234,
      "collectionId": 1440868131,
      "trackId": 1440868258,
      "artistName": "Weezer",
      "collectionName": "Weezer (Green Album)",
      "trackName": "Island In the Sun",
      "collectionCensoredName": "Weezer (Green Album)",
      "trackCensoredName": "Island In the Sun",
      "artistViewUrl": "https://music.apple.com/us/artist/weezer/115234?uo=4",
      "collectionViewUrl": "https://music.apple.com/us/album/island-in-the-sun/1440868131?i=1440868258&uo=4",
      "trackViewUrl": "https://music.apple.com/us/album/island-in-the-sun/1440868131?i=1440868258&uo=4",
      "previewUrl": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/52/a6/03/52a6032e-39c0-fd3e-555d-ce683f3d9d31/mzaf_7707796819108024384.plus.aac.p.m4a",
      "artworkUrl30": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/30x30bb.jpg",
      "artworkUrl60": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/60x60bb.jpg",
      "artworkUrl100": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/fc/ef/19/fcef196c-3f81-e9da-f02a-b55d900e7d69/16UMGIM53162.rgb.jpg/100x100bb.jpg",
      "collectionPrice": 9.99,
      "trackPrice": 1.29,
      "releaseDate": "2002-05-14T12:00:00Z",
      "collectionExplicitness": "notExplicit",
      "trackExplicitness": "notExplicit",
      "discCount": 1,
      "discNumber": 1,
      "trackCount": 10,
      "trackNumber": 4,
      "trackTimeMillis": 200307,
      "country": "USA",
      "currency": "USD",
      "primaryGenreName": "Rock",
      "isStreamable": true
    }
  ]
}
'''

# to print keys from the one dictionary inside the list (results):
# create a variable to store the output
# then the loop will iterate through all keys once in the one dictionary and print out the "trackName" value
o = response.json()
for result in o["results"]:
    print(result["trackName"])





# LIST OF DICTIONARIES — HOW TO THINK ABOUT IT
#
# When you see:
# for result in o["results"]:
#
# Think:
# "For each ITEM inside o["results"], temporarily call it result."
#
# ------------------------------------------------------------
#
# 1. o["results"] is a LIST
#
# o["results"]
#      ↓
# [
#     {dictionary 1},
#     {dictionary 2},
#     {dictionary 3}
# ]
#
# ------------------------------------------------------------
#
# 2. The for loop takes ONE dictionary at a time
#
# for result in o["results"]:
#
# First iteration:
# result = {dictionary 1}
#
# Second iteration:
# result = {dictionary 2}
#
# Third iteration:
# result = {dictionary 3}
#
# ------------------------------------------------------------
#
# 3. result is therefore a DICTIONARY
#
# So we can access its values using a key:
#
# result["trackName"]
#
# Think:
# "Go inside this dictionary and get the value
#  belonging to the 'trackName' key."
#
# ------------------------------------------------------------
#
# THE BIG IDEA:
#
# for item in list:
#     item is ONE thing from the list
#
# If the list contains dictionaries:
#
# for item in list_of_dictionaries:
#     item is ONE dictionary
#
# ------------------------------------------------------------
#
# MENTAL SHORTCUT:
#
# "FOR EACH ITEM IN THE COLLECTION..."
#
# Ask yourself:
# 1. What am I looping through?
# 2. What is inside it?
# 3. Therefore, what is my loop variable?
#
# Example:
#
# for result in o["results"]:
#     print(result["trackName"])
#
# o["results"] → list
# list contains → dictionaries
# result → one dictionary
# result["trackName"] → value from that dictionary