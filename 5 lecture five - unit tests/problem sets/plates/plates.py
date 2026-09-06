'''
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

'''

def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




def is_valid(s):

    # checks to see if plate starts with 2 letters
    if s[0:2].isdigit(): 
        return False



    # checks to see if there are numbers in the middle:
    # Find the first number. 
    # Once you encounter a number, everything after it must be a number.
    # we'll use a for loop, the range function, a conditional and some slicing
    for i in range(2, len(s)): # start at 2nd index, end at the length of s
        if s[i].isdigit(): # if 2nd index is a digit, go on to the if, else break and go to 3rd index
            if not s[i:].isdigit(): # if 2nd index to the end is not a digit, return False
                return False
            break



    # checks to see if the first number is zero
    if s[0] == "0":
        return False


    # checks to see if plate has a max of 6 characters and a min of 2
    if len(s) < 2 or len(s) > 6:
        return False





if __name__ == "__main__":
    main()