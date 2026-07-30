# FOR LOOPS
# FROM CS50 SHORTS
# powerful when you know how many times you want to loop 
# or when you want to do something for each item you 
# have in some list 
# or generally, anything iterable that can be iterated over


# this program works but it could be designed better 
# instead of multiple print statements, use a for loop and a list
def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # for i in range(len(names)):
    #     # print(names[i]) # to access all names
    #     print(write_letter(names[i], "Princess Peach"))


    # another more readable way of writing the above for loop:
    for name in names:
        print(write_letter(name, "Princess Peach"))



    # print(write_letter("Mario", "Princess Peach"))
    # print(write_letter("Luigi", "Princess Peach"))
    # print(write_letter("Daisy", "Princess Peach"))
    # print(write_letter("Yoshi", "Princess Peach"))



def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's Castle this evening, 7:00 PM. 

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()