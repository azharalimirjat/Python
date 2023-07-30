"""
What is Python string formatting?
String formatting is also known as String interpolation.
It is the process of inserting a custom string or variable in predefined text.

==> We use curlie brackets for inserting custom string, known as Placeholder.

Syntax:
    print("My name is {custom_value1} and I am {custom_value2} ")
EX:
"""

# METHOD_01
name="Azhar Ali"
profession = "Student"
print(f"My name is {name}, and I am a {profession}")
# OUTPUT: "My name is Azhar Ali, and I am a Student"


# METHOD_02
message = "My name is {0}, and I am a {1}".format(name,profession)
print(message)
# OUTPUT: "My name is Azhar Ali, and I am a Student"
