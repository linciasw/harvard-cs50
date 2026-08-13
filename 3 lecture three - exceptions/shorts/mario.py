# FROM SHORTS
# DEBUGGING
# REACHED 5:54 IN VIDEO


'''
print() is a nice tool for debugging.
it's a nice way to see what's inside your code.
'''


def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

        '''
        this is a debugging print() statement
        print(i, end = " ")  
        print("#" * i)
        
        the output of this is:
        Height: 4
        0
        1 #
        2 ##
        3 ###

        the first line with 0 is not wanted. 
        it happens because the first index is zero.
        '''


        # this should fix the problem and print the hashes without the first space for 0
        # print("#" * (i + 1))

        '''
        print becomes annoying becase you'll have print statements everywhere
        and you'll forget which print belongs where etc
        IDEs come with built-in debuggers.
        '''

        # breakpoints
        '''
        breakpoints are a little better.
        a breakpoint is simply a mechanism when using a text editor or an IDE
        that allows you to specify on what line or lines of code you want to pause
        or break execution of the program just so you can start poking around at
        that line of code
        '''


        print("#" * (i + 1))


if __name__ == "__main__":
    main()