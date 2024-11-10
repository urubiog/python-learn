# The art of Regular Expressions allows us to match complex patterns within strings,
# enabling efficient searching, extracting, and modifying operations. Using the `re` library,
# we can harness the power of pattern matching and create elegant solutions for a variety of tasks.

print("Mastering Regular Expressions with the 're' library!")

import re

# Let's explore the various methods and patterns available in the `re` library:

# Regular Expression Patterns:
# Here's a list of common pattern expressions used in regex:

# \d  : Matches any digit (0-9)
# \D  : Matches any non-digit character
# \w  : Matches any word character (alphanumeric + underscore)
# \W  : Matches any non-word character
# \s  : Matches any whitespace character (spaces, tabs, newlines)
# \S  : Matches any non-whitespace character
# \b  : Matches a word boundary (the position between a word and a non-word character)
# \B  : Matches a non-word boundary
# .   : Matches any character except newline
# ^   : Matches the beginning of the string
# $   : Matches the end of the string
# []  : A character class that matches any one of the enclosed characters
# ()  : Groups patterns together, allows capturing
# |   : Logical OR between patterns
# {n} : Matches exactly n occurrences of the preceding pattern
# {n,} : Matches n or more occurrences of the preceding pattern
# {n,m}: Matches between n and m occurrences of the preceding pattern

# re.match()  # Determines if the regular expression matches at the beginning of the string.
# This method returns a match object if the pattern matches at the start, otherwise None.
pattern = r"\d+"  # Pattern to match one or more digits
string = "123abc"
match_result = re.match(pattern, string)
print(f"re.match(): {match_result}")

# re.search()  # Searches the string for the first location where the regular expression pattern matches.
# Unlike `match()`, it does not require the match to occur at the beginning.
search_result = re.search(r"\d+", string)
print(f"re.search(): {search_result}")

# re.findall()  # Returns a list of all non-overlapping matches in the string.
# The result is a list of matches, or an empty list if no match is found.
findall_result = re.findall(r"\d+", "There are 123 apples and 456 oranges.")
print(f"re.findall(): {findall_result}")

# re.finditer()  # Returns an iterator yielding match objects for all non-overlapping matches.
# Useful for iterating over the matches.
finditer_result = re.finditer(r"\d+", "There are 123 apples and 456 oranges.")
for match in finditer_result:
    print(f"re.finditer(): {match.group()}")

# re.sub()  # Replaces the matched pattern with a string.
# You can also limit the number of substitutions and use a function to modify the replacement.
sub_result = re.sub(r"\d+", "NUMBER", "There are 123 apples and 456 oranges.")
print(f"re.sub(): {sub_result}")

# re.subn()  # Similar to `sub()`, but also returns the number of substitutions made.
subn_result = re.subn(r"\d+", "NUMBER", "There are 123 apples and 456 oranges.")
print(f"re.subn(): {subn_result}")

# re.split()  # Splits the string by the occurrences of the pattern.
split_result = re.split(r"\s+", "This is   a test   string.")
print(f"re.split(): {split_result}")

# re.compile()  # Compiles the regular expression pattern into a regular expression object.
# This object can be reused across multiple operations.
compiled_pattern = re.compile(r"\d+")
compiled_match = compiled_pattern.match("123abc")
print(f"re.compile() with match: {compiled_match}")

# re.fullmatch()  # Checks if the entire string matches the regular expression.
# It ensures the pattern matches the whole string, not just a part of it.
fullmatch_result = re.fullmatch(r"\d+", "123")
print(f"re.fullmatch(): {fullmatch_result}")

# re.escape()  # Escapes all non-alphanumeric characters in the string, so it can be used as a literal pattern.
escape_result = re.escape("Hello. How are you?")
print(f"re.escape(): {escape_result}")

# re.purge()  # Clears the internal regex cache (useful for memory management in large programs).
re.purge()  # We won't see output from this, but this clears the cache.

# Example of matching a pattern at the start of a string
pattern_start = r"^Hello"
start_match = re.match(pattern_start, "Hello world!")
print(f"Pattern match at start of string: {start_match}")

# Example of matching a pattern at the end of a string
pattern_end = r"world!$"
end_match = re.match(pattern_end, "Hello world!")
print(f"Pattern match at end of string: {end_match}")

# Exercise:
# Write a regular expression that matches an email address. It should match strings like:
# "example@example.com" but not "example@.com" or "example.com"
email_string = "Contact me at example@example.com"
email_pattern = r"[Insert you pattern here]"
email_match = re.match(email_pattern, email_string)
print(f"Email match: {email_match}")
