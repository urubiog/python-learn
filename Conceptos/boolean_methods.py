# Now it's time for bool methods in Python. Enjoy!

print("Bool methods time!")

# Booleans in Python are a subclass of integers, and they have several methods derived from their integer nature.

# bool.as_integer_ratio()
# Returns the numerator and denominator as a tuple (1, 1) for True, and (0, 1) for False.
# Booleans are just integers, where True is 1 and False is 0.
my_bool_true = True
my_bool_false = False
true_ratio = my_bool_true.as_integer_ratio()
false_ratio = my_bool_false.as_integer_ratio()
print(f"True as integer ratio: {true_ratio}")  # Output: True as integer ratio: (1, 1)
print(
    f"False as integer ratio: {false_ratio}"
)  # Output: False as integer ratio: (0, 1)

# bool.bit_count()
# Returns the number of bits set to 1 in the integer representation.
# For True, it returns 1 because 1 has one bit set to 1. For False, it returns 0.
true_bit_count = my_bool_true.bit_count()
false_bit_count = my_bool_false.bit_count()
print(f"True bit count: {true_bit_count}")  # Output: True bit count: 1
print(f"False bit count: {false_bit_count}")  # Output: False bit count: 0

# bool.bit_length()
# Returns the number of bits necessary to represent the boolean in binary.
# For both True and False, it returns 1, as both are represented with a single bit.
true_bit_length = my_bool_true.bit_length()
false_bit_length = my_bool_false.bit_length()
print(f"True bit length: {true_bit_length}")  # Output: True bit length: 1
print(f"False bit length: {false_bit_length}")  # Output: False bit length: 1

# bool.conjugate()
# Returns the same value, True or False, as the complex conjugate of a boolean doesn't change.
true_conjugate = my_bool_true.conjugate()
false_conjugate = my_bool_false.conjugate()
print(f"True conjugate: {true_conjugate}")  # Output: True conjugate: True
print(f"False conjugate: {false_conjugate}")  # Output: False conjugate: False

# bool.is_integer()
# Returns False, as booleans are not considered integers.
is_integer_true = my_bool_true.is_integer()
is_integer_false = my_bool_false.is_integer()
print(f"Is True an integer? {is_integer_true}")  # Output: Is True an integer? False
print(f"Is False an integer? {is_integer_false}")  # Output: Is False an integer? False

# [Exercise] What will happen if the following code is executed?

my_bool_true = True
my_bool_false = False

true_ratio = my_bool_true.as_integer_ratio()
false_ratio = my_bool_false.as_integer_ratio()

print(f"True as integer ratio: {true_ratio}")
print(f"False as integer ratio: {false_ratio}")

# Answer:
# [ ] The ratio for True will be (1, 1) and for False will be (0, 1).
# [ ] The ratio for True will be (0, 1) and for False will be (1, 1).
