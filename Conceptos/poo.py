# The world of Object-Oriented Programming (OOP) unlocks the power of modeling complex systems
# by organizing code into reusable, modular, and logical structures known as objects and classes.
# Let's delve into the essentials of OOP: inheritance, encapsulation, polymorphism, and abstraction.

print("Exploring the Depths of Object-Oriented Programming (OOP) in Python!")


# Example of a simple class definition
class Person:
    # The __init__ method is the constructor, which is called when an object is created
    def __init__(self, name, age):
        self.name = name  # Attribute to store the name
        self.age = age  # Attribute to store the age

    # A method to display information about the person
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an object (instance) of the Person class
person1 = Person("Alice", 30)

# Accessing the object's attributes and calling its methods
print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30
person1.introduce()  # Output: Hello, my name is Alice and I am 30 years old.


# Defining a base class to introduce the concept of inheritance and encapsulation
class Animal(
    object
):  # By default, classes in Python are inherited from the object class
    # Encapsulation: Protecting the internal state of the object using private attributes
    def __init__(self, name, age):
        self._name = name  # Protected attribute (intended for internal use)
        self.__age = (
            age  # Private attribute (cannot be accessed d  irectly outside the class)
        )

    # Getter method to access the private attribute
    def get_age(self):
        return self.__age

    # Setter method to modify the private attribute
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive value.")

    # Method to simulate behavior (Polymorphism)
    def speak(self):
        print(f"{self._name} makes a sound.")


# Inheritance: The Dog class inherits from the Animal class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Inheriting the base class constructor
        self._breed = breed  # New attribute specific to the Dog class

    # Overriding the speak() method (Polymorphism)
    def speak(self):
        print(f"{self._name} barks!")


# Another subclass of Animal: The Cat class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color  # New attribute specific to the Cat class

    # Overriding the speak() method (Polymorphism)
    def speak(self):
        print(f"{self._name} meows!")


# Abstraction: The abstract class can define abstract methods, leaving the implementation to subclasses.
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass  # Abstract method, must be implemented by any subclass


# The Car class implements the move() method of the Vehicle abstract class
class Car(Vehicle):
    def move(self):
        print("The car drives on the road.")


# The Boat class implements the move() method of the Vehicle abstract class
class Boat(Vehicle):
    def move(self):
        print("The boat sails on water.")


# Practical examples of using the classes defined above:

# Creating instances of Dog and Cat (Polymorphism in action)
dog = Dog("Rex", 5, "Labrador")
cat = Cat("Whiskers", 3, "White")

# Accessing methods
dog.speak()  # Output: Rex barks!
cat.speak()  # Output: Whiskers meows!

# Creating instances of Car and Boat
car = Car()
boat = Boat()

# Using polymorphism (different classes implementing the same method)
car.move()  # Output: The car drives on the road.
boat.move()  # Output: The boat sails on water.

# Demonstrating encapsulation and abstraction:
# Accessing the private attribute __age through a getter method
print(dog.get_age())  # Output: 5

# Using setter to modify the age
dog.set_age(6)
print(dog.get_age())  # Output: 6

# Trying to directly access the private attribute would raise an error
# print(dog.__age)  # This will raise an AttributeError

# Encapsulation prevents direct access to __age, ensuring controlled modification.

# Exercise:
# Define a class 'Person' that inherits from the 'Animal' class. Add attributes like name and occupation.
# Create an instance of 'Person' and call the 'speak' method.
