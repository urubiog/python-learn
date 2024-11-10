# Now is the turn for logical operators. Enjoy!

print("Logic time!")

# In Python, you can use logical operators to combine conditions
# and  -> returns True if both conditions are True
# or   -> returns True if at least one condition is True
# not  -> negates the condition, turning True into False and vice versa

# Logical operators work with boolean values (True or False).

a = 5
b = 10
c = 15

# AND Operator
result_and = (a < b) and (b < c)  # True and True -> True
result_and2 = (a > b) and (b < c)  # False and True -> False

# OR Operator
result_or = (a > b) or (b < c)  # False or True -> True
result_or2 = (a > b) or (c < b)  # False or False -> False

# NOT Operator
result_not = not (a < b)  # not True -> False
result_not2 = not (a > b)  # not False -> True

# [Exercise] What this will print?

print((a < b) and not (b > c or c == 15))

# out:
