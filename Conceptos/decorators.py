# The time has arrived to delve into decorators, those elegant wrappers around functions that
# allow us to extend their behavior without modifying their internal code. With decorators,
# we gain the ability to write clean and expressive code that is as powerful as it is readable.

print("Time for decorators!")

# A decorator is a function that takes another function and extends its behavior
# without explicitly modifying it. It is often used for logging, access control, memoization, etc.

# A simple decorator that prints a message before and after the function is called


def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")


# Using the decorator
print("Using a simple decorator:")
say_hello()  # This will print "Before the function call", "Hello!", and "After the function call"


# Decorators with arguments: If the function you're decorating accepts arguments,
# you need to modify the wrapper function to accept them as well.


def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(
            f"Function {func.__name__} is being called with arguments: {args}, {kwargs}"
        )
        return func(*args, **kwargs)

    return wrapper


@decorator_with_args
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


# Using the decorator with arguments
print("\nUsing decorator with arguments:")
greet(
    "Alice", 30
)  # It will print the function's arguments, and then execute the function


# Returning values from decorated functions: Decorators can also modify the return value
# of the decorated function.


def return_value_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"Modified result: {result}"

    return wrapper


@return_value_decorator
def add(a, b):
    return a + b


# Using a decorator that modifies the return value
print("\nUsing a decorator that modifies the return value:")
print(add(5, 7))  # Will print the modified result


# Chaining decorators: You can apply multiple decorators to a single function.
# The decorators are applied in the order in which they are listed.


def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator one is applied")
        return func(*args, **kwargs)

    return wrapper


def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator two is applied")
        return func(*args, **kwargs)

    return wrapper


@decorator_one
@decorator_two
def display_message():
    print("Hello from the function!")


# Using multiple decorators
print("\nUsing multiple decorators:")
display_message()  # Will print "Decorator one is applied", "Decorator two is applied", and "Hello from the function!"


# Decorators with parameters: You can create decorators that accept parameters to customize their behavior.


def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_decorator(3)
def say_goodbye():
    print("Goodbye!")


# Using a decorator with parameters
print("\nUsing a decorator with parameters:")
say_goodbye()  # Will print "Goodbye!" three times


# Exercise:
# Create a decorator that logs the execution time of a function. Apply it to a function that performs
# a time-consuming task (such as sleeping for a few seconds), and print how long it took to execute.
