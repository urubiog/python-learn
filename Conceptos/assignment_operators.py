# Now is the turn for assignment operators. Enjoy!

print("Assignment time!")

# In Python, assignment operators are used to assign values to variables.
# You can combine assignment with arithmetic, bitwise, or other operations.

# =   -> Assigns the value to the variable
# +=  -> Adds the right operand to the left operand and assigns the result
# -=  -> Subtracts the right operand from the left operand and assigns the result
# *=  -> Multiplies the left operand by the right operand and assigns the result
# /=  -> Divides the left operand by the right operand and assigns the result
# %=  -> Takes the modulus of the two operands and assigns the result
# **= -> Raises the left operand to the power of the right operand and assigns the result
# //= -> Performs integer division and assigns the result
# &=  -> Performs bitwise AND and assigns the result
# |=  -> Performs bitwise OR and assigns the result
# ^=  -> Performs bitwise XOR and assigns the result
# <<= -> Performs a left bitwise shift and assigns the result
# >>= -> Performs a right bitwise shift and assigns the result

# Examples:

# Basic Assignment
x = 10  # Assigns the value 10 to x

# Arithmetic Assignment
x += 5  # x = x + 5 -> 15
x -= 3  # x = x - 3 -> 12
x *= 2  # x = x * 2 -> 24
x /= 4  # x = x / 4 -> 6.0
x %= 5  # x = x % 5 -> 1.0

# Exponentiation and Integer Division Assignment
x **= 3  # x = x ** 3 -> 1.0
x //= 2  # x = x // 2 -> 0.0

# Bitwise Assignment
y = 5  # 0101 in binary
y &= 3  # y = y & 3 -> 0001 -> 1 in decimal
y |= 2  # y = y | 2 -> 0011 -> 3 in decimal
y ^= 1  # y = y ^ 1 -> 0010 -> 2 in decimal
y <<= 1  # y = y << 1 -> 0100 -> 4 in decimal
y >>= 2  # y = y >> 2 -> 0001 -> 1 in decimal

# [Exercise] What this will print?

z = 8
z <<= 2
z ^= 3
z += 5
z //= 4
print(z)  # out:
