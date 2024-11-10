# In this module, we explore the art of creating custom exceptions and employing assertions,
# two powerful techniques that allow us to handle errors and validate assumptions with elegance.
# All custom exceptions must derive from the BaseException class, the root of the exception hierarchy.

print("Time to master custom exceptions and assertions!")

# Custom exceptions: By creating your own exceptions, you can provide more specific,
# meaningful error messages that are tailored to the specific needs of your application.
# All custom exceptions must inherit from BaseException or one of its subclasses.


class MyCustomError(
    BaseException
):  # All exceptions must derivate from the class BaseException
    """A custom exception for specific errors in our program."""

    pass


# Raising a custom exception
def raise_my_error():
    raise MyCustomError("Something went wrong with my custom exception!")


# Using the custom exception
print("Using a custom exception:")
try:
    raise_my_error()  # This will raise the custom exception
except MyCustomError as e:
    print(f"Custom Exception caught: {e}")

# Custom exception with arguments: You can also pass custom information to your exception,
# making it even more informative.
# Remember, your custom exception must still inherit from BaseException or its subclasses.


class InvalidInputError(BaseException):
    """Exception raised for invalid input."""

    def __init__(self, message, value):
        self.message = message
        self.value = value
        super().__init__(self.message)


# Raising a custom exception with arguments
def process_input(input_value):
    if input_value < 0:
        raise InvalidInputError("Input must be non-negative", input_value)


# Using the custom exception with arguments
print("\nUsing custom exception with arguments:")
try:
    process_input(-5)  # This will raise the custom exception
except InvalidInputError as e:
    print(f"Error: {e} - Invalid value: {e.value}")


# Assertions: Assertions are used to check if certain conditions hold true during execution.
# If the condition is False, an AssertionError is raised.

print("\nUsing assertions:")

# Basic assertion: This checks if the condition is true, and raises an AssertionError if it's not.
assert 2 + 2 == 4  # This will pass silently

# This will raise an AssertionError because the condition is false
try:
    assert 2 + 2 == 5, "Mathematical error: 2 + 2 should equal 4!"
except AssertionError as e:
    print(f"AssertionError: {e}")


# Assert with more complex conditions
def calculate_average(numbers):
    assert len(numbers) > 0, "The list of numbers cannot be empty!"
    return sum(numbers) / len(numbers)


# Using assertion with function
print("\nUsing assertion in a function:")
try:
    avg = calculate_average([])  # This will raise an AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")


# Custom assertion: You can also create your own assertion-like functions
def assert_positive(number):
    if number <= 0:
        raise AssertionError(f"Value must be positive, but got {number}.")


# Using a custom assertion-like function
print("\nUsing a custom assertion:")
try:
    assert_positive(-10)  # This will raise an AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")


# Exercise:
# Create a custom exception for handling negative numbers. Then, write a function that checks if a number is negative.
# If it is, raise your custom exception with an appropriate message.
