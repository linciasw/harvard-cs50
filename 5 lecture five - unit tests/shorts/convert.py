# FROM SHORT, PYTEST


def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue


    print(f"{au} AU is {convert(au)} m")




# type errors are when functions are given the wrong type


### 📝 Note: Type Validation with `isinstance()`
# This block utilizes Python's built-in **`isinstance(object, classinfo)`** function to handle type checking.
# *   **Why it's used:** It verifies if an object matches a specific type (e.g., `str`, `int`) or a tuple of multiple acceptable types (e.g., `(list, tuple)`).
# *   **Inheritance Safe:** Unlike `type()`, it evaluates to `True` even if the object is an instance of a **subclass** (child class) of the specified type.
# *   **Production Best Practice:** It keeps the code robust, flexible, and fully compatible with object-oriented inheritance principles.


def convert(au):
    # checks to see if au is an int or a float
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()