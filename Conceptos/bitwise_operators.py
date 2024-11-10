# Now is the turn for bitwise operators. Enjoy!

print("Bitwise time!")

# In Python, bitwise operators allow you to manipulate individual bits of numbers.
# They work with integers and treat them as binary values.

# &  -> AND: sets each bit to 1 if both bits are 1
# |  -> OR: sets each bit to 1 if at least one of the bits is 1
# ^  -> XOR: sets each bit to 1 if the bits are different
# ~  -> NOT: inverts all the bits
# << -> Left shift: shifts bits to the left, filling with 0s
# >> -> Right shift: shifts bits to the right, discarding shifted bits

# Bitwise AND, OR, and XOR
a = 5  # 0101 in binary
b = 3  # 0011 in binary

result_and = a & b  # 0001 -> 1 in decimal
result_or = a | b  # 0111 -> 7 in decimal
result_xor = a ^ b  # 0110 -> 6 in decimal

# Bitwise NOT
c = 5  # 0101 in binary
result_not = (
    ~c
)  # -(5+1) -> -6 (inverts bits and adds 1 in two's complement representation)

# Bitwise Shifts
d = 5  # 0101 in binary
result_left_shift = d << 1  # 1010 -> 10 in decimal
result_right_shift = d >> 1  # 0010 -> 2 in decimal

# [Exercise] What this will print?

print((a & b) | ((~a ^ b) << 2))

# out:
