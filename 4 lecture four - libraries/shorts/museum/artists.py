# FROM SHORTS
# this is a module that search.py is importing

import requests

def get_artists(query, limit):

    try: 
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search",
            {"q": query, "limit": limit} # research this using the documentation
            )
        response.raise_for_status() # if the API response does not give back the <Response [200]> everything is okay
        # print(response)
        # this outputs <Response [200]>, http status code that means everything is okay
    except requests.HTTPError:
        print("Couldn't complete request!")
        return []

    content = response.json() # research the .json() function
    return [artist["title"] for artist in content["data"]]
