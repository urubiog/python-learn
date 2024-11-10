# Special Methods in Python: These methods are essential for customizing the behavior of objects.
# They allow us to define how our objects behave with respect to built-in operations,
# such as comparison, addition, string representation, and much more.
# In this module, we will explore the most commonly used special methods in Python.

print("Mastering Special Methods in Python!")


# __init__: The constructor method, called when an object is created
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating an object of MyClass
obj = MyClass("Alice", 30)
print(f"__init__: {obj.name}, {obj.age}")
# This special method is automatically called when a new instance of the class is created.


# __repr__: Called by the built-in function `repr()` and provides a string representation of the object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Creating a Point object
p = Point(3, 4)
print(f"__repr__: {repr(p)}")
# __repr__ should return a string that ideally gives a clear, unambiguous representation of the object.


# __str__: Called by the built-in function `str()` and provides a string representation for the user
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"


# Creating a Car object
car = Car("Toyota", "Corolla")
print(f"__str__: {str(car)}")
# __str__ is meant to return a user-friendly string representation of the object.


# __len__: Defines behavior for the built-in `len()` function
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)


# Creating a MyList object
my_list = MyList([1, 2, 3, 4])
print(f"__len__: {len(my_list)}")
# __len__ is called when we use the `len()` function on an object.


# __getitem__: Defines behavior for indexing into an object (e.g., obj[index])
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]


# Accessing an item from MyCollection
collection = MyCollection([10, 20, 30])
print(f"__getitem__: {collection[1]}")
# __getitem__ allows the use of square brackets for indexing.


# __setitem__: Defines behavior for setting values using indexing (e.g., obj[index] = value)
class MyDictionary:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value


# Setting a value using indexing
my_dict = MyDictionary()
my_dict["name"] = "Alice"
print(f"__setitem__: {my_dict.data}")
# __setitem__ is used when you assign values to an object via indexing.


# __delitem__: Defines behavior for deleting items using indexing (e.g., del obj[index])
class MyDict:
    def __init__(self):
        self.items = {}

    def __delitem__(self, key):
        del self.items[key]


# Deleting a key from MyDict
my_dict2 = MyDict()
my_dict2.items = {"key1": "value1", "key2": "value2"}
del my_dict2["key1"]
print(f"__delitem__: {my_dict2.items}")
# __delitem__ allows the use of `del` to remove items from an object.


# __contains__: Defines behavior for the `in` operator
class MySet:
    def __init__(self, elements):
        self.elements = elements

    def __contains__(self, item):
        return item in self.elements


# Checking membership in MySet
my_set = MySet([1, 2, 3])
print(f"__contains__: {2 in my_set}")
# __contains__ allows the use of the `in` operator for checking membership.


# __call__: Allows an instance to be called as a function
class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x


# Calling an object as a function
adder = Adder(10)
print(f"__call__: {adder(5)}")
# __call__ allows the object to be used as a callable function.


# __eq__: Defines behavior for equality comparison (e.g., obj1 == obj2)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


# Comparing two Person objects
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
print(f"__eq__: {person1 == person2}")
# __eq__ allows custom comparison logic for equality.


# __lt__, __gt__, __le__, __ge__, __ne__: Comparison operators (<, >, <=, >=, !=)
class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def __lt__(self, other):
        return self.temp < other.temp


# Comparing two Temperature objects
temp1 = Temperature(20)
temp2 = Temperature(25)
print(f"__lt__: {temp1 < temp2}")
# These methods enable object comparisons using operators like <, >, <=, >=, and !=.


# __add__: Defines behavior for the addition operator (+)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


# Adding two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print(f"__add__: ({result.x}, {result.y})")
# __add__ allows the use of the addition operator (+) to combine two objects.


# __mul__: Defines behavior for the multiplication operator (*)
class Box:
    def __init__(self, size):
        self.size = size

    def __mul__(self, other):
        return Box(self.size * other)


# Multiplying a Box object
box = Box(3)
multiplied_box = box * 2
print(f"__mul__: {multiplied_box.size}")
# __mul__ allows the use of the multiplication operator (*) to modify an object.

# [Exercise]
# What happens if we implement the __call__ method without a parameter?

# Try defining a class with a __call__ method that doesn't take parameters and invoke it.
