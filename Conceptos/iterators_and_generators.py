# Iterators and Generators: Mastering the art of iteration in Python, where efficiency meets laziness.

print("Exploring Iterators and Generators in Python!")

# An iterator is any object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
# The iterator provides a way to access elements of a collection one at a time.

# Let's start by creating a custom iterator.


class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # The __iter__ method returns the iterator object itself.
    def __iter__(self):
        return self

    # The __next__ method defines the iteration behavior.
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # StopIteration is raised to signal the end of the iteration.
        self.current += 1
        return self.current - 1


# Using the custom iterator
print("Using custom iterator:")
my_iter = MyIterator(0, 5)  # Iterate from 0 to 4
for num in my_iter:
    print(num)

# [Exercise] Create an iterator class that iterates over odd numbers within a given range.

# Generators: A generator is a function that yields a sequence of values one at a time.
# It is defined using the `yield` keyword, and it provides an elegant way to create iterators.


def my_generator(start, end):
    while start < end:
        yield start  # Yield the value and suspend the function's execution.
        start += 1


# Using the generator
print("\nUsing generator:")
gen = my_generator(0, 5)  # Generate numbers from 0 to 4
for num in gen:
    print(num)

# [Exercise] Create a generator function that yields the squares of numbers within a given range.

# Now let's understand how Python handles iterators and generators with special methods.

# Iterators Special Methods

# __iter__: Returns the iterator object itself.
# __next__: Returns the next value from the iterator. If there are no more values, it raises StopIteration.

# Example of a built-in iterator, iterating over a list.
print("\nIterating over a list:")
my_list = [1, 2, 3, 4, 5]
my_list_iter = iter(my_list)  # Converts the list into an iterator
try:
    while True:
        print(next(my_list_iter))  # Fetches the next item from the iterator.
except StopIteration:
    pass  # StopIteration is expected when the iterator is exhausted.

# Generators Special Methods

# A generator function is similar to an iterator, but instead of keeping all values in memory,
# it "yields" them one at a time and suspends the function's state.

# Here's a generator expression, which is like a list comprehension but returns a generator.
print("\nUsing generator expression:")
gen_expr = (
    x * x for x in range(5)
)  # Creates a generator that yields squares of numbers.
for square in gen_expr:
    print(square)

# Comparison of Iterators and Generators:
# - An iterator is an object that implements the iterator protocol (with __iter__ and __next__ methods).
# - A generator is a function that uses the yield keyword and provides lazy evaluation.

# Summary of key points:
# - Iterators use the __iter__() and __next__() methods.
# - Generators use the yield keyword and provide lazy evaluation.
# - Generators are often more memory-efficient because they don't store all values in memory.
# - Generator expressions provide a concise way to create generators.

# [Exercise]
# Create a generator that yields Fibonacci numbers, and use it to print the first 10 Fibonacci numbers.
