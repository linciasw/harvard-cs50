distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}


def main():
    # to loop over and return all keys in dictionary
    # for name in distances.keys():
    #     print(f"{name} is {distances[name]} AU from Earth")


    # to loop over and convert all distance values 
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")



def convert(au):
    return au * 149597870700


main()