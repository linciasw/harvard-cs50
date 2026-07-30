# STRING SLICING
# FROM CS50 SHORT 


# the first number in slicing is inclusive, 
# the second number is exclusive

def main():
    phone = "617-495-1000"
    print(phone[0:3]) # to access the first index (0) until it hit the third index exclusive ie first 3 numbers
    print(phone[:3]) # you can also leave the first index blank, python will assume you want to start from index 0
    print(phone[8:12]) # to get the last 4 digits 
    print(phone[8:])

    # getting to the last 4 numbers like this is not ideal
    # because if input is "+1-617-495-1000"
    # choosing the last specific index will be "95-1000"
    # the program will be broken
    # if the characters you want are always at the end of your string,
    # you can access them using negative numbers:

    print(phone[-4:])


main()