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
    greeting = input("Greeting: ")


    if greeting.startswith("hello"):
        say_greeting("$0")
    elif greeting.startswith("h"):
        say_greeting("$20")
    else: 
        say_greeting("$100")




def say_greeting(finalGreeting):
    print(finalGreeting)


main()