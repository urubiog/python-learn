# Now is the turn for membership operators. Enjoy!

print("Membership time!")

# In Python, membership operators are used to check if a value exists in a sequence.

# in     -> Returns True if the value is present in the sequence
# not in -> Returns True if the value is NOT present in the sequence

# Examples:

# Using "in" with strings
word = "Python"
result_in = "t" in word  # True -> 't' is in the string "Python"
result_not_in = "z" in word  # False -> 'z' is not in the string "Python"

# Using "not in" with strings
result_not_in_example = "a" not in word  # True -> 'a' is not in the string "Python"

# Membership with explicit values
string_example = "abcdef"
result_check = "d" in string_example  # True -> 'd' is in "abcdef"

# [Exercise] What this will print?

sentence = "The quick brown fox jumps over the lazy dog"
print("fox" in sentence and "cat" not in sentence)  

# out:

