# Now it's time for float methods in Python. Enjoy!

print("Float methods time!")

# Floats in Python come with several methods, mostly for dealing with complex numbers, hexadecimal conversion, and ratios.

# float.as_integer_ratio()
# Returns a tuple representing the float as a fraction (numerator, denominator).
# This method is useful when you want to express a float as a ratio.
my_float = 3.75
float_ratio = my_float.as_integer_ratio()
print(
    f"Float ratio of {my_float}: {float_ratio}"
)  # Output: Float ratio of 3.75: (15, 4)

# float.conjugate()
# Returns the conjugate of a complex number. If the float is not a complex number, it returns the float itself.
# Since floats are real numbers, it just returns the float value.
conjugate_of_float = my_float.conjugate()
print(
    f"Conjugate of {my_float}: {conjugate_of_float}"
)  # Output: Conjugate of 3.75: 3.75

# float.fromhex()
# Converts a hexadecimal string to a float.
hex_string = "0x1.8p2"  # This represents the float 6.0 in hexadecimal
float_from_hex = float.fromhex(hex_string)
print(
    f"Float from hex {hex_string}: {float_from_hex}"
)  # Output: Float from hex 0x1.8p2: 6.0

# float.hex()
# Converts a float to its hexadecimal string representation.
hex_representation = my_float.hex()
print(
    f"Hex representation of {my_float}: {hex_representation}"
)  # Output: Hex representation of 3.75: 0x1.8p1

# float.is_integer()
# Checks if the float is an integer. If it is, it returns True, otherwise False.
is_integer_check = my_float.is_integer()
print(
    f"Is {my_float} an integer?: {is_integer_check}"
)  # Output: Is 3.75 an integer?: False

# [Exercise] What will happen if the following code is executed?

my_float = 2.5
ratio_of_float = my_float.as_integer_ratio()
hex_of_float = my_float.hex()

print(f"Ratio of 2.5: {ratio_of_float}")
print(f"Hex of 2.5: {hex_of_float}")

# Answer:
# [ ] The ratio will be (5, 2) and the hex representation will be '0x1.4p1'.
# [ ] The ratio will be (5, 2) and the hex representation will be '0x1.8p1'.
