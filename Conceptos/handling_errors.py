# The time has come to master exception handling, where we balance the graceful handling of errors with the calm assurance of control.

print("Exception Handling time!")

# BaseError class is the base class for all exceptions
# - All built-in exceptions inherit from BaseException.

BaseException  # The base class for all exceptions (very rarely used directly)
Exception  # The base class for all non-exit exceptions
SyntaxError  # Raised when there is a syntax error in the code
IndentationError  # A subclass of SyntaxError raised for incorrect indentation
TypeError  # Raised when an operation or function is applied to an object of inappropriate type
ValueError  # Raised when a function receives an argument of the correct type but inappropriate value
KeyError  # Raised when a dictionary key is not found
IndexError  # Raised when a sequence subscript is out of range
AttributeError  # Raised when an attribute reference or assignment fails
NameError  # Raised when a local or global name is not found
FileNotFoundError  # Raised when a file or directory is requested but cannot be found
OSError  # Raised for system-related errors, including file input/output errors
IOError  # A subclass of OSError, specifically for I/O operation errors (file handling)
ZeroDivisionError  # Raised when a division or modulo operation is performed with zero
MemoryError  # Raised when an operation runs out of memory
OverflowError  # Raised when the result of an arithmetic operation is too large to be expressed
ImportError  # Raised when an import statement fails
ModuleNotFoundError  # Raised when a module cannot be found
RuntimeError  # Raised when a general error occurs in the execution of a program
RecursionError  # Raised when the maximum recursion depth is exceeded
StopIteration  # Raised when the next() function exceeds the end of an iterator
AssertionError  # Raised when an assert statement fails
NotImplementedError  # Raised when an abstract method needs to be implemented in a subclass
PermissionError  # Raised when an operation is not allowed due to permission restrictions
TimeoutError  # Raised when a time limit is exceeded for a specific operation
BlockingIOError  # Raised for blocking I/O operations in non-blocking mode
FileExistsError  # Raised when trying to create a file or directory that already exists
InterruptedError  # Raised when a system call is interrupted by a signal
IsADirectoryError  # Raised when a file operation is performed on a directory
NotADirectoryError  # Raised when a directory operation is performed on a file
ValueError  # Raised when a function gets an argument of the correct type, but an inappropriate value
UnicodeError  # Raised for errors related to Unicode encoding/decoding
UnicodeEncodeError  # Raised when a Unicode-related error occurs during encoding
UnicodeDecodeError  # Raised when a Unicode-related error occurs during decoding
UnicodeTranslateError  # Raised when a Unicode-related error occurs during translation
SystemError  # Raised when the interpreter finds an internal error
ReferenceError  # Raised when a weak reference proxy is accessed after the referent has been garbage-collected
EnvironmentError  # A superclass for IOError, OSError, and FileNotFoundError (deprecated)

# The try block is used to write the code that might throw an exception.
# The except block catches and handles the exception.
# The finally block will execute regardless of whether an exception occurred or not.
# The else block runs if no exceptions were thrown.

# Basic try-except
try:
    # Attempt to divide by zero (will throw an exception)
    result = 10 / 0
except ZeroDivisionError:
    # Handle the division by zero exception
    print("Can't divide by zero!")

# Try with multiple except blocks
try:
    number = int("Hello")  # This will raise a ValueError
except ValueError:
    print("ValueError: Invalid integer conversion!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Using finally: It always runs, regardless of whether an exception was raised
try:
    print("Opening file...")
    file = open("example.txt", "r")
    # Some code that may throw an exception
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    # This block will always run, closing the file whether an error occurs or not
    print("Closing file...")
    try:
        file.close()
    except NameError:
        pass  # This prevents error if file was never opened

# else: Runs if no exceptions were raised
try:
    num = 5
    result = num * 10
except Exception:
    print("An error occurred.")
else:
    print(
        f"The operation was successful. The result is {result}"
    )  # This runs because no exception was raised


# Custom exception handling using raise
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")  # Raising an exception
    print(f"Your age is {age}")


try:
    check_age(-5)  # This will raise a ValueError
except ValueError as ve:
    print(f"Error: {ve}")  # Handle the exception

# [Exercise] What will happen if the following code is executed?

try:
    x = (
        "hello" + 5
    )  # This will raise a TypeError because we cannot add a string and an integer
except TypeError:
    print("TypeError caught!")
else:
    print("No errors occurred.")
finally:
    print("The try-except-finally block has completed.")

# Answer:
# [ ] It will print "TypeError caught!"
# [ ] It will print "No errors occurred."
# [ ] It will print "The try-except-finally block has completed."
