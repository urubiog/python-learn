# Time for loops in Python. The rhythm of repetition!

print("Loops time!")

# Loops are used to repeat a block of code multiple times based on a given condition.

# For Loop
# The "for" loop is used to iterate over a sequence (like a list, tuple, or range) and execute a block of code for each item.

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # This will print each fruit in the list

# Using range() with for loop
# The range() function generates a sequence of numbers, which can be iterated using a for loop.
for i in range(5):  # range(5) generates numbers 0, 1, 2, 3, 4
    print(i)  # This will print numbers from 0 to 4

# Nested for loops
# A for loop can be nested inside another for loop.
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")  # This will print a combination of values of i and j

# While Loop
# The "while" loop repeats a block of code as long as a given condition is True.
x = 0
while x < 5:  # This will keep running as long as x is less than 5
    print(x)  # This will print numbers from 0 to 4
    x += 1  # Increment x by 1 after each iteration

# Infinite loop (don't run this in production code, unless you know what you're doing!)
# A while loop can run forever if the condition is always True.
# while True:
#     print("This will run forever!")  # This will never stop unless interrupted manually.

# Loop Control Statements
# These are used to alter the flow of the loop (exit it, skip iterations, etc.).

# break statement
# Used to exit a loop completely, even if the loop's condition is still True.
for i in range(10):
    if i == 5:
        break  # Exit the loop when i reaches 5
    print(i)  # This will print numbers from 0 to 4

# continue statement
# Used to skip the current iteration and move to the next one.
for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i is 3
    print(i)  # This will print numbers 0, 1, 2, 4 (skipping 3)

# else with loops
# The "else" clause can be used with loops, and it will execute if the loop completes normally (without a break).
for i in range(5):
    print(i)  # Prints numbers from 0 to 4
else:
    print(
        "Loop finished without interruption."
    )  # This will be executed after the loop completes

# [Exercise] What will happen if the following code is executed?

for i in range(5):
    if i == 2:
        break  # This will exit the loop when i equals 2
    print(i)  # This will print numbers up to 2 (but not 2 itself)

# Answer:
# [ ] It will print 0, 1, 2
# [ ] It will print 0, 1
# [ ] It will print 0, 1, 2, 3, 4
