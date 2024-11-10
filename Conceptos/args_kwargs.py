# The time has come to explore *args and **kwargs, two powerful tools that allow us to
# pass a variable number of arguments to functions with a clarity and versatility that is
# unmatched in Python. Let us learn how to handle arbitrary argument lists with grace.

print("Time for *args and **kwargs!")


# *args: Allows a function to accept a variable number of positional arguments.
# The *args parameter collects arguments into a tuple.
def print_numbers(*args):
    for number in args:
        print(number)


print("Using *args to pass a variable number of arguments:")
print_numbers(1, 2, 3)  # Passing three arguments
print_numbers(10, 20, 30, 40, 50)  # Passing five arguments


# **kwargs: Allows a function to accept a variable number of keyword arguments.
# The **kwargs parameter collects arguments into a dictionary, where the keys are the argument names.
def print_names(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\nUsing **kwargs to pass a variable number of keyword arguments:")
print_names(name="John", age=25, city="New York")  # Passing three keyword arguments
print_names(
    first_name="Alice", last_name="Smith", occupation="Engineer"
)  # Passing three keyword arguments

# Combining *args and **kwargs in the same function
# *args must appear before **kwargs when they are both used in a function definition.


def combined_example(arg1, *args, kwarg1=None, **kwargs):
    print(f"Positional argument: {arg1}")
    print(f"*args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"**kwargs: {kwargs}")


print("\nUsing both *args and **kwargs together:")
combined_example(1, 2, 3, 4, kwarg1="some_value", key1="value1", key2="value2")


# **kwargs with default values
# You can also provide default values for keyword arguments that may not be passed.
def greet(name, **kwargs):
    greeting = kwargs.get("greeting", "Hello")  # Default greeting is "Hello"
    print(f"{greeting}, {name}!")


print("\nUsing **kwargs with default values:")
greet("Alice")  # Uses default greeting
greet("Bob", greeting="Good morning")  # Uses custom greeting


# *args and **kwargs with arbitrary numbers of arguments in a method
# Let's say we have a method that can take any number of numbers and return their sum.
def sum_all_numbers(*args):
    return sum(args)


print("\nUsing *args to sum numbers:")
print(sum_all_numbers(1, 2, 3, 4))  # Sum of four numbers
print(sum_all_numbers(10, 20, 30))  # Sum of three numbers

# Exercise:
# Write a function `describe_person` that accepts a name as a positional argument,
# an arbitrary number of hobbies via *args, and an arbitrary number of personal details
# (like age, city, etc.) via **kwargs. Print all the information in a formatted way.
