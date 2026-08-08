# FROM SHORTS
# HANDLING EXCEPTIONS


distances  = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU" 
}


'''
choosing Pioneer 2 would give a:
"ValueError: could not convert string to float: '80 AU'".
a try-except block would help.
if the user chooses a spacecraft that's not on the list, that will give a :
"KeyError: 'James Webb Space Telscope'"

as you write code, try to anticipate these errors, and write code to 
handle them. 
it's good practice to be as specific as possible with the errors.
'''

def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float")
        return

    m = convert(au)
    print(f"{m} m away")



def convert(au):
    return au * 149597870700


main()