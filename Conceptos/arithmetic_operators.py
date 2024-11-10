# Now, you'll be learning about arithmetic operators in Python. Enjoy!

print("Math time!")

# In Python, you can use different arithmetic operators
# +  -> addition
# -  -> subtraction
# *  -> multiplication
# /  -> division
# %  -> modulus
# ** -> exponentiation
# // -> integer division

# There exist a priority order for operators, but with parenthesis can be modfied
# 1. ()
# 2. **
# 3. *, /, %, //
# 4. +, -

# Addition & Substraction
a = 5
b = 6
c = a + b  # 11
d = b - a  # 1

e = a + 5.5  # 16.5 -> int + float = float

# Multiplication & Division
g = a * b  # 30
g = (
    a / b
)  # 0.8333333333333334 -> There isn't a perfect precision, computers approximate decimal parts

# Modulus
# This operator is used to get the remainder of a division
h = 10 % 3  # 1 -> 10 divided by 3 leaves a remainder of 1

# Exponentiation
j = 2**3  # 8
r = 25**0.5  # 5 -> Same as the square root of 25

# Integer division
# The integer division is used to determine how many full sets of a certain size fit in a given total.
# It's often used when dividing a total into equal parts and you want to know how many complete parts you can have.

int_division = int(a / b)  # Is the same as doing this

k = 7 // 3  # 2 -> 7 divided by 3 gives 2, ignoring the decimal part.
m = 10 // 4  # 2 -> 10 divided by 4 gives 2, discarding the remainder

# [Exercise] What this will print?

print((3 + 5 * 2**3 - (6 / 2) ** 2 + 10 % 3) * (12 // 4 + 2) ** 2 - 8)

# out:
