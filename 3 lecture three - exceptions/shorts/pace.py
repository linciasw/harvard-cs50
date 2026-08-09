# FROM SHORTS
# RAISING EXCEPTIONS

'''
you can raise your own exceptions
ie define them.
see code below
'''


def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)}, minutes.")

def get_pace(miles, minutes):
    if not minutes > 0:
        # raise Exception()
        raise ValueError("Minutes must be greater than 0.")

    return minutes / miles



main()