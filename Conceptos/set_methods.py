# Now it's time for set methods in Python. Enjoy!

print("Set methods time!")

# Python provides several built-in methods for sets to perform operations like unions, intersections, and more.

# set.add()
# Adds a single element to the set.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# set.clear()
# Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()

# set.copy()
# Returns a shallow copy of the set.
my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

# set.difference()
# Returns a new set with elements that are in the original set but not in another set.
set_a = {1, 2, 3}
set_b = {2, 3, 4}
difference = set_a.difference(set_b)
print(difference)  # Output: {1}

# set.difference_update()
# Removes elements from the set that are present in another set.
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.difference_update(set_b)
print(set_a)  # Output: {1}

# set.discard()
# Removes an element from the set if it exists, but does nothing if the element is not found.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
my_set.discard(4)  # No error if the element is not present.
print(my_set)  # Output: {1, 3}

# set.intersection()
# Returns a new set with elements that are present in both sets.
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection = set_a.intersection(set_b)
print(intersection)  # Output: {2, 3}

# set.intersection_update()
# Updates the original set with elements that are present in both sets.
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a.intersection_update(set_b)
print(set_a)  # Output: {2, 3}

# set.isdisjoint()
# Returns True if two sets have no elements in common.
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.isdisjoint(set_b))  # Output: True

# set.issubset()
# Returns True if all elements of the set are in another set.
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))  # Output: True

# set.issuperset()
# Returns True if the set contains all elements of another set.
set_a = {1, 2, 3}
set_b = {1, 2}
print(set_a.issuperset(set_b))  # Output: True

# set.pop()
# Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element)  # Output: (The popped element, randomly chosen)
print(my_set)  # Output: Set with one less element.

# set.remove()
# Removes a specific element from the set. Raises KeyError if the element is not found.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
# my_set.remove(4)  # Uncommenting this would raise a KeyError because 4 is not in the set.

# set.symmetric_difference()
# Returns a new set with elements that are in either of the sets, but not in both.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
symmetric_difference = set_a.symmetric_difference(set_b)
print(symmetric_difference)  # Output: {1, 2, 4, 5}

# set.symmetric_difference_update()
# Updates the original set with elements that are in either set, but not in both.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.symmetric_difference_update(set_b)
print(set_a)  # Output: {1, 2, 4, 5}

# set.union()
# Returns a new set with all elements that are in either set.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union = set_a.union(set_b)
print(union)  # Output: {1, 2, 3, 4, 5}

# set.update()
# Adds elements from another set or iterable to the original set.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b)
print(set_a)  # Output: {1, 2, 3, 4, 5}

# [Exercise] What will happen if the following code is executed?

set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_a.update(set_b)
print(set_a)

# Answer:
# [ ] The set_a will remain unchanged
# [ ] The set_a will contain all unique elements from both sets
