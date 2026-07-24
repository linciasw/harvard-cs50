# WHILE LOOPS
# FROM CS50 SHORTS 




from soil import sample

# def main():
#     moisture = sample()
#     print(f"Moisture is {moisture}%")
    

# main()

# to get the program to keep checking the moisture of thesoil
# until it's dry, to then alert of that, to water it
# we can use a while loop


# while loops are great when you're not sure how many times you
# want to loop, but you want to loop while some condition is True 
def main():
    moisture = sample()
    days = 0
    print(f"Day {days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days += 1
        print(f"Day {days}: Moisture is {moisture}")

    print("Time to water!")
    

main()