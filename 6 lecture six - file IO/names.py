# FROM LECTURE
# REACHED 20:14
# READ DOCUMENTATION ON FILE I/O



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

# name = input("What's your name? ")

# file = open("names.txt", "w")
# file.write(f"{name}\n") 
# file.close()



# open just requires the name of the file we want to open and optionally,
# how we want to open it. 
# if file doesn't exist, it'll create it.
# open returns a file handle, a special file that allows you to access that file subsequently


# creates 3 new files with the new file overwriting the previous one
# file = open("names.txt", "w")



# to get all names in, we'll need to append
# to do this, we change "w" or write to "a" or append.
# this outputs harryronhermione though
# file = open("names.txt", "a") 


# this just writes the input to the file
# file.write(name) 

# this outputs each name on a new line
# file.write(f"{name}\n") 

# file.close()


# running the above with "w" 3x, creates 3 new files with the new file overwriting the previous one
# "w" not only creates the file for you, it will recreate the file everytime you run the program 
# to get all names in, we'll need to append
# to do this, we change "w" or write to "a" or append
# output for "a":
# harryronhermione
# to get it all on new lines, we'll have to do it manually in the file.write(name) line


# with
# sometimes we forget to close files using the .close() function
# with tells python to open and close file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n") 

# if there's no more code after the with block, python will automatically close the file for you 





# PROGRAM TO OPEN FILE
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line) 
    # the output here is:
    # hello, Hermione

    # hello, Harry

    # the names in the file has a new line at the end (see code above) and print adds in 
    # a new line so it's printing 2 new lines


    # we add an .rstrip() function to strip the new line space at the right of the line in the file
    # to allow print() to add its new line 
# for line in lines:
#     print("hello,", line.rstrip())


# we can shorten everything above by doing:
with open("nJames.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())








