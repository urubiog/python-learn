# Now is the turn for derivative types in Python. Enjoy!

print("Derivative types time!")

# Python provides several derivative types to organize and manipulate data.
# These are built upon fundamental types like numbers and strings.

# List
# - A mutable (modifiable) ordered collection of items.
# - Used to store multiple items, which can be of different types.
# - Items are accessed by their index, starting from 0.

my_list = [1, 2, 3, 4, 5]
print(my_list[3])  # 4
my_list[3] = 66
print(my_list)  # [1, 2, 3, 66, 5]

# Another way to create a list:
list_from_tuple = list((1, 2, 3, 4))  # Creates a list from a tuple
print(list_from_tuple)  # [1, 2, 3, 4]

# You can even make lists of lists
another_list = [[1, 2, 3], [4, 5, 6]]  # matrix
another_list = [[1, 2, 3], [4, 5, 6]]  # first row  # second row

print(another_list[0][1])  # 2 -> another_list[row][col]

# It can store any type
lst = [12, 12.3542, [12, 21], (12,), None, False, True]
print(lst)

# Tuple
# - An immutable (non-modifiable) ordered collection of items.
# - Useful for grouping related pieces of data that shouldn't change.

my_tuple = (10, 20, 30)
print(my_tuple)

# Another way to create a tuple:
tuple_from_list = tuple([1, 2, 3, 4])  # Creates a tuple from a list
print(tuple_from_list)  # (1, 2, 3, 4)

# Set
# - An unordered collection of unique items.
# - Used to store distinct values and perform set operations like union or intersection.

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Another way to create a set:
set_from_list = set([1, 2, 3, 4, 5])  # Creates a set from a list (removes duplicates)
print(set_from_list)  # {1, 2, 3, 4, 5}

# Dictionary
# - A mutable collection of key-value pairs.
# - Keys must be unique and immutable; values can be of any type.
# - Used for fast lookups and to organize data in a structured way.

my_dict = {"name": "Alice", "age": 25}
print(my_dict)

# Another way to create a dictionary:
dict_from_args = dict(
    name="Macumba", age=25
)  # Creates a dictionary from keyword arguments
print(dict_from_args)  # {'name': 'Macumba', 'age': 25}

# [Exercise] What will happen if the following code is executed?

a = [1, 2]
b = [3, 4]
t = (a, b)

t[1][1] = 6

# Answer:
# [ ] An error will be raised
# [ ] It will change the value inside t
