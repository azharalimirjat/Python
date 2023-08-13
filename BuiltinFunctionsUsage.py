"""
    The Python built-in functions are defined as the functions whose functionality
    is pre-defined in Python.
==>The python interpreter has several functions that are always present for use.
==>These functions are known as Built-in Functions.

==> We access all functions by dot(.) operator
Following are the examples:
"""
name= "Azhar Ali Mirjat"

# 1. lower(): to make all letters in small letters
print(name.lower())

# 2. upper(): to make all letters in capital letters
print(name.upper())

# 3. strip(): method used to remove leading and trailing
# whitespace characters (spaces, tabs, newlines) from a string.
# It returns a new string with the leading and trailing whitespace removed.
address = "   Jamshoro, Sindh, Pakistan"
print(address.strip())

# 4. split(): method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
print(name)

# 5. find(value): Used to find the position of any letter/word
print(name.find("Ali"))

# 6. replace(value_to_be_replaced, value_to_be_replaced_with):
# This method is used to replace one value to other value
print(name.replace("Ali","Hussain"))


# 7. startswith(value): tells whether the word starts with the given letter(value) or not
# It returns true if yes, and false if not
print(name.startswith("A"))

# 8. startswith(value): tells whether the word ends with the given letter(value) or not
# It returns true if yes, and false if not
print(name.startswith("x"))


# There may so many other built-in functions as well.sssss
