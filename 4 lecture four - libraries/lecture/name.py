# FROM LECTURE
# FROM 19:13

# command-line arguments
# the sys module 


import sys

# print("hello, my name is", sys.argv[1])
# input in the interpreter: python name.py Lincia
# output would be "hello, my name is Lincia"

# sys.argv[1] pulls the name i put on the intepreter line 
# because the name of the file is stored at index 0


print(sys.argv)
# input in the interpreter: python name.py Lincia
# output is ['name.py', 'Lincia']


# the below can give an indexError as that's one of the 
# most common errors whenever you're dealing with a list,
# dict, tuple etc
# to prevent this, we can use a try-except block 
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")




# we can also write an if-elif-else block to get around this
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

