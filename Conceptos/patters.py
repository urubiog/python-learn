# The time has come for the match statement. A refined approach to conditional branching.

print("Match time!")

# The match statement allows you to match a value against several patterns, offering a more readable and expressive way to perform multiple conditional checks.

# Basic usage of match
x = 2

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")  # This will print because x is 2
    case 3:
        print("x is 3")
    case _:
        print(
            "x is something else"
        )  # The underscore (_) acts as a wildcard, matching anything

# Pattern matching with multiple values
y = (10, 20)

match y:
    case (10, 20):
        print("y is (10, 20)")  # This will match and print "y is (10, 20)"
    case (x, y):
        print(f"y is a tuple with values {x} and {y}")
    case _:
        print("y is something else")

# Using match with lists
z = [1, 2, 3]

match z:
    case [1, 2, 3]:
        print("z is exactly [1, 2, 3]")  # This matches exactly
    case [1, *rest]:  # The *rest pattern captures all remaining elements in the list
        print(f"z starts with 1, and the rest is {rest}")
    case _:
        print("z is something else")

# The 'case' can also match types, which helps in making more complex conditionals based on the data's structure.
a = 42

match a:
    case int():  # Checks if the value is of type int
        print("a is an integer")  # This will print because a is indeed an int
    case str():
        print("a is a string")
    case _:
        print("a is something else")

# You can also use guards with match statements, adding conditions to a case.
b = 30

match b:
    case (
        x
    ) if x > 10:  # Guard condition ensures this case matches only if b is greater than 10
        print(f"b is greater than 10, specifically {x}")
    case _:
        print("b is 10 or less")

# [Exercise] What will happen if the following code is executed?

animal = "cat"

match animal:
    case "dog":
        print("It's a dog")
    case "cat":
        print("It's a cat")  # This will match because animal is "cat"
    case _:
        print("It's some other animal")

# Answer:
# [ ] It will print "It's a dog"
# [ ] It will print "It's a cat"
# [ ] It will print "It's some other animal"
