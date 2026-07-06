"""print("meow")
print("meow")
print("meow")"""


# WHILE
# you can count down 
# i = 3
# while i != 0:
#     print("Meow")
#     i = i -1 


# you can count up 
# i = 1
# while i <= 3:
#     print("meow") 
#     i = i + 1


# indexing starts at zero 
# i = 0
# while i < 3:
#     print("meow") 
#     i = i + 1


# another way of saying i = i + 1
# i = 0
# while i < 3:
#     print("meow") 
#     i += 1


# FOR LOOP AND LISTS
# square brackets represent lists, it's a data type
# for i in [0, 1, 2]: 
#     print("meow")


# NOTE:
# to decide if code is good, think of extreme cases 
# like what if you want to get a million?


# to simplify, you can use a function 
# range goes up to but not pass the number you specify 
# range helps because you can put in any amount you want 
# for i in range(3): 
#     print("meow") 


# there's a convention in python where if you need a variable just
# because the programming feature requires it to do some kind of 
# counting or automatic updating and you don't really care about its value,
# a pythonic improvement would be to name the variable a single underscore
# it signals to anyone looking at your code that yes, it's a variable
# but you don't care about its name, you're just using it for this particular
# feature 
# for _ in range(3): 
#     print("meow") 


# you can use this to do the same as the loops
# the output is meowmeowmeow however
# print("meow" * 3)


# to fix it, use escape character and put the last print to end with nothing 
print("meow\n" * 3, end="")





