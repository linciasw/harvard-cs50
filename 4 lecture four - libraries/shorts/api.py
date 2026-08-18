# FROM SHORTS

# art institute of chicago API
# https://api.artic.edu/docs/


import requests


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    # the network connection can get interrupted while sending API requests.
    # we can use a try-except block

    try: 
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist} # research this using the documentation
            )
        response.raise_for_status() # if the API response does not give back the <Response [200]> everything is okay
        # print(response)
        # this outputs <Response [200]>, http status code that means everything is okay
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    
    content = response.json()
    # print(content)

    for artwork in content["data"]:
        print(f"* {artwork['title']}")


    # all you need to do to use an API is to read the documentation to find out 
    # the structure of the response you'll get back and what keys you should 
    # use and what values they would give. 



    

main()