"""
x = input("What's x? ") #user input will always be a string
y = input("What's y? ")

#this will print 12 because python is concatenating 2 strings 
#z = x + y


#type conversion 
z = int(x) + int(y)

print(z)
"""


#TYPE CONVERSION
#x = int(input("What's x? "))
#y = int(input("What's y? "))
#x = float(input("What's x? "))
#y = float(input("What's y? "))


#rounds the number up
#z = round(x + y)

#z = x / y

#rounds to a certain amount of digits; 
#documentation: round(number[, ndigits])
#z = round(x / y, 2)



#how to round to a certain amount of digits using f string 
#print(f"{z:.2f}")


#print(z)

#this will add a , to indicate a thousand
#print(f"{z:,}")

#print(x + y)



#return values
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n



main()