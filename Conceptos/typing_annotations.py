# The time has come to master typing annotations, where we bring clarity and precision
# to the types of variables and functions, ensuring the safety and correctness of our code.

print("Typing annotations time!")

# Basic variable annotations
x: int = 5  # x is annotated to be an integer
y: str = "Hello, world!"  # y is annotated to be a string
z: float = 3.14  # z is annotated to be a floating point number

print(f"x: {x}, y: {y}, z: {z}")


# Function annotations
def greet(name: str) -> str:
    return f"Hello, {name}!"


# The function greet expects a string as the parameter 'name' and returns a string
result = greet("Sir Python")
print(result)


# Annotating functions with multiple parameters
def add_numbers(a: int, b: int) -> int:
    return a + b


# This function expects two integers and returns their sum as an integer
sum_result = add_numbers(10, 20)
print(f"Sum: {sum_result}")


# Default argument annotations
def multiply(a: int, b: int = 2) -> int:
    return a * b


# In this case, 'b' has a default value of 2, and the function returns an integer
product_result = multiply(5)
print(f"Product with default b: {product_result}")

# Using Union for multiple possible types
from typing import Union


def get_length(value: Union[str, list]) -> int:
    return len(value)


# The function get_length can accept either a string or a list and will return the length
string_length = get_length("Python")
list_length = get_length([1, 2, 3, 4])

print(f"String length: {string_length}, List length: {list_length}")

# Annotating functions with a tuple return type
from typing import Tuple


def divide(a: int, b: int) -> Tuple[int, float]:
    return a // b, a / b


# The divide function returns a tuple of two values: the integer division and the floating-point division
integer_division, float_division = divide(10, 3)
print(f"Integer division: {integer_division}, Float division: {float_division}")

# Using Optional for parameters that can be None
from typing import Optional


def greet_with_optional(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Stranger!"
    return f"Hello, {name}!"


# The function greet_with_optional allows the 'name' parameter to be None, and returns a default greeting if so
default_greeting = greet_with_optional()
personalized_greeting = greet_with_optional("Sir Python")

print(f"Default greeting: {default_greeting}")
print(f"Personalized greeting: {personalized_greeting}")

# Creating a custom type alias
from typing import List

# Defining a custom type alias for a list of integers
Vector = List[int]


def sum_vector(vector: Vector) -> int:
    return sum(vector)


# Using the custom alias 'Vector' to define a list of integers
vector_sum = sum_vector([1, 2, 3, 4, 5])
print(f"Sum of vector: {vector_sum}")

# Using Literal to restrict a function to specific values
from typing import Literal


def color_choice(color: Literal["red", "green", "blue"]) -> str:
    return f"You selected the color {color}!"


# The function color_choice only accepts specific color choices: "red", "green", or "blue"
selected_color = color_choice("red")
print(selected_color)

# Using Callable for typing functions as arguments
from typing import Callable


def apply_function(f: Callable[[int, int], int], x: int, y: int) -> int:
    return f(x, y)


# The function apply_function expects a function 'f' that takes two integers and returns an integer
result_function = apply_function(add_numbers, 5, 7)
print(f"Result of applying function: {result_function}")

# Using TypeVar for generic types
from typing import TypeVar

T = TypeVar("T")


def identity(value: T) -> T:
    return value


# The function identity is generic and can accept any type of value and return a value of the same type
print(identity(10))  # Integer
print(identity("Hello"))  # String

# Now, let's introduce TypeAlias: A cleaner way to define more complex type aliases

from typing import TypeAlias

# Creating a more readable alias for a tuple that represents a 2D point (x, y) of type float
Point: TypeAlias = Tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    # Using the Pythagorean theorem to calculate the distance between two points
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


# Using the Point alias to define tuples representing 2D points
point1: Point = (1.0, 2.0)
point2: Point = (4.0, 6.0)

print(f"Distance between points: {distance(point1, point2)}")
