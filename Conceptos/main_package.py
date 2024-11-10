# Importing the package to use its functions.

print("Time to use the package!")

from package import add, subtract, read_file, write_file

# Using the math functions
result_add = add(10, 5)  # 15
result_subtract = subtract(10, 5)  # 5

# Using the file handling functions
write_file("output.txt", "Hello, world!")  # Writes to the file
