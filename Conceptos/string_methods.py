# Now it's time for string methods in Python. Enjoy!

print("String methods time!")

# Python provides several built-in methods for strings that allow you to manipulate and interact with text.

# str.capitalize()
# Capitalizes the first letter of the string and converts the rest to lowercase.
name = "hello"
print(name.capitalize())  # Output: "Hello"

# str.casefold()
# Returns a lowercase version of the string, useful for case-insensitive text comparisons.
text = "HELLO"
print(text.casefold())  # Output: "hello"

# str.center()
# Centers the string in a specified width, padding with a specified character.
message = "Python"
print(message.center(10, "*"))  # Output: "**Python**"

# str.count()
# Returns the number of occurrences of a substring in the string.
phrase = "hello hello hello"
print(phrase.count("hello"))  # Output: 3

# str.encode()
# Encodes the string using the specified encoding.
text = "Python"
encoded = text.encode("utf-8")
print(encoded)  # Output: b'Python'

# str.endswith()
# Checks if the string ends with the specified substring, returning True or False.
file_name = "document.txt"
print(file_name.endswith(".txt"))  # Output: True

# str.expandtabs()
# Expands the tab characters in the string into spaces.
text_with_tabs = "a\tb\tc"
print(text_with_tabs.expandtabs(4))  # Output: "a   b   c"

# str.find()
# Searches for the first occurrence of a substring and returns its index.
sentence = "Python is awesome"
print(sentence.find("is"))  # Output: 7

# str.format()
# Formats the string using arguments.
greeting = "Hello, {}!"
print(greeting.format("Alice"))  # Output: "Hello, Alice!"

# str.format_map()
# Formats the string using a mapping (a dictionary).
person = {"name": "Bob", "age": 30}
info = "Name: {name}, Age: {age}"
print(info.format_map(person))  # Output: "Name: Bob, Age: 30"

# str.index()
# Similar to find(), but raises a ValueError if the substring is not found.
sentence = "Python is great"
print(sentence.index("is"))  # Output: 7

# str.isalnum()
# Checks if all characters in the string are alphanumeric (letters and digits).
text = "Python3"
print(text.isalnum())  # Output: True

# str.isalpha()
# Checks if all characters in the string are alphabetic.
word = "Python"
print(word.isalpha())  # Output: True

# str.isascii()
# Checks if all characters in the string are ASCII characters.
text = "Hello"
print(text.isascii())  # Output: True

# str.isdecimal()
# Checks if all characters in the string are decimal characters.
number = "12345"
print(number.isdecimal())  # Output: True

# str.isdigit()
# Checks if all characters in the string are digits.
digits = "12345"
print(digits.isdigit())  # Output: True

# str.isidentifier()
# Checks if the string is a valid identifier (e.g., for variable names).
var_name = "variable"
print(var_name.isidentifier())  # Output: True

# str.islower()
# Checks if all characters in the string are lowercase.
word = "python"
print(word.islower())  # Output: True

# str.isnumeric()
# Checks if all characters in the string are numeric.
numeric = "12345"
print(numeric.isnumeric())  # Output: True

# str.isprintable()
# Checks if all characters in the string are printable.
text = "Hello, World!"
print(text.isprintable())  # Output: True

# str.isspace()
# Checks if all characters in the string are whitespace characters.
whitespace = "    "
print(whitespace.isspace())  # Output: True

# str.istitle()
# Checks if the string follows title case (capitalized words).
title = "Hello World"
print(title.istitle())  # Output: True

# str.isupper()
# Checks if all characters in the string are uppercase.
word = "PYTHON"
print(word.isupper())  # Output: True

# str.join()
# Joins elements of an iterable with the string as a separator.
elements = ["apple", "banana", "cherry"]
print(", ".join(elements))  # Output: "apple, banana, cherry"

# str.ljust()
# Returns a left-justified version of the string, padded with a specified character.
text = "Python"
print(text.ljust(10, "-"))  # Output: "Python----"

# str.lower()
# Converts all characters in the string to lowercase.
word = "HELLO"
print(word.lower())  # Output: "hello"

# str.lstrip()
# Removes leading whitespace characters from the string.
text = "   Hello"
print(text.lstrip())  # Output: "Hello"

# str.maketrans()
# Creates a translation table for str.translate().
trans_table = str.maketrans("abc", "123")
print("abc".translate(trans_table))  # Output: "123"

# str.partition()
# Divides the string into a tuple (before_separator, separator, after_separator).
sentence = "Hello, World!"
print(sentence.partition(","))  # Output: ('Hello', ',', ' World!')

# str.removeprefix()
# Removes the specified prefix from the string.
text = "TestHook"
print(text.removeprefix("Test"))  # Output: "Hook"

# str.removesuffix()
# Removes the specified suffix from the string.
text = "MiscTests"
print(text.removesuffix("Tests"))  # Output: "Misc"

# str.replace()
# Replaces a substring with another substring in the string.
sentence = "Hello, World!"
print(sentence.replace("World", "Python"))  # Output: "Hello, Python!"

# str.rfind()
# Similar to find(), but searches from the end of the string.
sentence = "Python is awesome"
print(sentence.rfind("is"))  # Output: 7

# str.rindex()
# Similar to index(), but searches from the end of the string.
sentence = "Python is awesome"
print(sentence.rindex("is"))  # Output: 7

# str.rjust()
# Returns a right-justified version of the string.
text = "Python"
print(text.rjust(10, "-"))  # Output: "--Python"

# str.rpartition()
# Divides the string from the end into a tuple (before_separator, separator, after_separator).
sentence = "Hello, World!"
print(sentence.rpartition(","))  # Output: ('Hello', ',', ' World!')

# str.rsplit()
# Splits the string into a list of substrings, starting from the end.
sentence = "one two three"
print(sentence.rsplit())  # Output: ['one', 'two', 'three']

# str.rstrip()
# Removes trailing whitespace characters from the string.
text = "Hello   "
print(text.rstrip())  # Output: "Hello"

# str.split()
# Splits the string into a list of substrings.
sentence = "one two three"
print(sentence.split())  # Output: ['one', 'two', 'three']

# str.splitlines()
# Splits the string into a list of lines.
text = "Hello\nWorld"
print(text.splitlines())  # Output: ['Hello', 'World']

# str.startswith()
# Checks if the string starts with the specified substring.
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True

# str.strip()
# Removes leading and trailing whitespace characters from the string.
text = "   Hello   "
print(text.strip())  # Output: "Hello"

# str.swapcase()
# Swaps the case of all characters in the string.
text = "Hello"
print(text.swapcase())  # Output: "hELLO"

# str.title()
# Converts the string to title case.
text = "hello world"
print(text.title())  # Output: "Hello World"

# str.translate()
# Applies a translation table to the string.
trans_table = str.maketrans("abc", "123")
print("abc".translate(trans_table))  # Output: "123"

# str.upper()
# Converts all characters in the string to uppercase.
word = "hello"
print(word.upper())  # Output: "HELLO"

# str.zfill()
# Pads the string with zeros to reach a specified length.
text = "42"
print(text.zfill(5))  # Output: "00042"

# [Exercise]
# Given the string "The quick brown fox jumped over the lazy dog!",
# perform the following operations:

# 1. Remove all spaces from the string.
# 2. Convert all characters to lowercase.
# 3. Replace every occurrence of the letter 'o' with '0'.
# 4. Print the resulting string.

# Expected output: "thequickbr0wnf0xjumped0verthelazyd0g!"
