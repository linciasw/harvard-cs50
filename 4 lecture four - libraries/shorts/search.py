# FROM SHORTS
# THIS IS THE ORIGINAL FILE

# from artwork import get_artworks
# from artists import get_artists

from museum.artists import get_artists


# from *module name* import *this function*

# def main():
#     artwork = input("Artwork: ")
#     artworks = get_artworks(query=artwork, limit=3)
#     for artwork in artworks:
#         print(f"* {artwork}")



def main():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3)
    for artist in artists:
        print(f"* {artist}")


main()