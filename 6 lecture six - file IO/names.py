# FROM LECTURE
# REACHED 13:56



# file I/O within the context of programming, 
# is all about writing code than can read from or write to, files themselves


# in the below, everytime the names are printed,
# the information is lost
# names = []

# for i in range(3):
#     names.append(input("What's your name? "))


# for name in sorted(names):
#     print(f"hello, {name}")



# to save information to a file:
# keyword open
# the equivalent of double clicking on the gui
# documentation: https://docs.python.org/3/library/functions.html#open

name = input("What's your name? ")

# open just requires the name of the file we want to open and optionally,
# how we want to open it. 
# if file doesn't exist, it'll create it.
# open returns a file handle, a special file that allows you to access that file subsequently

# file = open("names.txt", "w")


file = open("names.txt", "a") 
# file.write(name) # this outputs harryronhermione 
file.write(f"{name}\n") # this outputs each name on a new line
file.close()


# running the above with "w" 3x, creates 3 new files with the new file overwriting the previous one
# "w" not only creates the file for you, it will recreate the file everytime you run the program 
# to get all names in, we'll need to append
# to do this, we change "w" or write to "a" or append
# output for "a":
# harryronhermione
# to get it all on new lines, we'll have to do it manually in the file.write(name) line



