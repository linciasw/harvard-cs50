




def main():
    meal_time = input("What time is it? 24-hour format ")
    convert(meal_time)
    


def convert(time):
    hour, minutes = time.split(":")
    x = float(hour)
    y = float(minutes)
    z = y / 60 # divide by 60 to get the minutes as a decimal of the hour 
    w = x + z
    

    if w > 7 and w <= 8:
        print("breakfast time")
    elif w > 12 and w <= 13:
        print("lunch time")
    elif w > 18 and w <= 19:
        print("dinner time")
    else:
        print("")

    
    
if __name__ == "__main__":
    main()