# The Complex Class in Python: Complex numbers consist of a real and an imaginary part.
# Python's built-in `complex` class provides a way to work with these numbers and perform mathematical operations.

print("Mastering the Complex Class in Python!")

# Creating complex numbers
# You can create a complex number using the built-in `complex()` function or by directly using the 'j' notation.

# Using the complex() function
z1 = complex(2, 3)  # Creates a complex number 2 + 3j
print(f"z1: {z1}")

# Using the 'j' notation
z2 = 4 + 5j  # Creates a complex number 4 + 5j
print(f"z2: {z2}")

# Accessing the real and imaginary parts of a complex number
print(f"Real part of z1: {z1.real}")
print(f"Imaginary part of z1: {z1.imag}")

# The real and imaginary attributes are used to access the real and imaginary components of a complex number.

# Complex Number Operations

# Addition of complex numbers
z3 = z1 + z2
print(f"z1 + z2 = {z3}")

# Subtraction of complex numbers
z4 = z1 - z2
print(f"z1 - z2 = {z4}")

# Multiplication of complex numbers
z5 = z1 * z2
print(f"z1 * z2 = {z5}")

# Division of complex numbers
z6 = z1 / z2
print(f"z1 / z2 = {z6}")

# Conjugate of a complex number
z7 = z1.conjugate()
print(f"Conjugate of z1: {z7}")

# Complex number magnitude (absolute value)
z8 = abs(z1)
print(f"Absolute value of z1: {z8}")

# Real and Imaginary Operations
z9 = 3 + 4j
print(f"Real part of z9: {z9.real}")
print(f"Imaginary part of z9: {z9.imag}")

# Special Methods for Complex Numbers

# __abs__: Returns the magnitude of the complex number (distance from the origin in the complex plane)
print(f"__abs__ of z2: {abs(z2)}")  # Same as using abs(z2)

# __add__: Allows the use of the + operator for complex numbers
z10 = z1 + z2
print(f"__add__ z1 + z2 = {z10}")

# __sub__: Allows the use of the - operator for complex numbers
z11 = z1 - z2
print(f"__sub__ z1 - z2 = {z11}")

# __mul__: Allows the use of the * operator for complex numbers
z12 = z1 * z2
print(f"__mul__ z1 * z2 = {z12}")

# __truediv__: Allows the use of the / operator for complex numbers
z13 = z1 / z2
print(f"__truediv__ z1 / z2 = {z13}")

# __repr__: Provides a string representation of a complex number for debugging
print(f"__repr__ of z1: {repr(z1)}")

# __str__: Provides a user-friendly string representation of the complex number
print(f"__str__ of z1: {str(z1)}")

# __eq__: Checks if two complex numbers are equal
z14 = 2 + 3j
print(f"__eq__ z1 == z14: {z1 == z14}")

# __neg__: Negates the complex number
z15 = -z1
print(f"__neg__ of z1: {z15}")

# __pos__: Returns the positive version of the complex number (essentially unchanged)
z16 = +z1
print(f"__pos__ of z1: {z16}")

# __abs__ provides the magnitude (also accessible via the abs() function):
z18 = abs(3 + 4j)  # magnitude is 5
print(f"__abs__ result: {z18}")

# [Exercise]
# Create two complex numbers, perform all possible operations (+, -, *, /) between them, and print the results.
# Experiment with the __abs__, __add__, __sub__, __mul__, __truediv__, __eq__ methods.
