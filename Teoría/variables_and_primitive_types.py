# Welcome to the practical learning Python resource. I invite you to also create your own .py modules and practice freely. Let's start!

print("Hello world")

# Python recognizes these primitive types, 
# each one is meant to store different types of data 
int   # integers
float # floating-point numbers
str   # strings
bool  # booleans

# Variables are just containers that store data in memory temporarily
this_is_a_variable_for_an_integer = 5 # = the equal sign is not used to compare equallities, is the assignment operator used to give value

print(this_is_a_variable_for_an_integer) # out: 5

# Variables can change its value over time 
this_is_a_variable_for_an_integer = 6 # We have reassigned the value to 6 

print(this_is_a_variable_for_an_integer) # out: 6

# Examples
f = 5.5
string = "Hello"
boolean = False

# Some types can be added with others
# The behaviour is determinated by Python
print(string + ", I'm using Python") # out: "Hello, I'm using Python"

# Now, imagin that you won't use anymore the string variable
del string # You can delete it and free the memory it occupied using del operator

# We can even multiply strings with integers
print("Hello" * 2) # out: "HelloHello" -> What's inside the round brackets will be evaluated and then interpretated as the argument for print()

# There's also a type for absence of value (None)
none_value = None

# As variables exist, there also exist constants
# which are used to store non-changing value variables
PI = 3.1415

# We can instanciate variables specifing explicitly its type 
a = int(6.6) # 6 -> Integers doesn't accept a decimal part, so the initial value is truncated

print(type(a)) # out: <class 'int'> -> type() function will tell us about the type of a variable 

b = float(5.21214214812)
c = str("Hello world") # Be careful, not the same as string(Hello world), that would be an error

t = bool(1)      # True
t = bool(55)     # True
t = bool(-12421) # True
f = bool(0)      # False

# Moreover, the input() function takes input from the user
input("What's your name? ") # In this case, the code will be executed but not stored in any variable 

b = input("How old are you? ") # input() returns the value as a string, so we have to convert it to int 
b = int(b)

print(f"Wow! You're {b} y/o.") # This is a f-string, you can insert code that will be interpreted to give its value

# [Exercice] What will this print? 
print(3.6 + 6)

# Response: 
