
#ask user for their name
#name = input("What's your name? ") #input only accepts text to prompt user
name = input("What's your name?").strip().title()


#to split user's name into first name and last name
first, last = name.split(" ")



#print documentation 
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) 

# Say hello to user 
#print("hello ," + name) #using operators does not add a space
#print("hello,", name) #when passing in 2 arguments, python puts the space for you 
#print("hello,", name, sep="???") 



#STR
#to remove whitespace from str
#strip() #a method
#methods are built in to functions
#needs to go before the print()
#name = name.strip() #in case the user enters spaces before or after input 

#capitalizes first letter 
#name = name.capitalize()

#capitalizes first letter of all words
#name = name.title()


#you can chain methods together or add them onto the input (see above input)
#name = name.strip().title()
#you can combine as many methods as you like





#f-strings (got added to python 3.16)
#print(f"hello, {name}")

#to call split
print(f"hello, {name}")



#to place inverted commas in the output, use different ones 
#print('hello, "friend"')

#you can also put escape characters to get inverted commas
#print("hello, \"friend\"")


#print adds a new line automatically
#print("hello, ", end="") #this overrides the new line print places at the end of the statement
#print(name)



#python is not only a language, it's also a program that translates
#human language code into ones and zeros for the computer - an intepreter
#you can run programs by doing python *name of file* in the terminal 



#functions
#arguments
#bugs & debugging 
#return values and variables
#operators; = is the assignment operator 
#comments can be used as pseudocode; can use either the hash (#) or ("""") 
#parameters: inputs we can provide when using function; positional (first thing passed gets printed first etc), named (end, sep)
#scope: a variable only exists within the function it was created 




"""
this is a multi 
line
comment 
"""

#the best thing you can do is learn to read the documentation 

#single and double quotes are interchangeable 


#INT
#no decimal point in integers
#+ - * / % 

#interactive mode: typing in python in the terminal to then type code and it'll run instantly 
#ctrl + z then enter to get out of interactive mode


#FLOAT
#a number that has a decimal point in it
#no limit on how big an int can be but there's a limit to how precise a float can be because of the limits of computer memory



#round 
#documentation: round(number[, ndigits])


