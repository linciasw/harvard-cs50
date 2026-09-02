

def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")




def is_valid(s):

    if s[0:2].isdigit(): 
        return False
    
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False


    for character in s:
        if s[0:5] == "0":
            return False




if __name__ == "__main__":
    main()