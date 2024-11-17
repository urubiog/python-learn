# Now, let's dive into Python functions—essential building blocks for clean and efficient code.

print("Functional time!")

"""
Built-in functions.
"""

# abs()  - Returns the absolute value of a number.
print(abs(-7))  # Output: 7


# delattr() - Deletes an attribute from an object.
class MyClass:
    x = 5


obj = MyClass()
delattr(obj, "x")  # Removes the attribute 'x' from obj

# hash() - Returns the hash value of an object.
print(hash("Hello"))  # Output: Hash value of "Hello"

# memoryview() - Creates a memory view object from a byte-like object.
byte_obj = bytes("Hello", "utf-8")
mv = memoryview(byte_obj)
print(mv[0])  # Output: 72 (ASCII value of 'H')

# all() - Returns True if all elements in an iterable are True.
print(all([True, True, False]))  # Output: False

# help() - Invokes the built-in help system.
help(print)  # Displays help for the print function

# min() - Returns the smallest element from an iterable or the smallest of two or more arguments.
print(min(4, 7, 1, 8))  # Output: 1

# setattr() - Sets an attribute of an object.
setattr(obj, "y", 10)  # Sets 'y' as an attribute of obj

# any() - Returns True if any element of an iterable is True.
print(any([False, False, True]))  # Output: True

# dir() - Returns a list of the attributes and methods of an object.
print(dir(obj))  # Output: List of attributes and methods of obj

# hex() - Converts an integer to a hexadecimal string.
print(hex(255))  # Output: '0xff'

# next() - Returns the next item from an iterator.
numbers = iter([1, 2, 3])
print(next(numbers))  # Output: 1

# slice() - Returns a slice object used to slice sequences.
s = slice(2, 5)
print("Hello"[s])  # Output: 'llo'

# ascii() - Returns a printable representation of an object.
print(ascii("café"))  # Output: "'caf\\xe9'"

# divmod() - Returns the quotient and remainder of a division.
print(divmod(8, 3))  # Output: (2, 2)

# id() - Returns the identity (unique identifier) of an object.
print(id(obj))  # Output: The unique ID of obj

# sorted() - Returns a sorted list of an iterable.
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# bin() - Converts an integer to a binary string.
print(bin(5))  # Output: '0b101'

# enumerate() - Returns an enumerate object (index and value) from an iterable.
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)  # Output: 0 a, 1 b, 2 c

# input() - Reads a line from input.
user_input = input("Enter your name: ")
print(f"Hello, {user_input}")

# oct() - Converts an integer to an octal string.
print(oct(8))  # Output: '0o10'


# staticmethod() - Converts a method to a static method.
class MyClass:
    @staticmethod
    def greet():
        print("Hello!")


MyClass.greet()  # Output: "Hello!"

# bool() - Converts a value to a boolean.
print(bool(0))  # Output: False

# eval() - Evaluates a string as Python code.
print(eval("3 + 5"))  # Output: 8

# int() - Converts a value to an integer.
print(int("42"))  # Output: 42

# open() - Opens a file.
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()

# str() - Converts a value to a string.
print(str(100))  # Output: '100'

# breakpoint() - Invokes the debugger.
breakpoint()  # Will stop the code execution here for debugging

# exec() - Executes dynamically provided Python code.
exec('print("Executed!")')  # Output: Executed!

# isinstance() - Checks if an object is an instance of a class.
print(isinstance(5, int))  # Output: True

# ord() - Returns the ASCII value of a character.
print(ord("A"))  # Output: 65

# sum() - Returns the sum of an iterable.
print(sum([1, 2, 3]))  # Output: 6

# filter() - Filters elements of an iterable using a function.
numbers = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, numbers)))  # Output: [2, 4]

# issubclass() - Checks if a class is a subclass of another.
print(issubclass(bool, int))  # Output: True

# pow() - Returns the result of raising a number to a power.
print(pow(2, 3))  # Output: 8


# super() - Returns a proxy object that delegates method calls to the parent class.
class Animal:
    def speak(self):
        print("Animal speaking...")


class Dog(Animal):
    def speak(self):
        super().speak()  # Call parent class method
        print("Dog barking!")


dog = Dog()
dog.speak()  # Output: Animal speaking... Dog barking!

# bytes() - Creates a bytes object.
print(bytes("Hello", "utf-8"))  # Output: b'Hello'

# iter() - Returns an iterator for an object.
numbers = [1, 2, 3]
numbers_iter = iter(numbers)
print(next(numbers_iter))  # Output: 1

# print() - Prints objects to the standard output.
print("Hello, World!")  # Output: Hello, World!

# callable() - Checks if an object is callable (i.e., a function or method).
print(callable(print))  # Output: True

# format() - Formats a string with placeholders.
print("The value of x is: {}".format(10))  # Output: The value of x is: 10

# len() - Returns the length of an object.
print(len("Hello"))  # Output: 5


# property() - Creates a property for a class.
class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


obj = MyClass(10)
print(obj.value)  # Output: 10

# type() - Returns the type of an object.
print(type(5))  # Output: <class 'int'>

# chr() - Returns a character from an ASCII value.
print(chr(65))  # Output: 'A'

# vars() - Returns the __dict__ of an object.
print(vars(obj))  # Output: {'_value': 10}


# classmethod() - Converts a method to a class method.
class MyClass:
    @classmethod
    def greet(cls):
        print("Greetings from the class!")


MyClass.greet()  # Output: Greetings from the class!

# getattr() - Gets an attribute of an object.
print(getattr(obj, "value"))  # Output: 10

# locals() - Returns a dictionary of local variables.
print(locals())

# repr() - Returns a string representation of an object.
print(repr(obj))  # Output: <__main__.MyClass object at 0x7f5fc1c0f430>

# zip() - Combines multiple iterables into tuples.
pairs = zip([1, 2, 3], ["a", "b", "c"])
print(list(pairs))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# compile() - Compiles a string of code into a code object.
code = compile("x = 10\nprint(x)", "<string>", "exec")
exec(code)  # Output: 10

# globals() - Returns a dictionary of global variables.
print(globals())

# map() - Applies a function to all items in an iterable.
print(list(map(lambda x: x**2, [1, 2, 3])))  # Output: [1, 4, 9]

# reversed() - Returns a reversed iterator.
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# __import__() - Dynamically imports a module.
math = __import__("math")
print(math.sqrt(16))  # Output: 4.0

# hasattr() - Checks if an object has an attribute.
print(hasattr(obj, "value"))  # Output: True

# max() - Returns the largest element from an iterable or the largest of two or more arguments.
print(max(1, 2, 3))  # Output: 3

# round() - Rounds a number to the nearest integer.
print(round(5.6))  # Output: 6

"""
Function declaration & invocation.
"""


# A simple function
def greet(name):
    print(f"Hello, {name}!")


# Invoking the function
greet("John")  # Output: Hello, John!


# Function with return value
def add(x, y):
    return x + y


# Invoking the function
result = add(3, 4)
print(result)  # Output: 7


# Function with default argument
def multiply(x, y=2):
    return x * y


print(multiply(5))  # Output: 10 (uses default y=2)
print(multiply(5, 3))  # Output: 15 (uses y=3)


# Function with conditional logic
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"


print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd


# A recursive function is one that calls itself in order to solve a problem.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # Output: 120 (5 * 4 * 3 * 2 * 1)

"""
Lambda functions.
"""

# A lambda function to add two numbers
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # Output: 8

# Using lambda with map()
numbers = [1, 2, 3]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9]

# [Exercise] Create a recursive function to compute the n-th fibonacci's series number


def fibo(n):
    ...


print(fibo(30))  # 832040
