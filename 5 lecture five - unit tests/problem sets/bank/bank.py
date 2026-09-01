# startswith() method is pretty common

# list of common string methods:
# .startswith()
# .endswith()
# .lower()
# .upper()
# .strip()
# .replace()
# .split()
# .join()
# .find()



def main(): 

    user_input = input("Greeting: ")

    money_given = value(user_input)
    print(money_given)





def value(greeting):

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else: 
        return 100
    



main()