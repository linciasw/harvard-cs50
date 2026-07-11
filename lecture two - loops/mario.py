# when python runs this script, 
# it looks for code that is outside of a function to execute first.
# It goes all the way to the bottom and finds main()


# TO PRINT 3 HASHES LIKE SO: (VERTICAL)
#
#
#

# for _ in range(3):
#     print("#")



# what's nice about functions is that you can change the underlying 
# implementation details of them, but so long as you don't change the 
# name of the function or its parameters, or what it returns, no one
# else will know the difference


# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")


# what's nice about functions is that you can change the underlying 
# implementation details of them, but so long as you don't change the 
# name of the function or its parameters, or what it returns, no one
# else will know the difference

# for example, we can change the above to the below
# it does the same exact thing but different code
# def print_column(height):
#     print("#\n" * height, end="")



# TO PRINT 3 HASHES LIKE SO: (HORIZONTAL)
###


def main():
    print_square(3)
#     print_row(4)




# to print a grid, 3 x 3
# nested loop
"""
def print_square(size):

    # for each row in square 
    # this loop is responsible for tracking which row we are currently building.
    for i in range(size):

        # for each brick in row 
        for j in range(size):

            # print brick, take off new line
            print("#", end="")

        # this is to print a new line at the end of every row
        # when you call print with no arguments, you get a new line     
        print()
"""




# instead of a nested loop, we can write code like below:
# def print_square(size):
#     for i in range(size):
#          print("#" * size)
    


# instead of the above, we can write it decomposed as below:
def print_square(size):
    for i in range(size):
         print_row(size)


def print_row(width):
    print("#" * width)



# def print_row(width):
#     print("?" * width)


main()