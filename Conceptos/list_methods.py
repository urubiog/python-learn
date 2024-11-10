# Now it's time for list methods in Python. Enjoy!

print("List methods time!")

# Python provides several built-in methods for lists that allow you to manipulate and interact with list data.

# list.append()
# Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# list.clear()
# Removes all elements from the list, leaving it empty.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []

# list.copy()
# Returns a shallow copy of the list.
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

# list.count()
# Returns the number of occurrences of an element in the list.
my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))  # Output: 3

# list.extend()
# Adds all elements from an iterable (e.g., another list) to the end of the list.
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # Output: [1, 2, 3, 4]

# list.index()
# Returns the index of the first occurrence of an element in the list.
my_list = [10, 20, 30, 40]
print(my_list.index(30))  # Output: 2

# list.insert()
# Inserts an element at a specific position in the list.
my_list = [1, 2, 3]
my_list.insert(1, 99)
print(my_list)  # Output: [1, 99, 2, 3]

# list.pop()
# Removes and returns the element at a specified position in the list.
# If no index is specified, it removes and returns the last element.
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2
print(my_list)  # Output: [1, 3]

# list.remove()
# Removes the first occurrence of a specified element from the list. Raises a ValueError if the element is not found.
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# list.reverse()
# Reverses the order of the elements in the list.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

# list.sort()
# Sorts the elements of the list in place.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

# [Exercise] What will happen if the following code is executed?

my_list = [5, 3, 8, 6, 7]
my_list.sort(reverse=True)
print(my_list)

# Answer:
# [ ] The list will be sorted in ascending order
# [ ] The list will be sorted in descending order
