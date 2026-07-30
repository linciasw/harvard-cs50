




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


  
# The if __name__ == "__main__": isn't there because main() doesn't work. 
# It's there to stop main() from running when another Python file imports yours.
if __name__ == "__main__":
    main()



# if __name__ == "__main__":
#     main()

# is simply asking:
# "Am I the file that the user started?"

# If yes:
# main()

# If no:
# Don't start—you're just being imported.