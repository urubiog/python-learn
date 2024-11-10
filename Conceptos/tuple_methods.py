# Now it's time for tuple methods in Python. Enjoy!

print("Tuple methods time!")

# Tuples in Python are immutable sequences, and they come with a limited set of methods.
# These methods allow us to count and find specific elements in a tuple.

# tuple.count()
# Counts the number of occurrences of a value in the tuple.
my_tuple = (1, 2, 3, 1, 4, 1)
count_of_1 = my_tuple.count(1)
print(f"Count of 1: {count_of_1}")  # Output: Count of 1: 3

# tuple.index()
# Returns the index of the first occurrence of a value in the tuple.
# If the value is not found, raises a ValueError.
index_of_2 = my_tuple.index(2)
print(f"Index of 2: {index_of_2}")  # Output: Index of 2: 1

# [Exercise] What will happen if the following code is executed?

my_tuple = (5, 6, 7, 5, 8, 5)
index_of_5 = my_tuple.index(5)
count_of_5 = my_tuple.count(5)

print(index_of_5)  # Index of the first 5
print(count_of_5)  # Count of how many times 5 appears in the tuple

# Answer:
# [ ] The index will be returned, and the count will be 2.
# [ ] The index will be returned, and the count will be 3.
