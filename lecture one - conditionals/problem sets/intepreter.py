expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == ("+"):
    a = int(x) + int(z)
    print(float(a))
elif y == ("-"):
    a = int(x) - int(z)
    print(float(a))
elif y == ("*"):
    a = int(x) * int(z)
    print(float(a))
else:
    a = int(x) / int(z)
    print(float(a))





# +
# -
# *
# /