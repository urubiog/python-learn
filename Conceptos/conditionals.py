# Time for conditionals in Python. Let the logic flow!

print("Conditionals time!")

# Conditional Statements
# These are used to execute different blocks of code based on specific conditions.

# if statement
# Executes the block of code only if the condition is True.
x = 10
if x > 5:
    print("x is greater than 5.")  # This will be executed because x > 5

# else statement
# Executes the block of code if the condition in the if statement is False.
x = 3
if x > 5:
    print("x is greater than 5.")
else:
    print(
        "x is not greater than 5."
    )  # This will be executed because x is not greater than 5

# elif statement
# A combination of "else" and "if" that allows checking multiple conditions.
x = 7
if x > 10:
    print("x is greater than 10.")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10.")  # This will be executed
else:
    print("x is 5 or less.")

# Nested if-else
# You can also nest if-else statements inside each other for more complex conditions.
x = 8
if x > 5:
    if x < 10:
        print("x is between 5 and 10.")  # This will be executed
    else:
        print("x is greater than or equal to 10.")
else:
    print("x is 5 or less.")

# The ternary (conditional) operator in Python
# A concise way to write simple if-else statements in one line.

# Syntax: value_if_true if condition else value_if_false
x = 12
result = "x is greater than 10" if x > 10 else "x is 10 or less"
print(result)  # Output: x is greater than 10

# [Exercise] What will happen if the following code is executed?

x = 15

if x > 10:
    print("x is greater than 10.")
elif x == 10:
    print("x is equal to 10.")
else:
    print("x is less than 10.")

# Answer:
# [ ] It will print "x is greater than 10."
# [ ] It will print "x is equal to 10."
# [ ] It will print "x is less than 10."
