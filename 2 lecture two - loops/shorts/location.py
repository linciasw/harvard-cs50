# TUPLES
# FROM CS50 SHORTS

import sys

def main():
    # coordinates = (42.376, -71.115)
    # print(f"Latitude: {coordinates[0]}")
    # print(f"Longitude: {coordinates[1]}")


    # tuples could be unpacked into separate variables 
    # latitude, longitude = coordinates
    # print(f"Latitude: {latitude}")
    # print(f"Longitude: {longitude}")

    # why use tuples and not lists?:
    # tuples are mutable ie it cannot be changed
    # when you're certain the data would not need to be changed,
    # using a tuple is a more efficient way of representing collections
    # of data 
    # tuples take up less space in memory
    coordinate_tuple = (42.376, -71.115)
    coordinate_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")




main()