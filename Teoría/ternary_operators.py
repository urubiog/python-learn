# Now it's time for ternary operators in Python. Enjoy!

print("Ternary operators, here we go!")

# In Python, ternary operators are used to evaluate a condition in a compact way on a single line.
# The basic syntax is:
# value_if_true if condition else value_if_false

condition = True
value_if_true = 1
value_if_false = 0

result = value_if_true if condition else value_if_false

# Simple ternary operator example
age = 20
majority_age = "Adult" if age >= 18 else "Minor"
print(majority_age)  # Output: "Adult"

# Example with even or odd number
number = 15
result = "Even" if number % 2 == 0 else "Odd"
print(result)  # Output: "Odd"

# Ternary operator is ideal when we want to choose between two values based on a condition.

# We can also use it for more complex assignments:
# Example with multiple ternaries
result = 10
b = 5
greater = "a is greater" if result > b else "b is greater or equal"
print(greater)  # Output: "a is greater"

# There are two other syntaxes for these operators
result = condition and value_if_true or value_if_false
result = (value_if_false, value_if_true)[condition]

# [Exercise] What will be printed by the following code?

x = 10
y = 15
result = "Greater" if x > y else "Lesser"
print(result)

# Answer:
# [ ] Greater
# [ ] Lesser


