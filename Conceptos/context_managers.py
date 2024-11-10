# Context Managers: Mastering resource management with the elegant "with" statement.

print("Understanding Context Managers in Python!")

# A context manager is a construct that allows for the allocation and release of resources,
# ensuring that resources are properly cleaned up after use. Context managers are often used
# when working with files, network connections, or database connections.

# Python provides a way to define context managers using:
# - The `with` statement.
# - The `__enter__` and `__exit__` methods for custom context managers.
# - The `contextlib` module for easier management.

# Let's first look at the built-in context manager for file handling.

print("Using built-in context manager for file handling:")

with open("sample.txt", "w") as file:
    file.write(
        "Hello, world!"
    )  # File will be automatically closed when the block ends.

# Here, the `open` function returns a context manager that manages the file resource.
# The file is automatically closed when the block exits, even if an error occurs inside the block.

# [Exercise] What will happen if the code inside the `with` block raises an exception?
# Hint: The file will still be closed because the context manager takes care of it.

# Creating a Custom Context Manager using `__enter__` and `__exit__`


class MyContextManager:
    def __enter__(self):
        # This is executed when the 'with' block starts.
        print("Entering the context...")
        return self  # The return value is bound to the variable after 'as'.

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This is executed when the 'with' block ends.
        print("Exiting the context...")
        if exc_type:
            print(f"Exception Type: {exc_type}")
            print(f"Exception Value: {exc_val}")
        # Returning True prevents the exception from propagating.
        return True  # Exception will be suppressed if True, or propagated if False.


# Using the custom context manager
print("\nUsing custom context manager:")

with MyContextManager() as cm:
    print("Inside the context.")
    # Uncomment the line below to test exception handling within the context manager
    # raise ValueError("An error occurred inside the context.")

# Here, `__enter__` is executed when the `with` block starts, and `__exit__` is executed when it ends.
# If an exception is raised inside the block, `__exit__` will handle it.

# The context manager ensures that the "Entering the context..." and "Exiting the context..." messages
# are printed regardless of whether an exception occurred, providing a clean resource management solution.

# [Exercise] Modify `MyContextManager` to log the execution time of the block.

# Using `contextlib` for Creating a Context Manager

from contextlib import contextmanager


@contextmanager
def simple_context_manager():
    print("Entering the context...")
    yield  # The code that follows will run inside the 'with' block.
    print("Exiting the context...")


# Using the contextlib-based context manager
print("\nUsing contextlib-based context manager:")

with simple_context_manager():
    print("Inside the context.")

# The `yield` in a function decorated with `@contextmanager` creates a context manager.
# Code before the `yield` runs when entering the context, and code after the `yield` runs when exiting.

# [Exercise] Modify `simple_context_manager` to manage database connections or open files.

# The context manager pattern is extremely powerful for managing resources like files, database connections, or network sockets.
# It ensures that resources are properly cleaned up even in the case of exceptions, providing a reliable way to manage resources.

# Summary of Key Points:
# - The `with` statement is used to manage resources.
# - Custom context managers implement the `__enter__` and `__exit__` methods.
# - The `contextlib` module allows for easier creation of context managers using the `@contextmanager` decorator.
# - The `__exit__` method can catch exceptions and prevent them from propagating.
# - Context managers are an excellent way to ensure that resources are properly cleaned up.

# [Exercise] Create a context manager that opens a file, writes a message, and ensures the file is always closed properly.
