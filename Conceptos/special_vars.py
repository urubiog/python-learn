# Understanding Special Variables in Python: These variables serve as essential tools in introspection,
# module management, and debugging, offering us a deeper connection with the internal workings of Python.
# In this module, we will explore the usage and implications of various special variables in Python.

print("Mastering Special Variables in Python!")

# __name__: Indicates the name of the module in Python
print(f"__name__: {__name__}")
# If this module is executed directly, the value of __name__ will be "__main__". If it is imported, it will be the name of the file.
# This is used to differentiate between running the script directly and importing it.

# __doc__: Contains the docstring associated with the current module
print(f"__doc__: {__doc__}")
# The docstring, if present, describes the purpose of the module and can be accessed through this special variable.

# __package__: Indicates the package name to which the module belongs
print(f"__package__: {__package__}")
# If the module is inside a package, this variable will contain the name of the package. Otherwise, it will be None.

# __loader__: Provides information about the loader of the module
print(f"__loader__: {__loader__}")
# This variable contains the loader object of the module, useful for introspection about how the module was loaded.

# __file__: The file path of the module
print(f"__file__: {__file__}")
# This shows the full path to the module file, allowing you to locate the file in the system.

# __cached__: Stores the path to the cache file generated by the Python interpreter for the module
print(f"__cached__: {__cached__}")
# If the module has a cache file, this variable will contain the path to the `.pyc` file.

# __spec__: Provides information about the `ModuleSpec` object representing the module's specification
print(f"__spec__: {__spec__}")
# Provides information on how the module should be loaded, useful for debugging module loading issues.

# __builtins__: A dictionary containing all the built-in functions and variables of Python
print(f"__builtins__: {__builtins__}")
# Contains all functions and variables that are globally accessible without needing to import them.


# __annotations__: Stores the type annotations defined for a function or method
def example_function(a: int, b: str) -> bool:
    return a > 0 and b == "Yes"


print(f"__annotations__: {example_function.__annotations__}")
# Type annotations are stored in this special variable, which can be useful for type validation and documentation.


# __dict__: A dictionary that contains the attributes of an object
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20


obj = MyClass()
print(f"__dict__: {obj.__dict__}")
# By accessing `__dict__`, we get a dictionary of the instance's attributes.

# __path__: Contains the list of search paths for a module's package
# print(f"__path__: {__path__}")
# This variable contains the paths where the package can search for other modules.


# __slots__: Allows restricting the attributes of a class, reducing memory usage and speeding up attribute access
class Person:
    __slots__ = ["name", "age"]  # Only these attributes are allowed

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alice", 30)
print(f"__slots__: {p.__slots__}")
# `__slots__` prevents the object from having dynamically defined attributes outside the ones specified, saving memory.

# __class__: Contains the class to which an instance of an object belongs
print(f"__class__: {p.__class__}")
# This variable contains the class of the instance, in this case `Person`.

# __weakref__: Contains weak references of the object, if any
import weakref

# weak_ref = weakref.ref(p)
# print(f"__weakref__: {p.__weakref__}")
# Primarily used for memory management, it holds weak references to an object, allowing the avoidance of reference cycles.


# __mro__: A tuple containing the method resolution order for a class
class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(f"__mro__: {C.__mro__}")
# `__mro__` shows the order in which base classes will be searched to resolve methods, making it useful for introspection of inheritance.

# __bases__: Contains a tuple of direct base classes for a class
print(f"__bases__: {C.__bases__}")
# `__bases__` shows the direct base classes of the class `C`, useful for understanding the class hierarchy.


# __closure__: Contains a tuple of cells holding the free variables referenced by a nested function, if it is a nested function
def outer():
    x = 10

    def inner():
        return x

    return inner


closure_func = outer()
print(f"__closure__: {closure_func.__closure__}")
# If a function has free variables (such as `x`), `__closure__` holds them in a tuple of cells.

# __code__: Contains the bytecode object of the function, along with information about its arguments, constants, etc.
print(f"__code__: {closure_func.__code__}")
# `__code__` holds information about the bytecode of the function, which is useful for analysis and debugging.


# __defaults__: Contains a tuple with the default values for the parameters of a function
def sample_func(a, b=5, c=10):
    pass


print(f"__defaults__: {sample_func.__defaults__}")
# `__defaults__` holds the default values for the function parameters (in this case, 5 and 10).


# __kwdefaults__: Contains a dictionary with the default values for the keyword parameters of a function
def sample_kw_func(a, b=5, c=10, d="hello"):
    pass


print(f"__kwdefaults__: {sample_kw_func.__kwdefaults__}")
# `__kwdefaults__` contains a dictionary with the default values for the keyword parameters (in this case, 'hello').

# [Exercise]
# What happens if we try to modify the variable __name__?
# Implement code where you modify __name__ and observe its behavior.
