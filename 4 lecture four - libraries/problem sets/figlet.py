# find out why -f not working if i put in the command line
# documentation for figlet
# https://www.figlet.org/figlet-man.html


# documentation for sys
# https://docs.python.org/3/library/sys.html

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
    figlet.setFont(font=sys.argv[1])
    print(figlet.renderText(input))
elif len(sys.argv) == 3 and sys.argv[1] != "-f" or sys.argv[1] != "-font":
    sys.exit


# else:
#     sys.exit


print(len(sys.argv))
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])









