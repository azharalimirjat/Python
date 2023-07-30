"""
USER INPUT/String Formatting advance:
    the program pauses to ask the user for input.
    When the user enters some data and hits enter,
    Python stores the data in a variable as a string.

==> NOTE: Input always takes the string type values


Syntax:
variable_name = input("message")
EX:
"""

# name = input("Enter your name: ")



username = input("Enter your name : ")
password = input("Enter your password: ")

print(f"User name is {username}, and user password is {password}")


"""
=>Taking user input and changing it into integer format
Syntak:
variable = int(input("Enter your number"))
Example below:
"""
age = int(input("Enter your age : "))
print(age)
