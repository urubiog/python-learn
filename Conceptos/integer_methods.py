# Now it's time for integer methods in Python. Enjoy!

print("Integer methods time!")

# Integers in Python come with several methods, mostly for dealing with rational numbers, complex numbers, and byte representations.

# int.as_integer_ratio()
# Returns a tuple representing the integer as a fraction (numerator, denominator).
# For example, it can represent 3/4 as (3, 4).
my_integer = 3
integer_ratio = my_integer.as_integer_ratio()
print(
    f"Integer ratio of {my_integer}: {integer_ratio}"
)  # Output: Integer ratio of 3: (3, 1)

# int.bit_count()
# Returns the number of bits set to 1 in the binary representation of the integer.
my_integer = 29  # binary representation of 29 is 11101
bit_count = my_integer.bit_count()
print(f"Bit count of {my_integer}: {bit_count}")  # Output: Bit count of 29: 4

# int.bit_length()
# Returns the number of bits required to represent the integer in binary (excluding sign and leading zeros).
bit_length = my_integer.bit_length()
print(f"Bit length of {my_integer}: {bit_length}")  # Output: Bit length of 29: 5

# int.conjugate()
# Returns the conjugate of a complex number. If the integer is not a complex number, it returns the integer itself.
# Since integers are real numbers, it just returns the integer.
conjugate_of_integer = my_integer.conjugate()
print(
    f"Conjugate of {my_integer}: {conjugate_of_integer}"
)  # Output: Conjugate of 29: 29

# int.from_bytes()
# Interprets a byte sequence as an integer. Useful when working with byte data.
byte_sequence = b"\x00\x00\x00\x1d"  # Represents 29 in bytes
integer_from_bytes = int.from_bytes(byte_sequence, "big")
print(
    f"Integer from bytes {byte_sequence}: {integer_from_bytes}"
)  # Output: Integer from bytes b'\x00\x00\x00\x1d': 29

# int.is_integer()
# Checks if the number is an integer. For integers, this will always return True.
is_integer_check = my_integer.is_integer()
print(
    f"Is {my_integer} an integer?: {is_integer_check}"
)  # Output: Is 29 an integer?: True

# int.to_bytes()
# Returns the byte representation of the integer.
byte_representation = my_integer.to_bytes(4, "big")
print(
    f"Byte representation of {my_integer}: {byte_representation}"
)  # Output: Byte representation of 29: b'\x00\x00\x00\x1d'

# [Exercise] What will happen if the following code is executed?

my_integer = 45
ratio_of_integer = my_integer.as_integer_ratio()
bit_count_of_integer = my_integer.bit_count()

print(f"Ratio of 45: {ratio_of_integer}")
print(f"Bit count of 45: {bit_count_of_integer}")

# Answer:
# [ ] The ratio will be (45, 1) and the bit count will be 5.
# [ ] The ratio will be (45, 1) and the bit count will be 6.
