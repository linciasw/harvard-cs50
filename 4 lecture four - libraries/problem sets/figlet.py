"""
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, 
in which case the first of the two should be -f or --font, 
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, 
the program should exit via sys.exit with an error message.

"""

# find out why -f not working if i put in the command line
# documentation for figlet
# https://www.figlet.org/figlet-man.html


# documentation for sys
# https://docs.python.org/3/library/sys.html

from pyfiglet import Figlet, FontNotFound
import sys
import random

figlet = Figlet()


input = input("Input: ")


print(len(sys.argv))
print(sys.argv)


# if len(sys.argv) == 1:
#     figlet.setFont(font=str(random.choice(figlet.getFonts())))
#     print(figlet.renderText(input))
# elif len(sys.argv) == 2:
#     # font = sys.argv[2]
#     figlet.setFont(font=sys.argv[1])
#     print(figlet.renderText(input))
# elif "-f" or "-font" in sys.argv:


try:
    if len(sys.argv) == 1:
        figlet.setFont(font=str(random.choice(figlet.getFonts())))
        print(figlet.renderText(input))
    elif len(sys.argv) > 1 and "-f" in sys.argv or "--font" in sys.argv:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input))
except FontNotFound as error:
    print(f"Error: The font '{error}' could not be found.")
else:
    sys.exit


"""
# THINGS I LEARNT
- because sys.argv is a list, checking for the presense of a argument in the list 
is a much better idea than creating a conditional to check if an argument is at an index 
and then doing something
- you have to import the exception as well, if you're only importing one function from the module 
at first

"""
