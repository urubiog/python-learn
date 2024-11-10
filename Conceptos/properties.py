# Properties in Python allow us to define methods that can be accessed as attributes.
# They help us to control how an attribute is accessed, set, or deleted without directly exposing the underlying implementation.
# Let's delve into the elegance and utility of properties, ensuring controlled access to class attributes.

print("Mastering the Art of Properties in Python!")


# Defining a class with properties to control access to private attributes
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age  # Protected attribute

    # Getter method for 'age' property
    @property
    def age(self):
        return self._age

    # Setter method for 'age' property
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    # Deleter method for 'age' property
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

    # Property for 'name' without a setter, only a getter
    @property
    def name(self):
        return self._name

    # A read-only property for displaying a full introduction
    @property
    def introduction(self):
        return f"My name is {self._name} and I am {self._age} years old."


# Practical examples:

# Creating an instance of the Person class
person = Person("John", 30)

# Accessing the 'age' property (getter)
print(person.age)  # Output: 30

# Modifying the 'age' property (setter)
person.age = 35
print(person.age)  # Output: 35

# Attempting to set an invalid age (this will raise an exception)
try:
    person.age = -5  # Raises ValueError: Age cannot be negative!
except ValueError as ve:
    print(f"Error: {ve}")

# Accessing the 'name' property (getter)
print(person.name)  # Output: John

# Accessing the 'introduction' property (read-only)
print(person.introduction)  # Output: My name is John and I am 35 years old.

# Deleting the 'age' property (deleter)
del person.age  # Output: Deleting age...

# Try to access 'age' after deletion will raise an error
try:
    print(person.age)  # Raises AttributeError: 'Person' object has no attribute '_age'
except AttributeError as ae:
    print(f"Error: {ae}")
