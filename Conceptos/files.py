# In this module, we delve into the world of file handling in Python.
# We will explore how to read from, write to, and manage files efficiently.
# Let's take control of files with elegance and precision.

print("It's time for file handling!")

# Opening a file: The open() function is used to open a file. It returns a file object.
# You can specify the mode in which you want to open the file (e.g., read, write, append).

# Opening a file for reading (default mode is 'r')
try:
    file = open("example.txt", "r")  # Reading mode
    content = file.read()
    print("File content read successfully:")
    print(content)
finally:
    file.close()  # Always close the file to release resources

# Writing to a file: Opening a file in write mode ('w') allows you to write data to the file.
# If the file doesn't exist, it is created. If it exists, it is overwritten.

try:
    file = open("example.txt", "w")  # Write mode (overwrites existing content)
    file.write("This is a new line of text written into the file.\n")
    print("Text written to the file successfully!")
finally:
    file.close()  # Always close the file after writing

# Appending to a file: You can open a file in append mode ('a') to add content without overwriting the existing content.

try:
    file = open("example.txt", "a")  # Append mode
    file.write("This is an additional line appended to the file.\n")
    print("Text appended to the file successfully!")
finally:
    file.close()  # Always close the file

# Using 'with' for file handling: The 'with' statement is used to wrap the file handling, ensuring that the file
# is automatically closed after the block of code is executed.

print("\nUsing 'with' to handle files:")

with open("example.txt", "r") as file:
    content = file.read()  # Reading the file content
    print("Content read using 'with':")
    print(content)

# Reading lines from a file: You can read the file line by line using the readlines() method.
with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns a list of lines in the file
    print("\nLines in the file:")
    for line in lines:
        print(line.strip())  # Using strip() to remove newline characters

# Checking if a file exists: You can use the os module to check if a file exists before attempting to open it.

import os

file_path = "example.txt"
if os.path.exists(file_path):
    print(f"\nThe file {file_path} exists.")
else:
    print(f"\nThe file {file_path} does not exist.")

# Reading binary files: To handle binary files (such as images), use 'rb' mode to read the file in binary format.

try:
    with open("example_binary.dat", "rb") as file:
        binary_content = file.read()  # Read binary data
        print("\nBinary content read successfully!")
except FileNotFoundError:
    print("\nThe binary file does not exist.")

# Writing binary files: Similarly, you can open a file in binary write mode ('wb') to write binary data.

try:
    with open("example_binary.dat", "wb") as file:
        data = bytes(
            [65, 66, 67, 68]
        )  # Example of binary data (ASCII codes for 'ABCD')
        file.write(data)  # Write binary data to the file
        print("\nBinary data written to the file successfully!")
except Exception as e:
    print(f"\nError writing binary data: {e}")

# Exercise:
# Create a text file named 'user_data.txt'. Write user-provided information (like name and age) into the file.
# Then, read the file and display its content.
