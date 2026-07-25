# STRING METHODS 
# FROM CS50 SHORTS

# methods are functions that belong to some kind of object


SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron",
    "the Proud family"
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        # print(show.capitalize()) # only uppercases the first character in your string 
        # print(show.title()) # capitzalizes all words in string
        # print(show.strip()) # strips leading & trailing spaces
        # print(show.strip().title()) # methods can be chained
        cleaned_shows.append(show.strip().title())

    # print(cleaned_shows)
    # output: ['Avatar: The Last Airbender', 'Ben 10', 'Arthur', 'Spongebob Squarepants', 'Phineas And Ferb', 'Kim Possible', 'Jimmy Neutron', 'The Proud Family']

    print(', '.join(cleaned_shows))

main()