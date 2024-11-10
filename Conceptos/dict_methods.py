# Now it's time for dictionary methods in Python. Enjoy!

print("Dictionary methods time!")

# Python provides several built-in methods for dictionaries that help in managing key-value pairs.

# dict.clear()
# Removes all the elements from the dictionary.
my_dict = {"name": "Alice", "age": 25}
my_dict.clear()
print(my_dict)  # Output: {}

# dict.copy()
# Returns a shallow copy of the dictionary.
my_dict = {"name": "Alice", "age": 25}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 25}

# dict.fromkeys()
# Creates a new dictionary from a given iterable, with specified keys and optional default values.
my_dict = dict.fromkeys(["name", "age"], "unknown")
print(my_dict)  # Output: {'name': 'unknown', 'age': 'unknown'}

# dict.get()
# Returns the value associated with a given key. If the key doesn't exist, returns a default value (None or provided value).
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("gender", "Not Specified"))  # Output: Not Specified

# dict.items()
# Returns a view object that displays a list of a dictionary's key-value tuple pairs.
my_dict = {"name": "Alice", "age": 25}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

# dict.keys()
# Returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# dict.pop()
# Removes and returns the value associated with a specified key. If the key does not exist, raises a KeyError.
my_dict = {"name": "Alice", "age": 25}
name = my_dict.pop("name")
print(name)  # Output: Alice
print(my_dict)  # Output: {'age': 25}

# dict.popitem()
# Removes and returns an arbitrary (key, value) pair from the dictionary. Raises a KeyError if the dictionary is empty.
my_dict = {"name": "Alice", "age": 25}
item = my_dict.popitem()
print(item)  # Output: ('age', 25) or ('name', 'Alice')

# dict.setdefault()
# Returns the value of a specified key if it exists, or inserts the key with a default value if the key does not exist.
my_dict = {"name": "Alice", "age": 25}
print(my_dict.setdefault("gender", "Female"))  # Output: Female (as it did not exist)
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'gender': 'Female'}

# dict.update()
# Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"age": 26, "city": "New York"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# dict.values()
# Returns a view object that displays a list of all the values in the dictionary.
my_dict = {"name": "Alice", "age": 25}
print(my_dict.values())  # Output: dict_values(['Alice', 25])

# [Exercise] What will happen if the following code is executed?

my_dict = {"name": "Alice", "age": 25}
my_dict.update({"city": "Paris"})
print(my_dict)

# Answer:
# [ ] The dictionary will remain unchanged
# [ ] A new key-value pair will be added to the dictionary
