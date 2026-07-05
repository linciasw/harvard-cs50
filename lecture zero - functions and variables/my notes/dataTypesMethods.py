"""
Python Primitive Data Types Cheat Sheet
(int, float, str)
"""

# =========================
# INT (Integers)
# =========================

x = 10

# Arithmetic operators
print(x + 5)   # addition
print(x - 5)   # subtraction
print(x * 5)   # multiplication
print(x / 5)   # division (float result)
print(x // 5)  # floor division
print(x % 5)   # modulus (remainder)
print(x ** 2)  # exponentiation

# Useful built-in functions with ints
print(abs(-10))     # absolute value
print(pow(2, 3))    # power
print(min(1, 2, 3))
print(max(1, 2, 3))

# Type conversion
print(int("10"))
print(int(3.7))     # truncates decimal


# =========================
# FLOAT (Decimals)
# =========================

y = 3.14

# Arithmetic (same as int)
print(y + 2)
print(y - 1)
print(y * 3)
print(y / 2)

# Rounding
print(round(3.14159, 2))

# Type conversion
print(float("3.14"))
print(float(10))

# Floating point precision note
print(0.1 + 0.2)  # not exactly 0.3


# =========================
# STRING (Text)
# =========================

text = "hello world"

# Case methods
print(text.lower())
print(text.upper())
print(text.title())

# Cleaning / replacing
print(text.strip())
print(text.replace("hello", "hi"))

# Splitting and joining
words = text.split()
print(words)

print(" ".join(["hi", "there"]))

# Searching
print(text.find("world"))
print(text.startswith("he"))
print(text.endswith("ld"))

# Checking content
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

# Length
print(len(text))


# =========================
# IMPORTANT TYPE BEHAVIOUR
# =========================

print(type(10))      # int
print(type(10.0))    # float
print(type("10"))    # str

# String vs numeric behavior
print("10" + "5")    # concatenation → "105"
print(10 + 5)        # math → 15