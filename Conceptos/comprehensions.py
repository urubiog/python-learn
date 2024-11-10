# Now we delve into comprehensions, the elegant and concise way to create sequences
# and dictionaries, all while maintaining clarity and readability. A true display of Pythonic grace.

print("Comprehensions time!")

# List Comprehension
# The list comprehension allows us to create a new list by applying an expression to each element of an iterable
numbers = [x * 2 for x in range(5)]  # Doubles each number in the range from 0 to 4
print(f"List comprehension: {numbers}")

# List comprehension with condition
# We can add conditions to filter the elements from the iterable
even_numbers = [x for x in range(10) if x % 2 == 0]  # Only even numbers
print(f"Even numbers: {even_numbers}")

# Nested list comprehension
# You can use nested comprehensions for more complex operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in matrix for item in sublist]  # Flattening the 2D list
print(f"Flattened matrix: {flattened}")

# Dictionary Comprehension
# Similar to list comprehensions, but used to create dictionaries
squares_dict = {x: x**2 for x in range(5)}  # Maps each number to its square
print(f"Dictionary comprehension: {squares_dict}")

# Dictionary comprehension with condition
# Just like with lists, we can filter dictionary comprehension based on conditions
even_squares_dict = {
    x: x**2 for x in range(5) if x % 2 == 0
}  # Only even numbers squared
print(f"Even squares dictionary: {even_squares_dict}")

# Set Comprehension
# A set comprehension creates a set, which is similar to a list but with no duplicates
unique_numbers = {x for x in range(10)}  # Set with unique numbers
print(f"Set comprehension: {unique_numbers}")

# Set comprehension with condition
# We can add conditions in set comprehensions as well
even_set = {x for x in range(10) if x % 2 == 0}  # Set with even numbers only
print(f"Even set: {even_set}")

# Generator Expression
# A generator expression is similar to a list comprehension but produces a generator instead of a list
gen_expression = (x * 2 for x in range(5))  # Generator that doubles the numbers
print(
    f"Generator expression: {list(gen_expression)}"
)  # Convert to list to see the results

# Nested Dictionary Comprehension
# Creating a dictionary where each key is a number and the value is another dictionary
nested_dict = {
    x: {y: x * y for y in range(3)} for x in range(3)
}  # Creating a multiplication table
print(f"Nested dictionary comprehension: {nested_dict}")

# Conditional Expressions in Comprehensions
# We can use conditional expressions inside comprehensions for more complex logic
numbers_with_sign = [
    f"Positive {x}" if x > 0 else f"Negative {x}" for x in range(-3, 4)
]
print(f"Conditional list comprehension: {numbers_with_sign}")

# Exercise:
# Create a list comprehension that generates a list of the first 10 squares of odd numbers.
