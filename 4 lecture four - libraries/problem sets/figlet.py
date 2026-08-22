# find out why -f not working if i put in the command line

from pyfiglet import Figlet
import sys
import random 


figlet = Figlet()


input = input("Input: ")




if len(sys.argv) == 1:
    figlet.setFont(font=str(random.choice(figlet.getFonts())))
    print(figlet.renderText(input))
elif len(sys.argv) == 2:
    # font = sys.argv[2]
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input))





