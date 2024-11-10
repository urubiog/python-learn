# Now, we explore the scope of variables in Python—a key concept for understanding
# how variables are accessed and modified across different levels of nested functions.
# This module will delve into the LEGB principle, closures, and the use of the global
# and nonlocal keywords to manipulate variable scope.

print("pointing to variables...")

# The LEGB principle refers to the order in which Python searches for variables:
# L -> Local scope: Variables inside the current function.
# E -> Enclosing scope: Variables in any enclosing (non-global) function.
# G -> Global scope: Variables at the level of the module.
# B -> Built-in scope: Python's built-in functions and objects.


# Local scope
def local_scope_example():
    x = 10  # Local variable
    print("Local scope:", x)


local_scope_example()


# Enclosing scope
def enclosing_scope_example():
    x = 20  # Enclosing variable

    def inner_function():
        print(
            "Enclosing scope:", x
        )  # This accesses the variable from the enclosing scope

    inner_function()


enclosing_scope_example()

# Global scope
x = 30  # Global variable


def global_scope_example():
    print("Global scope:", x)  # Accessing the global variable


global_scope_example()

# Built-in scope
print("Built-in scope:", abs(-10))  # The abs() function is part of the built-in scope


# Closure example
# A closure occurs when a nested function references a variable from the enclosing scope
def closure_example():
    x = 40  # Enclosing variable

    def inner_function():
        print("Closure scope:", x)  # Accessing the variable from the enclosing scope

    return inner_function


closure_func = closure_example()
closure_func()  # Calling the closure function, which remembers the enclosing scope


# The 'global' keyword
# We use 'global' to modify a global variable from within a function
def modify_global():
    global x
    x = 50  # Modifies the global variable
    print("Modified global variable:", x)


modify_global()  # Will modify the global variable x
print("Global variable after modification:", x)


# The 'nonlocal' keyword
# 'nonlocal' is used to modify a variable in an enclosing (but non-global) scope
def modify_nonlocal():
    x = 60  # Enclosing variable

    def inner_function():
        nonlocal x  # Modifies the variable in the enclosing scope
        x = 70
        print("Nonlocal modified variable:", x)

    inner_function()
    print("Enclosing variable after nonlocal modification:", x)


modify_nonlocal()

# [Exercise]
# 1. Create a function called `modify_variable` that defines a local variable `x` with the value 5.
# 2. Inside the function, define an inner function `inner_modify` that modifies `x` by multiplying it by 2.
# 3. The inner function should access the variable `x` from the enclosing scope (using the `nonlocal` keyword).
# 4. After calling `inner_modify`, print the value of `x` inside `modify_variable`.

# Expected output:
# The modified value of x inside `modify_variable` should be 10 after calling `inner_modify`.
