# FROM SHORTS
# DEBUGGING
# REACHED 5:54 IN VIDEO

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print(i, end = " ")
        print("#" * i)


if __name__ == "__main__":
    main()