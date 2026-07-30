# from shorts, not lecture
# side effects
# local versus global variable 


"""
NOTES FROM CHATGPT:

a side effect is anything a function does besides returning a value.
for example:
- print()
- Writing to a file
- Reading user input with input()
- Modifying a list, dictionary, or set passed into a function
- Changing a global variable
- Sending data over a network
- Making an API request
- Updating a database

functions without side effects, ie just returning a value 
are called pure functions.

functions with side effects can be harder to reason about because
they can change the program's state.

a simple rule to identify side effects:
"did this function do anything besides compute and return a value?"

as you continue learning pythin, you'll find that real-world programs often
need side effects (such as saving files or displaying information), but it's
generally good practice to keep your computational logic as pure as possible 
and isolate side effects to the parts of your program that interact with the 
outside world.

"""



# this program is an example of changing a global variable 
emoticon = "v.v" # global variable



def main():
    global emoticon # need to say this to change global variable 
    say("Is anyone there?")
    emoticon = ":D" 
    say("Oh, hi!")

    

def say(phrase):
    print(phrase + " " + emoticon)


main()