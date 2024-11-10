# Now is the turn for identity operators. Enjoy!

print("Identity time!")

# In Python, identity operators are used to compare the memory locations of two objects.
# They check whether two objects are the same (refer to the same memory address).

# is     -> Returns True if both variables point to the same object
# is not -> Returns True if the variables point to different objects

# Examples:

# Using "is"
a = 10
b = 10
result_is = (
    a is b
)  # True -> Both variables point to the same object (small integers are cached in Python)

# Using "is not"
x = [1, 2, 3]
y = [1, 2, 3]
result_is_not = (
    x is not y
)  # True -> Lists with the same values are stored in different memory locations

# Comparing with "None"
z = None
result_none = z is None  # True -> z points to None

# [Exercise] What this will print?

a = 5
b = a
c = [5]
d = [5]

print((a is b) and (c is not d))

# out:
