# e = mc2 


def main():

    mass = int(input("m: "))
    formula(mass)


def formula(mass):
    c_squared = 300000000 ** 2
    energy = mass * c_squared
    print(f"e: {energy}")


main()
